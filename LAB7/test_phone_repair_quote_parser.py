from hypothesis import given, strategies as st
from phone_repair_quote_parser import mask_imei, parse_parts_order, parse_model

inputs = st.one_of(
    st.text(),
    st.none(),
    st.integers(),
    st.booleans(),
    st.binary(),
    st.lists(st.text()),
    st.dictionaries(st.text(), st.integers()),
)


@given(inputs)
def test_mask_imei_no_crash(s):
    try:
        result = mask_imei(s)
    except Exception as exc:
        raise AssertionError(f"mask_imei crashed with {s!r}: {exc}") from exc
    assert isinstance(result, str)


@given(inputs)
def test_parse_parts_order_no_crash(s):
    try:
        result = parse_parts_order(s)
    except Exception as exc:
        raise AssertionError(f"parse_parts_order crashed with {s!r}: {exc}") from exc
    assert isinstance(result, dict)
    assert all(isinstance(part, str) and isinstance(quantity, int)
               for part, quantity in result.items())


@given(inputs)
def test_parse_model_no_crash(s):
    try:
        result = parse_model(s)
    except Exception as exc:
        raise AssertionError(f"parse_model crashed with {s!r}: {exc}") from exc
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert all(isinstance(value, str) for value in result)
