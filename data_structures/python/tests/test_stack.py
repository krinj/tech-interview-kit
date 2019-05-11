import unittest
from data_structures.python.linked_list import LinkedList
from data_structures.python.stack import Stack


class TestLinkedList(unittest.TestCase):

    def test_stack(self):
        stack = Stack()

        self.assertTrue(stack.is_empty())

        stack.push(5)
        stack.push(3)
        stack.push(4)
        stack.push(10)

        self.assertEqual(4, stack.size())
        self.assertFalse(stack.is_empty())

        self.assertEqual(10, stack.peek())
        self.assertEqual(10, stack.pop())
        self.assertEqual(4, stack.pop())
        self.assertEqual(2, stack.size())
        self.assertEqual(3, stack.peek())
        self.assertEqual(3, stack.pop())
        self.assertEqual(5, stack.pop())

        self.assertTrue(stack.is_empty())


