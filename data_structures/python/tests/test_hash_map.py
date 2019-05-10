import unittest
from data_structures.python.hash_map import HashMap


class TestHashMap(unittest.TestCase):

    def setUp(self):
        self.hash_map = HashMap()
    
    def test_set_item(self):
        self.hash_map["A"] = 1
        self.hash_map["B"] = 2
        self.hash_map["C"] = 3
        self.hash_map["D"] = 4
        self.hash_map["E"] = 5
        self.hash_map["F"] = 6
        self.hash_map["G"] = 7
        self.hash_map["H"] = 8
        self.hash_map["A"] = 1
        self.hash_map["A"] = 1

        self.assertEqual(8, self.hash_map.size())

    def test_get_item(self):
        self.hash_map["A"] = 1
        self.hash_map["B"] = 2
        self.hash_map["C"] = 3
        self.hash_map["D"] = 4
        self.hash_map["E"] = 5
        self.hash_map["F"] = 6
        self.hash_map["G"] = 7
        self.hash_map["H"] = 8
        self.hash_map["A"] = 99

        self.assertEqual(99, self.hash_map["A"])
        self.assertEqual(2, self.hash_map["B"])
        self.assertEqual(3, self.hash_map["C"])
        self.assertEqual(4, self.hash_map["D"])
        self.assertEqual(5, self.hash_map["E"])
        self.assertEqual(6, self.hash_map["F"])
        self.assertEqual(7, self.hash_map["G"])
        self.assertEqual(8, self.hash_map["H"])

    def test_resize(self):
        self.hash_map["A"] = 1
        self.hash_map["B"] = 2
        self.hash_map["C"] = 3
        capacity = self.hash_map._capacity

        self.hash_map["D"] = 1
        self.hash_map["E"] = 2
        self.hash_map["F"] = 3
        self.assertGreater(self.hash_map._capacity, capacity)

    def test_display(self):
        self.hash_map["A"] = 1
        self.hash_map["B"] = 2
        self.hash_map["C"] = 3
        self.hash_map["D"] = 4
        self.hash_map["E"] = 5
        self.hash_map["F"] = 6
        self.hash_map["G"] = 7
        self.hash_map["H"] = 8
        self.hash_map.display()
