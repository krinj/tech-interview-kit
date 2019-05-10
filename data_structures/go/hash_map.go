package ds

import (
	"fmt"
	"hash/fnv"
)

type HashNode struct {
	key      string
	val      interface{}
	next     *HashNode
	occupied bool
}

type HashMap struct {
	storage  []*HashNode
	size     int
	capacity int
	limit    int
}

func NewHashMap() HashMap {
	hashMap := HashMap{
		storage:  make([]*HashNode, 0),
		size:     0,
		capacity: 0,
		limit:    0,
	}
	hashMap.resize(8)
	return hashMap
}

func getHashIndex(key string, capacity int) int {
	algorithm := fnv.New32a()
	algorithm.Write([]byte(key))
	return int(algorithm.Sum32()) % capacity
}

func (hm *HashMap) Set(key string, value interface{}) {

	hm.size += setInternal(key, value, hm.capacity, hm.storage)
	if hm.size >= hm.limit {
		hm.resize(hm.capacity * 2)
	}
}

func setInternal(key string, value interface{}, capacity int, nodes []*HashNode) int {
	index := getHashIndex(key, capacity)
	node := nodes[index]

	for node.occupied && node.key != key {
		node = node.next
	}

	node.key = key
	node.val = value

	if !node.occupied {
		newNode := HashNode{occupied: false}
		node.next = &newNode
		node.occupied = true
		return 1
	}

	return 0
}

func (hm *HashMap) Get(key string) interface{} {
	index := getHashIndex(key, hm.capacity)
	node := hm.storage[index]

	for node.occupied && node.key != key {
		node = node.next
	}

	if !node.occupied {
		panic("Key not found!")
	} else {
		return node.val
	}
}

func (hm *HashMap) Display() {

	for i := 0; i < hm.capacity; i++ {
		node := hm.storage[i]
		fmt.Printf("%03v: [", i)
		for node.occupied {
			fmt.Printf("%v (%v)", node.key, node.val)
			node = node.next
			if node.occupied {
				fmt.Printf(" -> ")
			}
		}
		fmt.Printf("]\n")
	}
	fmt.Printf("\nSize: %v\n", hm.size)
	fmt.Printf("Capacity: %v\n", hm.capacity)
	fmt.Printf("Limit: %v\n", hm.limit)
}

func (hm *HashMap) Size() int {
	return hm.size
}

func (hm *HashMap) resize(newSize int) {
	// Create the new slice.
	newStorage := make([]*HashNode, newSize)
	for i := 0; i < newSize; i++ {
		node := HashNode{occupied: false}
		newStorage[i] = &node
	}

	// Transfer the data.
	for i := 0; i < hm.capacity; i++ {
		node := hm.storage[i]
		for node.occupied {
			setInternal(node.key, node.val, newSize, newStorage)
			node = node.next
		}
	}

	// Set the references.
	hm.capacity = newSize
	hm.limit = hm.capacity
	hm.storage = newStorage
}
