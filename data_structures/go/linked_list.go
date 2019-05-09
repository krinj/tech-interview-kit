package ds

import "fmt"

type LLNode struct {
	Next *LLNode
	Prev *LLNode
	Val  interface{}
}

type LinkedList struct {
	Head *LLNode
	Tail *LLNode
	size int
}

func (ll *LinkedList) AddHead(x interface{}) {
	// Wrap the data in a node and add to head.
	node := LLNode{Val: x}
	if ll.size == 0 {
		ll.addFirstNode(&node)
	} else {
		node.Next = ll.Head
		ll.Head.Prev = &node
		ll.Head = &node
	}
	ll.size++
}

func (ll *LinkedList) AddTail(x interface{}) {
	node := LLNode{Val: x}
	if ll.size == 0 {
		ll.addFirstNode(&node)
	} else {
		node.Prev = ll.Tail
		ll.Tail.Next = &node
		ll.Tail = &node
	}
	ll.size++
}

func (ll *LinkedList) addFirstNode(n *LLNode) {
	ll.Head = n
	ll.Tail = n
}

func (ll *LinkedList) removeLastNode() interface{} {
	x := ll.Head.Val
	ll.Head.Next = nil
	ll.Head.Prev = nil
	ll.Head = nil
	ll.Tail = nil
	return x
}

func (ll *LinkedList) PopHead() interface{} {
	ll.size--

	if ll.size == 0 {
		return ll.removeLastNode()
	}

	x := ll.Head.Val
	oldNode := ll.Head
	oldNode.Next.Prev = nil
	ll.Head = oldNode.Next
	oldNode.Next = nil

	return x
}

func (ll *LinkedList) PopTail() interface{} {
	ll.size--

	if ll.size == 0 {
		return ll.removeLastNode()
	}

	x := ll.Tail.Val
	oldNode := ll.Tail
	oldNode.Prev.Next = nil
	ll.Tail = oldNode.Prev
	oldNode.Prev = nil

	return x
}

func (ll *LinkedList) PeekHead() interface{} {
	return ll.Head.Val
}

func (ll *LinkedList) PeekTail() interface{} {
	return ll.Tail.Val
}

func (ll *LinkedList) Size() interface{} {
	return ll.size
}

func (ll *LinkedList) IsEmpty() bool {
	return ll.Size() == 0
}

func (ll *LinkedList) Display() {
	fmt.Printf("[")
	node := ll.Head
	for node != nil {
		fmt.Printf("%v", node.Val)
		if node.Next != nil {
			fmt.Printf(" -> ")
		}
		node = node.Next
	}
	fmt.Printf("]\n")
}
