import pytest

from aoc_2025.day1_math import handle_turns, turn


@pytest.mark.parametrize(
    ("curr", "n", "result"),
    [
        # no wrap
        (0, 50, 50),
        (23, 17, 40),
        (20, -10, 10),
        (10, -10, 0),
        (100, -5, 95),
        (1, 1, 2),
        (1, 0, 1),
        # wrap right
        (0, -1, 99),
        (0, -10, 90),
        (0, -30, 70),
        (50, -51, 99),
        # wrap left
        (99, 1, 0),
        (99, 10, 9),
        (99, 30, 29),
        (50, 51, 1),
        # actual case from AOC
        (50, -68, 82),
        (82, -30, 52),
        (52, 48, 0),
        (0, -5, 95),
        (95, 60, 55),
        (55, -55, 0),
        (0, -1, 99),
        (99, -99, 0),
        (0, 14, 14),
        (14, -82, 32),
    ],
)
def test_turn(curr, n, result):
    assert turn(curr, n) == result


def test_handle_turns():
    turns = [
        -68,
        -30,
        48,
        -5,
        60,
        -55,
        -1,
        -99,
        14,
        -82,
    ]  # dial is 3 times at 0

    part1 = handle_turns(turns)

    assert part1 == 3
