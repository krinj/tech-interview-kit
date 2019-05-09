import unittest
from data_structures.python.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.linked_list = LinkedList()

    def test_insert(self):
        # Check if we can insert items into the list.
        self.linked_list.add_head(5)
        self.assertEqual(1, self.linked_list.size())
        self.linked_list.add_head(3)
        self.assertEqual(2, self.linked_list.size())
        self.linked_list.add_tail(2)
        self.assertEqual(3, self.linked_list.size())

    def test_peek(self):
        self.linked_list.add_tail(3)
        self.assertEqual(3, self.linked_list.peek_head())
        self.assertEqual(3, self.linked_list.peek_tail())

        self.linked_list.add_head(9)
        self.assertEqual(9, self.linked_list.peek_head())
        self.assertEqual(3, self.linked_list.peek_tail())

        self.linked_list.add_tail(12)
        self.assertEqual(9, self.linked_list.peek_head())
        self.assertEqual(12, self.linked_list.peek_tail())

    def test_pop(self):
        self.linked_list.add_tail(2)
        self.linked_list.add_tail(4)
        self.linked_list.add_tail(6)
        self.linked_list.add_tail(8)
        self.assertEqual(2, self.linked_list.pop_head())
        self.assertEqual(8, self.linked_list.pop_tail())
        self.assertEqual(4, self.linked_list.pop_head())
        self.assertEqual(6, self.linked_list.pop_tail())
        self.assertEqual(0, self.linked_list.size())

    def test_display(self):
        self.linked_list.add_tail(2)
        self.linked_list.add_tail(4)
        self.linked_list.add_tail(6)
        self.linked_list.add_tail(8)
        self.linked_list.display()
