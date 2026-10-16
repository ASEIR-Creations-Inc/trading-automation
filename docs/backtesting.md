# Backtesting methodology

What we test, how we report it, and what you receive. This page describes *what* our
engine guarantees, not how it is built. Implementation walkthroughs are available under NDA.

## Principles

**Test what will actually trade.** The backtest runs the same rule set as the live system:
same detection logic, same entry and exit mechanics, same sizing. If a rule cannot be
executed live, it is not in the backtest.

**Resolve what happens inside the bar.** A signal timeframe of 2h says nothing about the
order in which a stop and a target were touched within those two hours. We resolve fills,
stops and exits on finer data. Where even that is ambiguous, we run both the best and the
worst plausible sequence and report the range.

**Price costs from live conditions.** Taker fees, per-symbol spread measured from the live
order book, and funding charged at each settlement a position spans. Every result is
reported gross and net.

**Simulate the account, not just the signal.** Position sizing from equity and stop distance,
leverage and margin limits, exchange minimum order size, one position per symbol, entries
skipped when price has already moved past the allowed slippage. A strategy that only works
with unlimited capital or perfect fills is reported as such.

**Guard against self-deception.** Out-of-sample periods, random-entry baselines with the same
exits and costs, full parameter sweeps (not just the best cell), and per-symbol and
per-period breakdowns, so one lucky coin cannot carry a result.

## Reproducibility

- Market data is fetched once into a versioned local store at several resolutions. Reruns are
  fast and read identical bytes.
- Every run's settings, including a fingerprint of the data it read, produce a
  **settings stamp** ([`stamp/`](../stamp/)). The stamp is printed on every chart, report and
  trade preview.
- Any trade in any run can be redrawn on demand in the live-alert chart style through the
  trade explorer bot.

## What you receive

| Deliverable | Contents |
|---|---|
| Specification | Your rules restated precisely, with the parameters that will be stamped |
| Backtest report | Gross and net results, drawdown, win rate, R distribution, exits by type, per-symbol and per-month breakdowns, sweep tables |
| Trade list | Every trade with times, prices, exit reason, result in R and in account currency ([sample](../examples/backtest-trades-sample.csv)) |
| Trade explorer | A Telegram bot to browse the list and request any trade as a chart |
| Verdict | A plain-language conclusion, including "no edge after costs" when that is what the data says |

## Sample run

The sample in this repository is our own SMA50 pullback strategy: 62 markets, setups on 2h,
execution resolved on 15m, live-priced costs, a $20 test account. It is **not profitable**
after costs. We publish it because an honest negative result demonstrates the tooling better
than a flattering one.

Settings stamp `2f8e8943959c`, settings in [`examples/stamp-settings.json`](../examples/stamp-settings.json).
