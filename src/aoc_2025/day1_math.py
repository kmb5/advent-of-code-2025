# math-version of day1 with modulo
DIAL_SIZE = 100
START_POS = 50


def turn(curr: int, n: int) -> int:
    new_pos = (curr + n) % DIAL_SIZE

    return new_pos


def handle_turns(turns: list[int]) -> int:
    pos = START_POS

    num_0_pos = 0

    for t in turns:
        pos = turn(pos, t)

        if pos == 0:
            num_0_pos += 1

    return num_0_pos


def parse_input(inp: str) -> list[int]:
    parsed = []

    for row in inp.splitlines():
        direction, num = row[0], row[1:]

        if direction == "L":
            parsed.append(-int(num))
        else:
            parsed.append(int(num))

    return parsed


def main():
    with open("inputs/day1.txt", "r", encoding="utf-8") as f:
        inp = f.read()

    parsed = parse_input(inp)
    part_1 = handle_turns(parsed)

    print(f"PART 1: {part_1}")


if __name__ == "__main__":
    main()
