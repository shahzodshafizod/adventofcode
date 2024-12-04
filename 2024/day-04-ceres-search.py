import unittest

# Day 4: Ceres Search
# https://adventofcode.com/2024/day/4

# python3 -m unittest 2024/day-04-ceres-search.py

class Solution(unittest.TestCase):
    filename = "2024/day-04-ceres-search.data"

    def part1(self) -> None:
        with open(self.filename, "r") as file:
            letters = ['X', 'M', 'A', 'S']
            grid = [list(line.removesuffix("\n")) for line in file.readlines()]
            m, n = len(grid), len(grid[0])
            UP, DOWN, LEFT, RIGHT = 1, 2, 4, 8
            UP_LEFT, UP_RIGHT, DOWN_LEFT, DOWN_RIGHT = 16, 32, 64, 128
            def dfs(row: int, col: int, idx: int, dir: int) -> int:
                if min(row, col) < 0 or row == m or col == n or grid[row][col] != letters[idx]:
                    return 0
                if idx == 3 and grid[row][col] == 'S':
                    return 1
                count = 0
                if dir&UP == UP:
                    count += dfs(row-1, col, idx+1, UP)
                if dir&DOWN == DOWN:
                    count += dfs(row+1, col, idx+1, DOWN)
                if dir&LEFT == LEFT:
                    count += dfs(row, col-1, idx+1, LEFT)
                if dir&RIGHT == RIGHT:
                    count += dfs(row, col+1, idx+1, RIGHT)
                if dir&UP_LEFT == UP_LEFT:
                    count += dfs(row-1, col-1, idx+1, UP_LEFT)
                if dir&UP_RIGHT == UP_RIGHT:
                    count += dfs(row-1, col+1, idx+1, UP_RIGHT)
                if dir&DOWN_LEFT == DOWN_LEFT:
                    count += dfs(row+1, col-1, idx+1, DOWN_LEFT)
                if dir&DOWN_RIGHT == DOWN_RIGHT:
                    count += dfs(row+1, col+1, idx+1, DOWN_RIGHT)
                return count
            count = 0
            for row in range(m):
                for col in range(n):
                    if grid[row][col] == 'X':
                        count += dfs(row, col, 0, 255)
            print("count:", count)

    def part2(self) -> None:
        with open(self.filename, "r") as file:
            grid = [list(line.removesuffix("\n")) for line in file.readlines()]
            m, n = len(grid), len(grid[0])
            count = 0
            for row in range(1, m-1):
                for col in range(1, n-1):
                    if grid[row][col] == 'A':
                        # [MM, SS]
                        if (grid[row-1][col-1] == 'M' and grid[row-1][col+1] == 'M' and
                            grid[row+1][col-1] == 'S' and grid[row+1][col+1] == 'S'):
                            count += 1
                        # [MS, MS]
                        if (grid[row-1][col-1] == 'M' and grid[row-1][col+1] == 'S' and
                            grid[row+1][col-1] == 'M' and grid[row+1][col+1] == 'S'):
                            count += 1
                        # [SM, SM]
                        if (grid[row-1][col-1] == 'S' and grid[row-1][col+1] == 'M' and
                            grid[row+1][col-1] == 'S' and grid[row+1][col+1] == 'M'):
                            count += 1
                        # [SS, MM]
                        if (grid[row-1][col-1] == 'S' and grid[row-1][col+1] == 'S' and
                            grid[row+1][col-1] == 'M' and grid[row+1][col+1] == 'M'):
                            count += 1
            print("count:", count)

    def test(self) -> None:
        self.part1()
        self.part2()
