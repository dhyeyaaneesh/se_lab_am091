import pytest
from traffic_fine import speeding_fine, license_action, total_penalty

@pytest.mark.parametrize("speed,limit,zone,expected", [
    (60, 60, "city", 0),
    (61, 60, "school", 2000),
    (81, 60, "highway", 2000),
    (101, 60, "city", 1500),
    (82, 60, "school", 4000),
    (70, 60, "unknown", 500),
])
def test_speeding_fine_all_decision_outcomes(speed, limit, zone, expected):
    assert speeding_fine(speed, limit, zone) == expected

@pytest.mark.parametrize("points,commercial,repeat,expected", [
    (12, True, False, "revoke"),
    (12, False, False, "suspend"),
    (8, False, True, "suspend"),
    (8, False, False, "warning"),
    (4, False, False, "notice"),
    (3, False, False, "none"),
])
def test_license_action_all_decision_outcomes(points, commercial, repeat, expected):
    assert license_action(points, commercial, repeat) == expected

def test_total_penalty_empty_list():
    assert total_penalty([]) == 0

def test_total_penalty_non_empty_below_cap():
    assert total_penalty([100, 200, 300]) == 600

def test_total_penalty_exactly_at_cap():
    assert total_penalty([10000]) == 10000

def test_total_penalty_above_cap():
    assert total_penalty([6000, 5000]) == 10000

def test_total_penalty_negative_fine_raises():
    with pytest.raises(ValueError, match="negative fine"):
        total_penalty([100, -1, 50])
