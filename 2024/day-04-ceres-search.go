package adventofcode

import (
	"bufio"
	"errors"
	"fmt"
	"os"
)

// Day 4: Ceres Search
// https://adventofcode.com/2024/day/4

func Day04Part1() error {
	filename := "day-04-ceres-search.data"
	file, err := os.OpenFile(filename, os.O_RDONLY, 0644)
	if err != nil {
		return errors.New("os.OpenFile ERROR: " + err.Error())
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)
	var grid = make([][]byte, 0)
	for scanner.Scan() {
		grid = append(grid, []byte(scanner.Text()))
	}
	const (
		UP = 1 << iota
		DOWN
		LEFT
		RIGHT
		LEFT_UP
		RIGHT_UP
		LEFT_DOWN
		RIGHT_DOWN
	)
	var letters = [4]byte{'X', 'M', 'A', 'S'}
	var m, n = len(grid), len(grid[0])
	var dfs func(row int, col int, idx int, dir int) int
	dfs = func(row int, col int, idx int, dir int) int {
		if min(row, col) < 0 || row == m || col == n || grid[row][col] != letters[idx] {
			return 0
		}
		if idx == 3 && grid[row][col] == 'S' {
			return 1
		}
		var count = 0
		if dir&UP == UP {
			count += dfs(row-1, col, idx+1, UP)
		}
		if dir&DOWN == DOWN {
			count += dfs(row+1, col, idx+1, DOWN)
		}
		if dir&LEFT == LEFT {
			count += dfs(row, col-1, idx+1, LEFT)
		}
		if dir&RIGHT == RIGHT {
			count += dfs(row, col+1, idx+1, RIGHT)
		}
		if dir&LEFT_UP == LEFT_UP {
			count += dfs(row-1, col-1, idx+1, LEFT_UP)
		}
		if dir&RIGHT_UP == RIGHT_UP {
			count += dfs(row-1, col+1, idx+1, RIGHT_UP)
		}
		if dir&LEFT_DOWN == LEFT_DOWN {
			count += dfs(row+1, col-1, idx+1, LEFT_DOWN)
		}
		if dir&RIGHT_DOWN == RIGHT_DOWN {
			count += dfs(row+1, col+1, idx+1, RIGHT_DOWN)
		}
		return count
	}
	var count = 0
	for row := 0; row < m; row++ {
		for col := 0; col < n; col++ {
			if grid[row][col] == 'X' {
				count += dfs(row, col, 0, 255) // dec(255)=bin(11111111)
			}
		}
	}
	fmt.Println("count:", count)
	return nil
}

func Day04Part2() error {
	filename := "day-04-ceres-search.data"
	file, err := os.OpenFile(filename, os.O_RDONLY, 0644)
	if err != nil {
		return errors.New("os.OpenFile ERROR: " + err.Error())
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)
	var grid = make([][]byte, 0)
	for scanner.Scan() {
		grid = append(grid, []byte(scanner.Text()))
	}
	var m, n = len(grid), len(grid[0])
	var count = 0
	for row := 1; row < m-1; row++ {
		for col := 1; col < n-1; col++ {
			if grid[row][col] == 'A' {
				// ["MM", "SS"]
				if grid[row-1][col-1] == 'M' && grid[row-1][col+1] == 'M' &&
					grid[row+1][col-1] == 'S' && grid[row+1][col+1] == 'S' {
					count++
				}
				// ["MS", "MS"]
				if grid[row-1][col-1] == 'M' && grid[row-1][col+1] == 'S' &&
					grid[row+1][col-1] == 'M' && grid[row+1][col+1] == 'S' {
					count++
				}
				// ["SM", "SM"]
				if grid[row-1][col-1] == 'S' && grid[row-1][col+1] == 'M' &&
					grid[row+1][col-1] == 'S' && grid[row+1][col+1] == 'M' {
					count++
				}
				// ["SS", "MM"]
				if grid[row-1][col-1] == 'S' && grid[row-1][col+1] == 'S' &&
					grid[row+1][col-1] == 'M' && grid[row+1][col+1] == 'M' {
					count++
				}
			}
		}
	}
	fmt.Println("count:", count)
	return nil
}
