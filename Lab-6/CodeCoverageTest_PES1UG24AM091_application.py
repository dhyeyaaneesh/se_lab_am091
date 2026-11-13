import pytest
from traffic_fine import speeding_fine, license_action, total_penalty

@pytest.mark.parametrize("speed,limit,zone,expected", [
    (50, 60, "city", 0),
    (70, 60, "school", 2000),
    (90, 60, "school", 4000),
    (110, 60, "school", 6000),
    (70, 60, "highway", 1000),
    (90, 60, "highway", 2000),
    (110, 60, "highway", 3000),
    (70, 60, "city", 500),
    (90, 60, "city", 1000),
    (110, 60, "city", 1500),
])
def test_speeding_fine_scenarios(speed, limit, zone, expected):
    assert speeding_fine(speed, limit, zone) == expected

@pytest.mark.parametrize("points,commercial,repeat,expected", [
    (12, True, False, "revoke"),
    (12, False, False, "suspend"),
    (8, False, True, "suspend"),
    (8, False, False, "warning"),
    (4, False, False, "notice"),
    (3, False, False, "none"),
])
def test_license_action_scenarios(points, commercial, repeat, expected):
    assert license_action(points, commercial, repeat) == expected

@pytest.mark.parametrize("fines,expected", [
    ([], 0),
    ([100, 200, 300], 600),
    ([10000], 10000),
    ([6000, 5000], 10000),
])
def test_total_penalty_scenarios(fines, expected):
    assert total_penalty(fines) == expected

def test_total_penalty_rejects_negative_fine():
    with pytest.raises(ValueError, match="negative fine"):
        total_penalty([100, -1, 50])
