from collections import defaultdict
import unittest

# Day 1: Historian Hysteria
# https://adventofcode.com/2024/day/1

# python3 -m unittest 2024/day-01-historian-hysteria.py

class Solution(unittest.TestCase):
    filename = "2024/day-01-historian-hysteria.data"

    def part1(self) -> None:
        list1 = []
        list2 = []
        with open(self.filename, "r") as file:
            for line in file:
                nums = line.split()
                list1.append(int(nums[0]))
                list2.append(int(nums[1]))
        list1.sort()
        list2.sort()
        total = 0
        for idx in range(len(list1)):
            distance = abs(list1[idx] - list2[idx])
            total += distance
        print("total distance:", total)

    def part2(self) -> None:
        list1 = []
        count2 = defaultdict(int)
        with open(self.filename, "r") as file:
            for line in file:
                nums = line.split()
                list1.append(int(nums[0]))
                count2[int(nums[1])] += 1
        score = 0
        for num in list1:
            similarity = num * count2[num]
            score += similarity
        print("similarity score:", score)

    def test(self) -> None:
        self.part1()
        self.part2()
