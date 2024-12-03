package adventofcode

import (
	"bufio"
	"errors"
	"fmt"
	"os"
	"regexp"
)

// Day 3: Mull It Over
// https://adventofcode.com/2024/day/3

func Day03Part1() error {
	filename := "day-03-mull-it-over.data"
	file, err := os.OpenFile(filename, os.O_RDONLY, 0644)
	if err != nil {
		return errors.New("os.OpenFile ERROR: " + err.Error())
	}
	defer file.Close()
	pattern := `mul\(\d{1,3},\d{1,3}\)`
	reg, err := regexp.Compile(pattern)
	if err != nil {
		return errors.New("regexp.Compile ERROR: " + err.Error())
	}
	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)
	var result = 0
	for scanner.Scan() {
		var first, second int
		for _, mul := range reg.FindAllString(scanner.Text(), -1) {
			fmt.Sscanf(mul, "mul(%d,%d)", &first, &second)
			result += first * second
		}
	}
	fmt.Println("results of the multiplications:", result)
	return nil
}

func Day03Part2() error {
	filename := "day-03-mull-it-over.data"
	file, err := os.OpenFile(filename, os.O_RDONLY, 0644)
	if err != nil {
		return errors.New("os.OpenFile ERROR: " + err.Error())
	}
	defer file.Close()
	pattern := `mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)`
	reg, err := regexp.Compile(pattern)
	if err != nil {
		return errors.New("regexp.Compile(pattern) ERROR: " + err.Error())
	}
	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)
	var result = 0
	var first, second int
	var enabled = true
	for scanner.Scan() {
		for _, oper := range reg.FindAllString(scanner.Text(), -1) {
			if oper == "don't()" {
				enabled = false
			} else if oper == "do()" {
				enabled = true
			} else if enabled {
				fmt.Sscanf(oper, "mul(%d,%d)", &first, &second)
				result += first * second
			}
		}
	}
	fmt.Println("results of the multiplications:", result)
	return nil
}
