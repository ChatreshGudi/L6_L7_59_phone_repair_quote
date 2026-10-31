"""Line-coverage tests for the phone repair quote application."""

import pytest

from phone_repair_quote import repair_days, repair_quote, trade_in_value


@pytest.mark.parametrize(
    ("part", "tier", "warranty", "express", "expected"),
    [
        ("screen", "budget", False, False, 4600),
        ("battery", "budget", False, True, 2300),
        ("camera", "flagship", False, False, 5300),
        ("charging_port", "flagship", True, False, 300),
        ("screen", "flagship", True, True, 9100),
    ],
)
def test_repair_quote_calculates_supported_quotes(part, tier, warranty, express, expected):
    assert repair_quote(part, tier, warranty, express) == expected


def test_repair_quote_rejects_unknown_part():
    with pytest.raises(ValueError, match="unknown part"):
        repair_quote("speaker", "budget", False, False)


def test_repair_quote_rejects_unknown_brand_tier():
    with pytest.raises(ValueError, match="unknown brand tier"):
        repair_quote("screen", "premium", False, False)


@pytest.mark.parametrize(
    ("part", "in_stock", "technicians_free", "expected"),
    [
        ("battery", True, 2, 1),
        ("camera", False, 0, 8),
        ("screen", False, 1, 6),
        ("battery", False, 1, 3),
    ],
)
def test_repair_days_estimates_turnaround(part, in_stock, technicians_free, expected):
    assert repair_days(part, in_stock, technicians_free) == expected


@pytest.mark.parametrize(
    ("price", "age", "cracked", "expected"),
    [
        (10000, 6, False, 6000),
        (10000, 18, False, 4000),
        (10000, 36, True, 1000),
        (10000, 50, False, 0),
    ],
)
def test_trade_in_value_estimates_supported_phones(price, age, cracked, expected):
    assert trade_in_value(price, age, cracked) == expected


@pytest.mark.parametrize(("price", "age"), [(0, 0), (10000, -1)])
def test_trade_in_value_rejects_invalid_inputs(price, age):
    with pytest.raises(ValueError, match="invalid input"):
        trade_in_value(price, age, False)
