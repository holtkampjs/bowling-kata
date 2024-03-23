# -- -- -- -- -- -- -- -- -- --
from main.bowling import bowling_point_calculator


def test_null():
    assert bowling_point_calculator("-- " * 10) == 0


def test_assert_one_nonzero_throw():
    assert bowling_point_calculator("1- " + "-- " * 9) == 1


def test_multiple_nonzero_firstplace():
    assert bowling_point_calculator("2- 4- -- 2- " + "-- " * 6) == 8


def test_multiple_nonzero_secondplace():
    assert bowling_point_calculator("-2 -- -5 -9 " + "-- " * 6) == 16


def test_multiple_nonzero():
    assert bowling_point_calculator("-2 12 -5 -9 " + "-- " * 6) == 19


def test_spare():
    assert bowling_point_calculator("5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5-") == 140


def test_strike_followedby_openframe():
    assert bowling_point_calculator("X 13 " + "-- " * 8) == 18


def test_strike_followedby_strike():
    assert bowling_point_calculator("X X 24 " + "-- " * 7) == 44


def test_tenthframe_spare():
    assert bowling_point_calculator("5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/5") == 150


def test_perfect_game():
    assert bowling_point_calculator("X X X X X X X X X X X X") == 300


def test_tenthframe_strike_spare():
    assert bowling_point_calculator("-- " * 9 + "X 5/") == 20


def test_tenthframe_spare_strike():
    # two potential ways of writing this
    one_way = bowling_point_calculator("-- " * 9 + "5/ X")
    another_way = bowling_point_calculator("-- " * 9 + "5/X")
    assert one_way == another_way == 20


# Format
# -    : miss
# [1-9]: number of pins nocked down
# \    : Spare
# X    : strike
