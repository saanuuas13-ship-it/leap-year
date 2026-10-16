from leap import is_leap_year

def test_leap_year():
    assert is_leap_year(2024) == "leap year"

def test_non_leap_year():
    assert is_leap_year(2023) == "not"

