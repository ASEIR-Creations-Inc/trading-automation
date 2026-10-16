import json
import hashlib
from pathlib import Path

import pytest

from aseir_stamp import canonical, main, stamp, verify

EXAMPLE = Path(__file__).resolve().parent.parent / "examples" / "stamp-settings.json"
PUBLISHED = "2f8e8943959c"


def load_example():
    return json.loads(EXAMPLE.read_text(encoding="utf-8"))


def test_published_example_matches_the_stamp_on_every_chart():
    assert stamp(load_example()) == PUBLISHED


def test_key_order_does_not_matter():
    s = load_example()
    assert stamp(dict(reversed(list(s.items())))) == stamp(s)


@pytest.mark.parametrize("key,value", [("extend_pct", 4.5), ("sma", 55), ("data", "0" * 16)])
def test_any_change_breaks_the_stamp(key, value):
    assert stamp({**load_example(), key: value}) != PUBLISHED


def test_canonical_form_is_plain_sha256():
    s = {"b": 1, "a": "x"}
    assert canonical(s) == b'{"a":"x","b":1}'
    assert stamp(s) == hashlib.sha256(b'{"a":"x","b":1}').hexdigest()[:12]


def test_verify_tolerates_case_and_whitespace():
    assert verify(load_example(), f"  {PUBLISHED.upper()} \n")


def test_nan_is_rejected():
    with pytest.raises(ValueError):
        stamp({"x": float("nan")})


def test_cli(capsys):
    assert main(["compute", str(EXAMPLE)]) == 0
    assert capsys.readouterr().out.strip() == PUBLISHED
    assert main(["verify", str(EXAMPLE), PUBLISHED]) == 0
    assert main(["verify", str(EXAMPLE), "000000000000"]) == 1
    assert "MISMATCH" in capsys.readouterr().out
