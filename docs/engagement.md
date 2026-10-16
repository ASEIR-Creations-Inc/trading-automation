# Engagements

## Service tiers

| | Alerts | Integration | Operations |
|---|---|---|---|
| Strategy specification and sign-off | ✓ | ✓ | as needed |
| Backtest report and trade explorer | ✓ | ✓ | re-runs on request |
| Live scanner with chart alerts in Telegram | ✓ | ✓ | maintained |
| Order execution on your demo account | | ✓ | maintained |
| Go-live on your live account (on approval) | | ✓ | maintained |
| Account health reports and incident alerts | | ✓ | ✓ |
| Watchdog, restarts, exchange API changes | | | ✓ |
| Rule adjustments and monthly report | | | ✓ |
| Billing | fixed project fee | fixed project fee | monthly retainer |

Operations can be added to either project tier, or taken on its own for an existing system
that needs monitoring.

## Process

1. **Brief** ([template](../examples/client-brief.yaml)): your rules in your own words,
   markets, timeframes, exchange, what you want to see in an alert and when.
2. **Specification**: we restate the rules precisely and list every open question. You sign
   off, and the approved settings are stamped.
3. **Backtest**: report, trade list and trade explorer bot. We iterate with you until each
   inspected trade matches your intent.
4. **Demo**: the system runs against your exchange demo account with alerts and health
   reports in Telegram. Minimum two weeks before any go-live discussion.
5. **Go-live**: on your written approval, with position and loss limits you choose.
6. **Operations**: monitoring, maintenance, adjustments and monthly reporting.

## What we need from you

- A description of the strategy, with screenshots of past setups if you have them.
- Exchange account with a **trade-only** API key for demo (and later live). See [security](security.md).
- A Telegram account for the private ops chat, and optionally a channel for alerts.

## What we will not do

- Promise or imply returns.
- Hold, move or have withdrawal access to client funds.
- Reuse or publish a client's strategy.
- Go live without a demo period and written approval.
