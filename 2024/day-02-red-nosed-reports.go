package adventofcode

import (
	"bufio"
	"errors"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

// Day 2: Red-Nosed Reports
// https://adventofcode.com/2024/day/2

func Day02Part1() error {
	filename := "day-02-red-nosed-reports.data"
	file, err := os.OpenFile(filename, os.O_RDONLY, 0644)
	if err != nil {
		return errors.New("os.OpenFile ERROR: " + err.Error())
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)
	var reports = 0
	var n, diff int
	var inc, dec bool
	for scanner.Scan() {
		strs := strings.Split(scanner.Text(), " ")
		n = len(strs)
		var nums = make([]int, 0, n)
		for _, s := range strs {
			num, _ := strconv.Atoi(s)
			nums = append(nums, num)
		}
		inc, dec = true, true
		for idx := 1; idx < n && (inc || dec); idx++ {
			diff = nums[idx] - nums[idx-1]
			if math.Abs(float64(diff)) > 3 {
				inc, dec = false, false
				break
			}
			inc = inc && diff > 0
			dec = dec && diff < 0
		}
		if inc || dec {
			reports++
		}
	}
	fmt.Println("safe reports:", reports)
	return nil
}

func Day02Part2() error {
	filename := "day-02-red-nosed-reports.data"
	file, err := os.OpenFile(filename, os.O_RDONLY, 0644)
	if err != nil {
		return errors.New("os.OpenFile ERROR: " + err.Error())
	}
	defer file.Close()
	// safe: 1-increasing, 2-decreasing
	var isSafe func(nums []int, idx int, safe int) bool
	isSafe = func(nums []int, idx int, safe int) bool {
		if safe == 0 {
			return false
		}
		if idx == len(nums) {
			return true
		}
		if math.Abs(float64(nums[idx]-nums[idx-1])) > 3 {
			return false
		}
		if safe&1 == 1 && nums[idx-1] >= nums[idx] {
			safe ^= 1
		}
		if safe&2 == 2 && nums[idx-1] <= nums[idx] {
			safe ^= 2
		}
		return isSafe(nums, idx+1, safe)
	}
	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)
	var reports = 0
	for scanner.Scan() {
		strs := strings.Split(scanner.Text(), " ")
		var n = len(strs)
		var nums = make([]int, 0, n)
		for _, s := range strs {
			num, _ := strconv.Atoi(s)
			nums = append(nums, num)
		}
		// if isSafe(nums, 1, 3) {
		// 	reports++
		// 	continue
		// }
		var erased = make([]int, n)
		for mid := range nums {
			copy(erased[:mid], nums[:mid])
			copy(erased[mid:], nums[mid+1:])
			if isSafe(erased[:n-1], 1, 3) {
				reports++
				break
			}
		}
	}
	fmt.Println("safe reports:", reports)
	return nil
}
