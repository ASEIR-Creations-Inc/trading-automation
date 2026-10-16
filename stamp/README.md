# aseir-stamp

Every chart, trade preview and report we deliver carries a **settings stamp**: the first
12 hex characters of the SHA-256 of that run's settings, serialised as canonical JSON
(keys sorted, no whitespace, UTF-8). With the settings file in hand you can recompute
the stamp yourself and confirm the result was produced with exactly what you approved.

```bash
pip install ./stamp
aseir-stamp compute examples/stamp-settings.json
# 2f8e8943959c
aseir-stamp verify examples/stamp-settings.json 2f8e8943959c
# OK  2f8e8943959c  settings match the stamp
```

The settings include a `data` fingerprint of the market data the run read, so a stamp
also changes if a single candle in the input changes.

No dependencies, standard library only. MIT licensed.
