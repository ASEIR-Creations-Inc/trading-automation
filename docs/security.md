# Security and risk controls

## Exchange access

- **Trade-only keys.** API keys must have withdrawals disabled. Keys with withdrawal
  permission are refused.
- **IP-restricted.** Keys are bound to the static IP of the server that runs your system.
- **Stored as secrets.** Keys live in a root-only environment file on the server, never in
  source code, logs, chat messages or repositories.
- **Revocable by you at any time** from your exchange account, which stops the system
  immediately.

## Execution safeguards

- Every entry has a protective stop placed with it.
- Entries are skipped, and reported, when price has moved past the allowed slippage.
- Position size respects your risk-per-trade, leverage and margin-per-position limits.
- Exchange rate limits are respected, including backing off for the exact ban window
  if one is ever imposed.
- A watchdog alerts you if the system stops scanning, and again when it recovers.

## Change control

- Demo first, for every new system and every material rule change.
- Go-live and limit changes require your written approval.
- Each deployed configuration carries a settings stamp, so you always know which version
  is trading.

## Confidentiality

- Client strategies, settings and results are never published or reused.
- NDA available on request before you share any details.

## Reporting a vulnerability

Please use GitHub's private vulnerability reporting on this repository
(**Security → Report a vulnerability**) rather than a public issue.
