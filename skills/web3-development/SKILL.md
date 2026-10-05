---
name: web3-development
description: Smart contracts and dApps on EVM chains - Solidity, Hardhat, Foundry, ethers.js/viem/wagmi, OpenZeppelin, Chainlink, wallets, tokens, DeFi, deploy/verify scripts. Use for writing, changing, deploying, or integrating contracts. Not for non-chain web work (web-development).
---

# Web3 Development

**Caveman** (per CLAUDE.md): shrink installs, compile output, gas reports, full-suite runs. Keep full: revert reasons, failing test traces, storage layouts, ABIs, addresses, tx hashes, chain IDs.

## Context
- **Toolchain + versions first:** `hardhat.config.*` / `foundry.toml`, compiler version, installed OpenZeppelin, ethers/viem, Hardhat versions (lockfile or `lib/` remappings). Majors break APIs:
  - OpenZeppelin 4 → 5: import paths moved; `Ownable` takes an initial owner.
  - ethers 5 → 6: `BigNumber` → `bigint`; `ethers.utils.*` removed.
  - Hardhat 2 → 3: config format and plugins changed.
- **Then:** the contract in scope, its parents, and the interfaces it calls. Library code (`node_modules`, `lib`): read only the function you depend on.
- **Deploy:** deploy script, network config (never print keys/RPC secrets), saved addresses/ABIs.
- **dApp:** contract hook/service, ABI source, chain config.

## Contracts
- Audited OpenZeppelin components; don't reimplement standards. Audit-level review → `security`.
- Pragma: match the project; pin an exact version for deployable contracts.
- Checks-effects-interactions; `ReentrancyGuard` on value transfers/untrusted calls; `SafeERC20`; custom errors; events for state changes; bounded loops; explicit visibility; `immutable`/`constant` for fixed values.
- Upgradeable only if the project already is or the user asks: preserve storage layout, initializers instead of constructor logic, `_disableInitializers()` in the implementation constructor.
- Minimal, documented owner powers; hard caps on fees/taxes.
- Chainlink feeds: check `answer > 0`, `updatedAt` staleness, `decimals()`. Randomness via VRF, never block values. Feed/coordinator addresses from official Chainlink docs for the target network.
- Use the token's `decimals`, never assume 18. Multiply before dividing.

## Deploy
- Local → testnet → mainnet. Real-value chains: explicit approval every time; confirm network, chain ID, constructor args first.
- Keys only from env, keystore, or hardware wallet.
- Deploy by script, record addresses per network, verify source on the explorer.

## dApp
Match the existing library (ethers, viem, wagmi). Check chain ID and prompt a switch; handle wallet rejection; show pending/confirmed/failed with tx hash; wait for the receipt, then refetch state.

## Verify
Clean compile → targeted tests (`npx hardhat test <file>`, `forge test --match-test <name>`) → full suite → coverage and Slither when available. Live-protocol integrations → fork tests.
