package adventofcode

import (
	"bufio"
	"errors"
	"fmt"
	"os"
	"sort"
)

// Day 1: Historian Hysteria
// https://adventofcode.com/2024/day/1

func Day01Part1() error {
	filename := "day-01-historian-hysteria.data"
	file, err := os.OpenFile(filename, os.O_RDONLY, 0644)
	if err != nil {
		return errors.New("os.OpenFile ERROR: " + err.Error())
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)
	var first, second int
	var list1 = make([]int, 0)
	var list2 = make([]int, 0)
	for scanner.Scan() {
		_, err := fmt.Sscanf(scanner.Text(), "%d   %d", &first, &second)
		if err != nil {
			return errors.New("fmt.Sscanf ERROR: " + err.Error())
		}
		list1 = append(list1, first)
		list2 = append(list2, second)
	}
	sort.Ints(list1)
	sort.Ints(list2)
	var abs = func(n int) int {
		if n < 0 {
			return -n
		}
		return n
	}
	var total, distance = 0, 0
	for idx := range list1 {
		distance = abs(list1[idx] - list2[idx])
		total += distance
	}
	fmt.Println("total distance:", total)
	return nil
}

func Day01Part2() error {
	filename := "day-01-historian-hysteria.data"
	file, err := os.OpenFile(filename, os.O_RDONLY, 0644)
	if err != nil {
		return errors.New("os.OpenFile ERROR: " + err.Error())
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)
	var first, second int
	var list1 = make([]int, 0)
	var freq2 = make(map[int]int)
	for scanner.Scan() {
		_, err := fmt.Sscanf(scanner.Text(), "%d   %d", &first, &second)
		if err != nil {
			return errors.New("fmt.Sscanf ERROR: " + err.Error())
		}
		list1 = append(list1, first)
		freq2[second]++
	}
	var score, similarity = 0, 0
	for _, num := range list1 {
		similarity = num * freq2[num]
		score += similarity
	}
	fmt.Println("similarity score:", score)
	return nil
}
