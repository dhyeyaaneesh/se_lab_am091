import re
import pytest
from hypothesis import given, strategies as st

from traffic_fine import parse_ticket_id, total_fines, speed_excess


def _call_accepting_valueerror(function, value, valid_result):
    """Malformed inputs may raise ValueError; unexpected exceptions are failures."""
    try:
        result = function(value)
    except ValueError:
        return
    except Exception as exc:
        pytest.fail(f"{function.__name__} raised unexpected {type(exc).__name__}: {exc}")
    assert valid_result(result), f"Unexpected result for input {value!r}: {result!r}"


@given(st.one_of(st.text(), st.none(), st.integers()))
def test_parse_ticket_id_handles_arbitrary_inputs(value):
    _call_accepting_valueerror(
        parse_ticket_id,
        value,
        lambda result: (
            isinstance(result, tuple)
            and len(result) == 3
            and isinstance(result[0], str)
            and result[0] == result[0].upper()
            and isinstance(result[1], int)
            and isinstance(result[2], int)
        ),
    )


@given(
    prefix=st.text(alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", min_size=1, max_size=8),
    year=st.integers(min_value=1000, max_value=9999),
    serial=st.integers(min_value=0, max_value=999999),
)
def test_parse_ticket_id_valid_generated_ids(prefix, year, serial):
    result = parse_ticket_id(f"{prefix}-{year}-{serial}")
    assert result == (prefix.upper(), year, serial)


@given(st.one_of(st.text(), st.none(), st.integers()))
def test_total_fines_handles_arbitrary_inputs(value):
    _call_accepting_valueerror(
        total_fines,
        value,
        lambda result: isinstance(result, int) and 0 <= result <= 10000,
    )


@given(st.lists(st.integers(min_value=0, max_value=20000), min_size=1, max_size=30))
def test_total_fines_is_nonnegative_and_capped(amounts):
    csv_value = ",".join(str(amount) for amount in amounts)
    assert total_fines(csv_value) == min(sum(amounts), 10000)


@given(st.one_of(st.text(), st.none(), st.integers()))
def test_speed_excess_handles_arbitrary_inputs(value):
    _call_accepting_valueerror(
        speed_excess,
        value,
        lambda result: isinstance(result, int),
    )


@given(
    speed=st.integers(min_value=0, max_value=1000),
    limit=st.integers(min_value=1, max_value=300),
)
def test_speed_excess_matches_percentage_formula(speed, limit):
    assert speed_excess(f"{speed}/{limit}") == (speed - limit) * 100 // limit


@pytest.mark.parametrize("bad_ticket", ["", "TF-2024", "TF-20X4-0456", "TF-2024-04-56", "-2024-45"])
def test_parse_ticket_id_rejects_malformed_ids(bad_ticket):
    with pytest.raises(ValueError):
        parse_ticket_id(bad_ticket)


@pytest.mark.parametrize("bad_csv", ["", "1,,2", "one,2", "-1,2", "1,"])
def test_total_fines_rejects_malformed_amounts(bad_csv):
    with pytest.raises(ValueError):
        total_fines(bad_csv)


@pytest.mark.parametrize("bad_reading", ["", "70", "70/0", "-1/60", "fast/60", "70/60/50"])
def test_speed_excess_rejects_malformed_readings(bad_reading):
    with pytest.raises(ValueError):
        speed_excess(bad_reading)
