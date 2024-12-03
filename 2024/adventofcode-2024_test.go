package adventofcode

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

// go test -v -count=1 ./2024/ -run ^TestAdventofcode$
func TestAdventofcode(t *testing.T) {
	// assert.NoError(t, Day01Part1())
	// assert.NoError(t, Day01Part2())
	// assert.NoError(t, Day02Part1())
	// assert.NoError(t, Day02Part2())
	// assert.NoError(t, Day03Part1())
	assert.NoError(t, Day03Part2())
}
