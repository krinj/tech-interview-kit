package ds

type StackNode struct {
	val  interface{}
	next *StackNode
}

type Stack struct {
	size int
	tail *StackNode
}

func (s *Stack) Push(x interface{}) {
	node := StackNode{val: x}
	if s.tail != nil {
		node.next = s.tail
	}
	s.tail = &node
	s.size++
}

func (s *Stack) Pop() interface{} {
	if s.tail != nil {
		val := s.tail.val
		s.tail = s.tail.next
		s.size--
		return val
	} else {
		return nil
	}
}

func (s *Stack) Peek() interface{} {
	if s.tail != nil {
		return s.tail.val
	} else {
		return nil
	}
}

func (s *Stack) IsEmpty() bool {
	return s.Size() == 0
}

func (s *Stack) Size() int {
	return s.size
}
