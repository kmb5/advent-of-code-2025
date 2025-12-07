import textwrap
from collections.abc import Sequence


def is_valid_id(n: int) -> bool:
    num_str = str(n)
    split_idx = int(len(num_str) / 2)

    if len(num_str) % 2 != 0:
        return True

    first_half, second_half = num_str[:split_idx], num_str[split_idx:]

    if first_half == second_half:
        return False

    return True


def is_valid_id_part2(n: int) -> bool:
    str_n = str(n)

    for i in range(1, len(str_n) // 2 + 1):
        if len(str_n) % i != 0:
            continue

        groups = textwrap.wrap(str_n, i)
        if all(p == groups[0] for p in groups):
            return False

    return True


def find_invalid_ids(seq: Sequence[int], part: int = 1) -> list[int]:
    invalid_ids: list[int] = []
    is_valid_id_fn = is_valid_id if part == 1 else is_valid_id_part2

    for _id in seq:
        if not is_valid_id_fn(_id):
            invalid_ids.append(_id)

    return invalid_ids


def part1(inp: str) -> int:
    ranges = inp.split(",")
    total = 0
    for rng in ranges:
        start, stop = rng.split("-")
        start = int(start)
        stop = int(stop) + 1  # stop is exclusive

        invalid_ids = find_invalid_ids(range(start, stop))
        total += sum(invalid_ids)

    return total


def part2(inp: str) -> int:
    ranges = inp.split(",")
    total = 0
    for rng in ranges:
        start, stop = rng.split("-")
        start = int(start)
        stop = int(stop) + 1  # stop is exclusive

        invalid_ids = find_invalid_ids(range(start, stop), part=2)
        total += sum(invalid_ids)

    return total


def main():
    with open("inputs/day2.txt", "r", encoding="utf-8") as f:
        inp = f.read()

    part_1 = part1(inp)
    print(f"PART 1: {part_1}")

    part_2 = part2(inp)
    print(f"PART 2: {part_2}")


if __name__ == "__main__":
    main()
