import unittest

from RUL import RUL

class RUL_Empty_Tests(unittest.TestCase):
    def setUp(self):
        self.rul = RUL()

    def test_is_empty_after_creation(self):
        self.assertTrue(self.rul.empty())

    def test_is_not_empty_after_insert(self):
        self.rul.add("item")
        self.assertFalse(self.rul.empty())

    def test_size_zero_after_creating(self):
        self.assertEqual(0, self.rul.size())

    def test_size_one_after_one_insert(self):
        self.rul.add("item")
        self.assertEqual(1, self.rul.size())

    def test_return_first_item_on_empty_throws(self):
        with self.assertRaises(IndexError):
            self.rul.first()

    def test_first_return_inserted_item(self):
        self.rul.add("item")
        self.assertEqual("item", self.rul.first())

class RUL_Populated_Tests(unittest.TestCase):
    def setUp(self):
        self.rul = RUL()
        self.items = ["item1", "item2", "item3", "item4"]
        for item in self.items:
            self.rul.add(item)

    def test_first_is_last_inserted(self):
        self.assertEqual(self.items[-1], self.rul.first())

    def test_size_equals_to_items_size(self):
        self.assertEqual(len(self.items), self.rul.size())

    def test_throws_for_bad_index(self):
        with self.assertRaises(IndexError):
            self.rul[self.rul.size()]

    def test_items_are_in_LIFO_order(self):
        rul_list = [self.rul[i] for i in range(len(self.items))]
        rev_items = list(reversed(self.items))
        self.assertEqual(rev_items, rul_list)
        # self.assertEqual(self.items[2], self.rul[0])
        # self.assertEqual(self.items[1], self.rul[1])
        # self.assertEqual(self.items[0], self.rul[2])

class RUL_Populated_plus_duplicated_item_inserted_Tests(unittest.TestCase):
    def setUp(self):
        self.rul = RUL()
        self.items = ["item1", "item2", "item3", "item4"]
        for item in self.items:
            self.rul.add(item)
        self.rul.add(self.items[0])

    def test_insert_duplicate_doesnt_resize(self):
        self.assertEqual(len(self.items), self.rul.size())

    def test_insert_duplicate_moves_to_front(self):
        self.assertEqual(self.items[0], self.rul.first())

    def test_items_are_in_order_after_duplicate_insert(self):
        rul_list = [self.rul[i] for i in range(len(self.items))]
        test_items = ["item1", "item4", "item3", "item2"]
        self.assertEqual(test_items, rul_list)

if __name__ == "__main__":
    unittest.main()
