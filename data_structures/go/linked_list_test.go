package ds

import (
	"testing"

	"gotest.tools/assert"
)

func TestLinkedListAdd(t *testing.T) {
	t.Log("Testing that we can create LinkedLists and add values to it.")
	ll := LinkedList{}
	assert.Equal(t, 0, ll.Size())

	ll.AddHead(1)
	ll.AddHead(2)
	ll.AddHead(3)

	assert.Equal(t, 3, ll.Size())

	ll.AddTail(4)
	ll.AddTail(5)
	ll.AddTail(6)

	assert.Equal(t, 6, ll.Size())
}

func TestLinkedListPop(t *testing.T) {
	t.Log("Testing that popping values from the list gives what we expect.")
	ll := LinkedList{}

	ll.AddTail(4)
	ll.AddTail(5)
	ll.AddTail(6)

	assert.Equal(t, 4, ll.PopHead())
	assert.Equal(t, 6, ll.PopTail())
	assert.Equal(t, 5, ll.PopTail())
	assert.Equal(t, 0, ll.Size())
}

func TestLinkedListPeek(t *testing.T) {
	ll := LinkedList{}

	ll.AddHead(9)
	assert.Equal(t, 9, ll.PeekHead())
	assert.Equal(t, 9, ll.PeekTail())

	ll.AddTail(5)
	assert.Equal(t, 9, ll.PeekHead())
	assert.Equal(t, 5, ll.PeekTail())
	assert.Equal(t, 2, ll.Size())
}

func TestLinkedListDisplay(t *testing.T) {

	t.Log("Testing that we can create LinkedLists and add values to it.")
	ll := LinkedList{}

	ll.AddHead(1)
	ll.AddHead(3)
	ll.AddHead(5)
	ll.AddTail(2)
	ll.AddTail(4)
	ll.AddTail(6)
	ll.Display()

}
