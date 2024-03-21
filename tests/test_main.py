# -- -- -- -- -- -- -- -- -- --
from main.bowling import bowling_point_calculator

def test_null():
    assert bowling_point_calculator("-- "*10) == 0

def test_assert_one_nonzero_throw():
    assert bowling_point_calculator("1- "+"-- "*9) == 1

def test_multiple_nonzero_firstplace():
    assert bowling_point_calculator("2- 4- -- 2- "+"-- "*6) == 8

def test_multiple_nonzero_secondplace():
    assert bowling_point_calculator("-2 -- -5 -9 "+"-- "*6) == 16

def test_multiple_nonzero():
    assert bowling_point_calculator("-2 12 -5 -9 "+"-- "*6) == 19

def test_spare():
    assert bowling_point_calculator("5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5-") == 140

def test_strike_followedby_openframe():
    assert bowling_point_calculator("X 13 ") == 18
# Format
# -    : miss
# [1-9]: number of pins nocked down
# \    : Spare
# X    : strike
