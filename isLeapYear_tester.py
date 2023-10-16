import pytest
from LeapYear_Function import isLeapYear


# 2000 mod 4 = 0, first check fullfilled
def test_year_divisible_by_4():
    year = 2000
    assert year % 4 == 0

# 2000 mod 100 != 0, second check not fullfilled
@pytest.mark.xfail
def test_year_divisible_by_100():
    year = 2000
    assert year % 100 != 0

#2000 mod 400 = 0, third check passes, therefore 2000 is
#a leap year
def test_year_divisible_with_400():
    year = 2000
    assert year % 400 == 0

#adding checks together with AND & OR.
def test_year_divisible_with_4_AND_not_100_OR_400():
    year = 2000
    assert (year % 4 == 0 and year % 100 != 0
            or year % 400 == 0)


#testing a couple of years.
@pytest.mark.parametrize("year, expected", [
    (2023, False),
    (2024, True),
    (2025, False),
    (2026, False),
    (2027, False),
    (2028, True),
    (2029, False),
    (2030, False),
])
def test_years_from_2023_2030(year, expected):
    assert isLeapYear(year) == expected
