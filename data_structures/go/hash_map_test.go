package ds

import (
	"testing"

	"gotest.tools/assert"
)

func TestHashMapSet(t *testing.T) {
	t.Log("Check that we can set some values.")
	hm := NewHashMap()
	hm.Set("A", 1)
	hm.Set("B", 2)
	hm.Set("C", 3)
	hm.Set("A", 9)

	assert.Equal(t, 3, hm.Size())
}

func TestHashMapGet(t *testing.T) {
	t.Log("Check that we can get some values.")
	hm := NewHashMap()

	hm.Set("A", 1)
	hm.Set("B", 2)
	hm.Set("C", 3)
	hm.Set("A", 4)
	hm.Set("D", 5)
	hm.Set("E", 6)
	hm.Set("F", 7)

	assert.Equal(t, 4, hm.Get("A"))
	assert.Equal(t, 7, hm.Get("F"))
	assert.Equal(t, 2, hm.Get("B"))
}

func TestHashMapResize(t *testing.T) {
	t.Log("Check that we can resize the map.")
	hm := NewHashMap()

	oldCapacity := hm.capacity

	hm.Set("A", 1)
	hm.Set("B", 2)
	hm.Set("C", 3)
	hm.Set("D", 4)
	hm.Set("E", 5)
	hm.Set("F", 6)
	hm.Set("G", 7)
	hm.Set("H", 8)
	hm.Set("I", 9)
	hm.Set("J", 15)
	hm.Set("K", 20)
	hm.Set("L", 100)

	hm.Display()

	assert.Assert(t, hm.capacity > oldCapacity)
}

func TestHashMapDisplay(t *testing.T) {
	t.Log("Check we can display things.")
	hm := NewHashMap()

	hm.Set("A", 1)
	hm.Set("B", 2)
	hm.Set("C", 3)
	hm.Set("A", 4)
	hm.Set("D", 5)
	hm.Set("E", 6)
	hm.Set("F", 7)

	hm.Display()
}
