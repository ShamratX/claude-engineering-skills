---
name: web3-development
description: Smart contracts and dApps on EVM chains - Solidity, Hardhat, Foundry, ethers.js/viem/wagmi, OpenZeppelin, Chainlink, wallets, tokens, DeFi, deploy and verify scripts. Use for writing, changing, deploying, or integrating contracts. Pair with security for audits or anything that holds value.
---

# Web3 Development

## 0. Caveman check
Active if the `caveman` skill is listed or the `caveman` CLI is on PATH. If missing, install it yourself: `claude plugin marketplace add JuliusBrussee/caveman && claude plugin install caveman@caveman` (takes effect next session). Blocked → continue normally. Terse replies; code and errors verbatim.
Here: shrink installs, compile output, gas reports, and full-suite runs. Keep full: revert reasons, failing test traces, storage layouts, ABIs, addresses, tx hashes, and chain IDs.

## Context
- **Toolchain and versions first:** `hardhat.config.*` / `foundry.toml`, compiler version, and the installed versions of OpenZeppelin, ethers/viem, and Hardhat (grep the lockfile or `lib/` remappings). Majors differ:
  - OpenZeppelin 4 → 5: import paths moved, `Ownable` takes an initial owner.
  - ethers 5 → 6: `BigNumber` → `bigint`, `ethers.utils.*` removed.
  - Hardhat 2 → 3: config format and plugins changed.
  Check before writing code against them.
- **Then:** the contract in scope, its parents, and the interfaces it calls. For library code in `node_modules`/`lib`, read the specific function you depend on, not the package.
- **Deploy work:** deploy script, network config (never print keys or RPC secrets), saved addresses/ABIs.
- **dApp work:** the contract hook/service, the ABI source, and the chain config.

## Contracts
- Code holds value and is public and permanent once deployed. Design for that. Full review → `security`.
- Use audited OpenZeppelin components. Don't reimplement standards.
- Pragma: match the project. Pin an exact version for contracts that will be deployed.
- Checks-effects-interactions; `ReentrancyGuard` on value transfers and untrusted calls; `SafeERC20`; custom errors; events for state changes; bounded loops; explicit visibility; `immutable`/`constant` for fixed values.
- Upgradeable only if the project already is or the user asks: keep storage layout, use initializers (no constructor logic), call `_disableInitializers()` in the implementation's constructor.
- Keep owner powers minimal and documented. Put hard caps on fees and taxes.
- Chainlink: for price feeds, check `answer > 0`, `updatedAt` staleness, and `decimals()`. Use VRF, never block values, for randomness. Take feed/coordinator addresses for the target network from official Chainlink docs.
- Amounts: use the token's `decimals`, never assume 18. Multiply before dividing.

## Deploy
- Local → testnet → mainnet. Any real-value chain needs explicit user approval every time. Confirm network, chain ID, and constructor args first.
- Keys come from env, keystore, or hardware wallet only. Never in code, chat, or logs.
- Deploy by script, record addresses per network, verify source on the explorer.

## dApp
- Match the library already used (ethers, viem, wagmi).
- Check chain ID and prompt a switch; handle wallet rejection without crashing; show pending/confirmed/failed with the tx hash; wait for the receipt, then refetch state.

## Verify
Clean compile → targeted tests (`npx hardhat test <file>`, `forge test --match-test <name>`) → full suite → coverage and Slither when available and relevant. Integrations with live protocols → fork tests.
