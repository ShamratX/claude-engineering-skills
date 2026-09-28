---
name: web3-development
description: Build, test, and deploy smart contracts and dApps - Solidity, Hardhat, Foundry, OpenZeppelin, ethers.js/viem, wallet connection, ERC-20/721 tokens, and DEX integrations. Use for any blockchain, token, or contract work.
---

# Web3 Development

## Golden rules

1. **Never handle real private keys or seed phrases in code or chat.** Load
   them from `.env`, which must be in `.gitignore`. Only `.env.example` with
   placeholders is committed.
2. **Testnet first, always.** Deploy to a local node, then a testnet
   (Sepolia, BSC Testnet, etc.). Mainnet deployment needs explicit approval
   from the user every time.
3. **Contracts are immutable once deployed.** Treat every line as permanent
   and public.

## Workflow

1. Read `hardhat.config.js` / `foundry.toml`, the Solidity version, and the
   existing contracts before writing new ones.
2. Use **OpenZeppelin** for standard pieces (ERC20, ERC721, Ownable,
   AccessControl, ReentrancyGuard). Do not reimplement them.
3. Write tests alongside the contract (see the `testing` skill).
4. Compile with warnings treated as problems to fix.
5. Deploy with a script, save deployed addresses to a file, and verify the
   source on the block explorer.

## Solidity conventions

- Pin the compiler: `pragma solidity 0.8.24;` (not `^`).
- Follow **checks-effects-interactions**: validate, update state, then make
  external calls.
- Use `ReentrancyGuard` on functions that send ETH or call untrusted contracts.
- Use custom errors (`error NotOwner();`) instead of long revert strings.
- Emit events for every important state change.
- Mark functions `external` when not called internally; `view`/`pure` where
  possible.
- Avoid unbounded loops over user-controlled arrays.
- Use `SafeERC20` for token transfers.
- Access control on every admin function; consider a timelock or multisig
  for owner powers.

## Token-specific checks (ERC-20 / factory contracts)

- [ ] Total supply and decimals are correct
- [ ] Owner powers (mint, pause, blacklist, fees) are documented and limited
- [ ] Fee and tax values have hard maximums
- [ ] Liquidity and router addresses are configurable per network, not hardcoded
- [ ] No hidden mint or transfer-blocking logic

## Frontend (dApp)

- Use ethers.js v6 or viem + wagmi. Match whatever the project already uses.
- Always check the connected chain ID and prompt the user to switch.
- Show pending, confirmed, and failed transaction states with the tx hash.
- Handle user rejection of a wallet request without crashing.
- Format token amounts with the token's `decimals`, never assume 18.

## Before deploying

- [ ] All tests pass, including edge cases and failure paths
- [ ] Coverage checked on critical functions
- [ ] Static analysis run (Slither) and findings reviewed
- [ ] Constructor arguments double-checked for the target network
- [ ] Deployer wallet funded on the correct network
- [ ] User has confirmed the target network
