import re
import unittest

# Day 3: Mull It Over
# https://adventofcode.com/2024/day/3

# python3 -m unittest 2024/day-03-mull-it-over.py

class Solution(unittest.TestCase):
    filename = "2024/day-03-mull-it-over.data"

    def part1(self) -> None:
        with open(self.filename, "r") as file:
            result = 0
            pattern = re.compile("mul\\(\\d{1,3},\\d{1,3}\\)")
            numreg = re.compile("\\d{1,3}")
            for line in file:
                for oper in pattern.findall(line):
                    nums = list(map(int, numreg.findall(oper)))
                    result += nums[0] * nums[1]
            print("results of the multiplications:", result)

    def part2(self) -> None:
        with open(self.filename, "r") as file:
            result = 0
            pattern = re.compile("mul\\(\\d{1,3},\\d{1,3}\\)|do\\(\\)|don't\\(\\)")
            numreg = re.compile("\\d{1,3}")
            enabled = True
            for line in file:
                for oper in pattern.findall(line):
                    if oper == "do()":
                        enabled = True
                    elif oper == "don't()":
                        enabled = False
                    elif oper.index("mul") == 0 and enabled:
                        nums = list(map(int, numreg.findall(oper)))
                        result += nums[0] * nums[1]
            print("results of the multiplications:", result)

    def test(self) -> None:
        # self.part1()
        self.part2()
