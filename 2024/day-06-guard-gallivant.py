import unittest
import sys
sys.setrecursionlimit(1_000_000)

# Day 6: Guard Gallivant
# https://adventofcode.com/2024/day/6

# python3 -m unittest 2024/day-06-guard-gallivant.py

class Solution(unittest.TestCase):
    filename = "2024/day-06-guard-gallivant.data"

    # Approach: Iterative
    def part1(self) -> None:
        with open(self.filename, "r") as file:
            grid = file.read().split("\n")
            ROWS, COLS = len(grid), len(grid[0])
            dirs = [[-1,0],[0,1],[1,0],[0,-1]] # UP, RIGHT, DOWN, LEFT
            row, col = -1, -1
            for r in range(ROWS):
                col = grid[r].find("^")
                if col >= 0:
                    row = r
                    break
            seen = set([(row, col)])
            dir = 0
            while True:
                nr = row + dirs[dir][0]
                nc = col + dirs[dir][1]
                if min(nr, nc) < 0 or nr == ROWS or nc == COLS:
                    break
                if grid[nr][nc] == '#':
                    dir = (dir+1) % 4
                    continue
                row, col = nr, nc
                seen.add((row, col))
            print("result:", len(seen))

    # Approach: Recursive
    def part1(self) -> None:
        with open(self.filename, "r") as file:
            grid = file.read().split("\n")
            ROWS, COLS = len(grid), len(grid[0])
            dirs = [[-1,0],[0,1],[1,0],[0,-1]] # UP, RIGHT, DOWN, LEFT
            seen = set()
            def traverse(row: int, col: int, dir: int) -> bool:
                if min(row, col) < 0 or row == ROWS or col == COLS:
                    return False
                if grid[row][col] == '#':
                    return True
                seen.add((row, col))
                nr = row + dirs[dir][0]
                nc = col + dirs[dir][1]
                if not traverse(nr, nc, dir):
                    return False
                dir = (dir+1) % 4
                return traverse(row, col, dir)
            for row in range(ROWS):
                col = grid[row].find("^")
                if col >= 0:
                    traverse(row, col, 0)
                    break
            print("result:", len(seen))

    def part2(self) -> None:
        with open(self.filename, "r") as file:
            grid = file.read().split("\n")
            ROWS, COLS = len(grid), len(grid[0])
            inbound = lambda r,c: min(r,c) >= 0 and r < ROWS and c < COLS
            dirs = [[-1,0],[0,1],[1,0],[0,-1]]
            result = 0
            def traverse(orow: int, ocol: int, row: int, col: int, dir: int) -> bool:
                nonlocal result
                if not inbound(row, col):
                    return False
                if grid[row][col] == '#' or (row,col) == (orow,ocol):
                    return True
                if (row, col, dir) in visited:
                    result += 1
                    return False
                visited.add((row, col, dir))
                nr = row + dirs[dir][0]
                nc = col + dirs[dir][1]
                if not traverse(orow, ocol, nr, nc, dir):
                    visited.remove((row, col, dir))
                    return False
                visited.remove((row, col, dir))
                dir = (dir+1) % 4
                return traverse(orow, ocol, row, col, dir)
            row, col = -1, -1
            for r in range(ROWS):
                col = grid[r].find("^")
                if col >= 0:
                    row = r
                    break
            dir = 0
            seen = set([(row, col)])
            visited = set([(row, col, dir)])
            while True:
                nr = row + dirs[dir][0]
                nc = col + dirs[dir][1]
                if not inbound(nr, nc):
                    break
                if grid[nr][nc] == '#':
                    dir = (dir+1) % 4
                    continue
                if (nr, nc) not in seen:
                    traverse(nr, nc, row, col, (dir+1)%4)
                seen.add((nr, nc))
                visited.add((nr, nc, dir))
                row, col = nr, nc
            print("result:", len(seen), result)

    def test(self) -> None:
        self.part1()
        self.part2()
