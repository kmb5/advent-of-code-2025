# OOP version of day 1 with every dial rotation 'simulated'


class Dial:
    def __init__(self, start_pos: int = 50):
        self.pos = start_pos
        self.num_0 = 0

    def rotate_left(self, n: int):
        for x in range(n):
            self.pos -= 1
            if self.pos == -1:
                self.pos = 99

            # for part 2 we need to count all the times the dial hits 0
            if self.pos == 0:
                self.num_0 += 1

    def rotate_right(self, n: int):
        for x in range(n):
            self.pos += 1
            if self.pos == 100:
                self.pos = 0

            # for part 2 we need to count all the times the dial hits 0
            if self.pos == 0:
                self.num_0 += 1

    def rotate(self, direction: str, n: int):
        if direction == "L":
            self.rotate_left(n)
        elif direction == "R":
            self.rotate_right(n)


def part1(inp):
    dial = Dial()
    password = 0

    for row in inp:
        direction, amount = row[0], row[1:]
        amount = int(amount)
        dial.rotate(direction, amount)
        if dial.pos == 0:
            password += 1

    print(f"Password is: {password}")


def part2(inp):
    dial = Dial()
    for row in inp:
        direction, amount = row[0], row[1:]
        amount = int(amount)
        dial.rotate(direction, amount)

    print(f"Password is: {dial.num_0}")


def main():
    with open("./inputs/day1.txt", "r", encoding="utf-8") as file:
        data = file.read().splitlines()

    part1(data)
    part2(data)


if __name__ == "__main__":
    main()
