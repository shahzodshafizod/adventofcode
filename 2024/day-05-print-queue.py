from functools import cmp_to_key
from collections import defaultdict
import unittest

# Day 5: Print Queue
# https://adventofcode.com/2024/day/5

# python3 -m unittest 2024/day-05-print-queue.py

class Solution(unittest.TestCase):
    filename = "2024/day-05-print-queue.data"

    def part1(self) -> None:
        result = 0
        with open(self.filename, "r") as file:
            edges, queries = file.read().strip().split("\n\n")
            prev = defaultdict(set)
            for line in edges.split("\n"):
                src, dst = map(int, line.split("|"))
                prev[dst].add(src)
            for line in queries.split("\n"):
                nums = list(map(int, line.split(",")))
                n = len(nums)
                ok = True
                for i in range(n):
                    for j in range(i+1, n):
                        if nums[j] in prev[nums[i]]:
                            ok = False
                            break
                if ok:
                    result += nums[n//2]
        print("result:", result)

    def part2(self) -> None:
        result = 0
        with open(self.filename, "r") as file:
            edges, queries = file.read().strip().split("\n\n")
            prev = defaultdict(set)
            for line in edges.split("\n"):
                src, dst = map(int, line.split("|"))
                prev[dst].add(src)
            def compare(a: int, b: int) -> int:
                if a in prev[b]: return -1
                if b in prev[a]: return 1
                return 0
            for line in queries.split("\n"):
                nums = list(map(int, line.split(",")))
                n = len(nums)
                ok = True
                for i in range(n):
                    for j in range(i+1, n):
                        if nums[j] in prev[nums[i]]:
                            ok = False
                            break
                if not ok:
                    nums.sort(key=cmp_to_key(compare))
                    result += nums[n//2]
        print("result:", result)

    def test(self) -> None:
        self.part1()
        self.part2()
