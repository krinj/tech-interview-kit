package ds

import (
	"testing"

	"gotest.tools/assert"
)

func TestStack(t *testing.T) {
	stack := Stack{}
	assert.Assert(t, stack.IsEmpty())

	stack.Push(5)
	stack.Push(2)
	stack.Push(19)
	stack.Push(48)

	assert.Assert(t, !stack.IsEmpty())

	assert.Equal(t, 4, stack.Size())
	assert.Equal(t, 48, stack.Peek())
	assert.Equal(t, 48, stack.Pop())
	assert.Equal(t, 19, stack.Pop())
	assert.Equal(t, 2, stack.Size())

	assert.Equal(t, 2, stack.Peek())
	assert.Equal(t, 2, stack.Pop())
	assert.Equal(t, 5, stack.Pop())

	assert.Assert(t, stack.IsEmpty())

}
