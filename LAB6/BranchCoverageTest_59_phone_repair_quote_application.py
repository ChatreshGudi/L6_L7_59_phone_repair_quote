"""Decision-outcome tests for the phone repair quote application."""

import pytest

from phone_repair_quote import repair_days, repair_quote, trade_in_value


@pytest.mark.parametrize(
    ("part", "tier", "warranty", "express", "expected"),
    [
        ("screen", "budget", False, False, 4600),
        ("battery", "flagship", False, False, 3300),
        ("screen", "flagship", False, True, 9100),
        ("camera", "budget", True, False, 300),
        ("screen", "budget", True, False, 4600),
    ],
)
def test_repair_quote_decision_outcomes(part, tier, warranty, express, expected):
    assert repair_quote(part, tier, warranty, express) == expected


@pytest.mark.parametrize(
    ("part", "in_stock", "technicians_free", "expected"),
    [
        ("screen", True, 0, 3),
        ("camera", False, 1, 6),
        ("battery", False, 2, 3),
        ("charging_port", True, 2, 1),
    ],
)
def test_repair_days_decision_outcomes(part, in_stock, technicians_free, expected):
    assert repair_days(part, in_stock, technicians_free) == expected


@pytest.mark.parametrize(
    ("price", "age", "cracked", "expected"),
    [
        (10000, 12, False, 6000),
        (10000, 13, False, 4000),
        (10000, 24, True, 2000),
        (10000, 25, False, 2000),
        (10000, 49, True, 0),
    ],
)
def test_trade_in_decision_boundaries(price, age, cracked, expected):
    assert trade_in_value(price, age, cracked) == expected


@pytest.mark.parametrize(("price", "age"), [(0, 12), (10000, -1)])
def test_trade_in_rejects_each_invalid_input_condition(price, age):
    with pytest.raises(ValueError, match="invalid input"):
        trade_in_value(price, age, False)
