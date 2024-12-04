from typing import List
import unittest

# Day 2: Red-Nosed Reports
# https://adventofcode.com/2024/day/2

# python3 -m unittest 2024/day-02-red-nosed-reports.py

class Solution(unittest.TestCase):
    filename = "2024/day-02-red-nosed-reports.data"

    def part1(self) -> None:
        with open(self.filename, "r") as file:
            reports = 0
            for line in file:
                nums = list(map(int, line.split()))
                inc, dec = True, True
                for idx in range(1, len(nums)):
                    diff = nums[idx] - nums[idx-1]
                    if abs(diff) > 3:
                        inc = dec = False
                        break
                    inc = inc and diff > 0
                    dec = dec and diff < 0
                    if not inc and not dec:
                        break
                if inc or dec:
                    reports += 1
            print("safe reports:", reports)

    def part2(self) -> None:
        with open(self.filename, "r") as file:
            reports = 0
            for line in file:
                nums = list(map(int, line.split()))
                for mid in range(-1, len(nums)):
                    copy = nums[:mid] + nums[mid+1:]
                    inc, dec = True, True
                    for idx in range(1, len(copy)):
                        diff = copy[idx] - copy[idx-1]
                        if abs(diff) > 3:
                            inc = dec = False
                            break
                        inc = inc and diff > 0
                        dec = dec and diff < 0
                        if not inc and not dec:
                            break
                    if inc or dec:
                        reports += 1
                        break
            print("safe reports:", reports)

    def test(self) -> None:
        self.part1()
        self.part2()
