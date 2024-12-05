import unittest

# Day X: 
# https://adventofcode.com/

# python3 -m unittest 

class Solution(unittest.TestCase):
    filename = "2024/day-.data"

    def part1(self) -> None:
        with open(self.filename, "r") as file:
            for line in file:
                print(line)
        print("result:")

    def part2(self) -> None:
        with open(self.filename, "r") as file:
            for line in file:
                print(line)

    def test(self) -> None:
        self.part1()
        self.part2()
