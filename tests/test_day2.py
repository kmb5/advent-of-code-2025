from collections.abc import Sequence

import pytest

from aoc_2025.day2 import (
    find_invalid_ids,
    is_valid_id,
    is_valid_id_part2,
    part1,
    part2,
)

TEST_INPUT = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"


@pytest.mark.parametrize(
    ("_id", "is_valid"),
    [
        (11, False),
        (22, False),
        (12, True),
    ],
)
def test_is_valid_id(_id: int, is_valid: bool):
    assert is_valid_id(_id) == is_valid


@pytest.mark.parametrize(
    ("_id", "is_valid"),
    [
        (12341234, False),
        (123123123, False),
        (1212121212, False),
        (1111111, False),
    ],
)
def test_is_valid_id_part2(_id: int, is_valid: bool):
    assert is_valid_id_part2(_id) == is_valid


@pytest.mark.parametrize(
    ("seq", "invalid_ids"),
    [
        (range(11, 23), [11, 22]),
        (range(95, 116), [99]),
        (range(998, 1013), [1010]),
        (range(1188511880, 1188511891), [1188511885]),
    ],
)
def test_find_invalid_ids(seq: Sequence[int], invalid_ids: bool):
    assert find_invalid_ids(seq) == invalid_ids


@pytest.mark.parametrize(
    ("seq", "invalid_ids"),
    [
        (range(11, 23), [11, 22]),
        (range(95, 116), [99, 111]),
        (range(998, 1013), [999, 1010]),
        (range(1188511880, 1188511891), [1188511885]),
    ],
)
def test_find_invalid_ids_day2(seq: Sequence[int], invalid_ids: bool):
    assert find_invalid_ids(seq, part=2) == invalid_ids


def test_real_input_p1():
    assert part1(TEST_INPUT) == 1227775554


def test_real_input_p2():
    assert part2(TEST_INPUT) == 4174379265
