#!/usr/bin/env python3
"""Validate skills, CLAUDE.md, and the memory store. Stdlib only, no network, read-only.

Usage: python scripts/validate.py [--installed]
  --installed  also compare the repo with the copies installed in ~/.claude/
Exit code 1 if any ERROR is found; WARNs don't fail.
"""
import datetime as dt
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MEMORY = ROOT / "memory"
TODAY = dt.date.today()
STALE_DAYS = 180
SKILL_WARN_BYTES = 6000
CLAUDE_WARN_BYTES = 10500
REF_WARN_BYTES = 30000
LICENSE_NAMES = ("LICENSE", "LICENSE.txt", "LICENSE.md")

SECRET_PATTERNS = {
    "private key block": r"-----BEGIN [A-Z ]*PRIVATE KEY-----",
    "AWS access key": r"\bAKIA[0-9A-Z]{16}\b",
    "GitHub token": r"\bgh[pousr]_[A-Za-z0-9]{36,}\b",
    "Slack token": r"\bxox[abpors]-[A-Za-z0-9-]{10,}",
    "OpenAI/Anthropic key": r"\bsk-(ant-)?[A-Za-z0-9_-]{20,}",
    "Google API key": r"\bAIza[0-9A-Za-z_-]{35}\b",
    "hex private key": r"\b(0x)?[0-9a-fA-F]{64}\b",
    "JWT": r"\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}",
    "credential assignment": r"(?i)\b(password|passwd|secret|api[_-]?key|token|mnemonic|seed[_ ]phrase)\b\s*[:=]\s*['\"]?[^\s'\"`<>]{8,}",
}
ENTRY_RE = re.compile(r"^- \d{4}-\d{2}-\d{2} · .+ · (confirmed|unverified|superseded)\b")

errors, warns = [], []


def err(msg):
    errors.append(msg)


def warn(msg):
    warns.append(msg)


def rel(p):
    return p.relative_to(ROOT).as_posix()


def front_matter(text):
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", text, re.S)
    if not m:
        return None
    out = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            out[k.strip()] = v.strip()
    return out


def parse_date(s):
    try:
        return dt.date.fromisoformat(s)
    except (TypeError, ValueError):
        return None


def check_skills():
    skills = {}
    for d in sorted((ROOT / "skills").iterdir()):
        if not d.is_dir():
            continue
        f = d / "SKILL.md"
        if not f.exists():
            err(f"{rel(d)}: missing SKILL.md")
            continue
        text = f.read_text(encoding="utf-8")
        fm = front_matter(text)
        if fm is None:
            err(f"{rel(f)}: missing front matter")
            continue
        name, desc = fm.get("name", ""), fm.get("description", "")
        if name != d.name:
            err(f"{rel(f)}: name '{name}' != folder '{d.name}'")
        if not re.fullmatch(r"[a-z0-9-]{1,64}", name):
            err(f"{rel(f)}: name must be lowercase letters, digits, hyphens (max 64)")
        if not desc:
            err(f"{rel(f)}: empty description")
        elif len(desc) > 1024:
            err(f"{rel(f)}: description {len(desc)} chars > 1024")
        size = len(text.encode("utf-8"))
        if size > SKILL_WARN_BYTES and not (d / "SOURCE.md").exists():  # copied files stay unmodified
            warn(f"{rel(f)}: {size} bytes; move detail into a reference file")
        check_skill_files(d, text)
        skills[name] = text
    return skills


def check_skill_files(d, text):
    """Links resolve, references stay small, copied material keeps its license and is registered."""
    links = re.findall(r"\]\(([^)#\s]+)\)", text) + re.findall(r"`((?:references|rules)/[\w./-]+\.md)`", text)
    for target in links:
        if "://" in target or target.startswith("mailto:"):
            continue
        if not (d / target).exists():
            err(f"{rel(d)}/SKILL.md: broken link '{target}'")
    for f in d.rglob("*.md"):
        if f.name != "SKILL.md" and f.stat().st_size > REF_WARN_BYTES:
            warn(f"{rel(f)}: {f.stat().st_size} bytes; split it")
    if (d / "SOURCE.md").exists():
        if not any(f.name in LICENSE_NAMES for f in d.rglob("LICENSE*")):
            err(f"{rel(d)}: has SOURCE.md but no LICENSE file")
        registry = ROOT / "docs" / "third-party.md"
        if not registry.exists() or f"`skills/{d.name}" not in registry.read_text(encoding="utf-8"):
            err(f"{rel(d)}: copied material not listed in docs/third-party.md")


def check_claude_md():
    f = ROOT / "CLAUDE.md"
    text = f.read_text(encoding="utf-8")
    if "{{MEMORY_ROOT}}" not in text:
        err("CLAUDE.md: missing {{MEMORY_ROOT}} placeholder")
    if "\n## This repo" not in text:
        err("CLAUDE.md: missing '## This repo' section (install strips from there)")
    size = len(text.encode("utf-8"))
    if size > CLAUDE_WARN_BYTES:
        warn(f"CLAUDE.md: {size} bytes; it loads every session, move domain detail into skills")
    return text


def check_duplicates(claude_text, skills):
    """Flag long identical lines shared by CLAUDE.md and skills, or by two skills."""
    seen = {}
    sources = {"CLAUDE.md": claude_text, **{f"skills/{n}": t for n, t in skills.items()}}
    for src, text in sources.items():
        for line in {l.strip() for l in text.splitlines()}:
            if len(line) >= 60 and not line.startswith(("#", "---")):
                seen.setdefault(line, []).append(src)
    for line, srcs in seen.items():
        if len(srcs) > 1:
            warn(f"duplicate instruction in {', '.join(srcs)}: {line[:70]}...")


def check_memory():
    if not MEMORY.exists():
        err("memory/: missing")
        return
    for f in sorted(MEMORY.rglob("*.md")):
        r = rel(f)
        if f.name == "README.md" or "_template" in f.parts:
            continue
        text = f.read_text(encoding="utf-8")
        fm = front_matter(text)
        updated = parse_date(fm.get("updated")) if fm else None
        if not updated:
            err(f"{r}: missing or invalid 'updated: YYYY-MM-DD' front matter")
        elif (TODAY - updated).days > STALE_DAYS:
            warn(f"{r}: not updated for {(TODAY - updated).days} days; review for staleness")
        if f.name == "INDEX.md" or f.parent.name == "research":  # research notes use their own format
            continue
        for i, line in enumerate(text.splitlines(), 1):
            if not line.startswith("- "):
                continue
            if not ENTRY_RE.match(line):
                warn(f"{r}:{i}: entry not in '- YYYY-MM-DD · fact · confirmed|unverified' format")
            m = re.search(r"review-by: (\d{4}-\d{2}-\d{2})", line)
            if m and (parse_date(m.group(1)) or TODAY) < TODAY:
                warn(f"{r}:{i}: research past review-by date")
    index = MEMORY / "INDEX.md"
    if index.exists():
        for line in index.read_text(encoding="utf-8").splitlines():
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) < 4 or cells[0] in ("slug", "") or set(cells[0]) <= {"-"}:
                continue
            slug, path = cells[0], cells[1]
            if not (MEMORY / "projects" / slug).is_dir():
                err(f"memory/INDEX.md: project folder missing for '{slug}'")
            if not Path(path).exists():
                warn(f"memory/INDEX.md: path for '{slug}' not found on this machine: {path}")
    else:
        warn("memory/INDEX.md: missing (copy memory/_template/INDEX.md)")


def check_secrets():
    for f in ROOT.rglob("*"):
        if not f.is_file() or ".git" in f.parts or f.suffix not in (".md", ".py", ".json", ".txt", ".yml", ".yaml", ".toml", ""):
            continue
        if f.resolve() == Path(__file__).resolve():
            continue  # pattern definitions would match themselves
        try:
            lines = f.read_text(encoding="utf-8").splitlines()
        except (UnicodeDecodeError, OSError):
            continue
        for i, line in enumerate(lines, 1):
            for label, pat in SECRET_PATTERNS.items():
                if re.search(pat, line):
                    err(f"{rel(f)}:{i}: possible {label} (value not shown)")


def check_installed(claude_text, skills):
    home = Path.home() / ".claude"
    expected = claude_text.split("\n## This repo")[0].rstrip()
    expected = expected.replace("{{MEMORY_ROOT}}", MEMORY.as_posix())
    inst = home / "CLAUDE.md"
    if not inst.exists():
        warn("~/.claude/CLAUDE.md: not installed")
    else:
        got = inst.read_text(encoding="utf-8-sig").replace("\r\n", "\n").rstrip()
        if "{{MEMORY_ROOT}}" in got:
            err("~/.claude/CLAUDE.md: placeholder not replaced")
        if got != expected.replace("\r\n", "\n"):
            warn("~/.claude/CLAUDE.md: differs from repo; re-run install step 3")
    for name in skills:
        src, dst = ROOT / "skills" / name, home / "skills" / name
        if not dst.exists():
            warn(f"~/.claude/skills/{name}: not installed")
            continue
        for f in src.rglob("*"):
            if not f.is_file():
                continue
            g = dst / f.relative_to(src)
            if not g.exists() or g.read_bytes().replace(b"\r\n", b"\n") != f.read_bytes().replace(b"\r\n", b"\n"):
                warn(f"~/.claude/skills/{name}/{f.relative_to(src).as_posix()}: missing or differs; re-run install step 2")


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    skills = check_skills()
    claude_text = check_claude_md()
    check_duplicates(claude_text, skills)
    check_memory()
    check_secrets()
    if "--installed" in sys.argv:
        check_installed(claude_text, skills)
    for m in errors:
        print(f"ERROR {m}")
    for m in warns:
        print(f"WARN  {m}")
    print(f"{len(skills)} skills, {len(errors)} errors, {len(warns)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
