import unittest
from rul import RUL


class RUL_empty_test(unittest.TestCase):

    def setUp(self):
        self.rul = RUL()

    def test_is_empty_after_create(self):
        self.assertTrue(self.rul.empty())

    def test_is_not_empty_after_insert(self):
        self.rul.add('a')
        self.assertFalse(self.rul.empty())

    def test_size_zero_empty_list(self):
        self.assertEqual(0, self.rul.size())

    def test_size_after_add_one_element(self):
        self.rul.add('a')
        self.assertEqual(1, self.rul.size())

    def test_throw_raise_when_get_first_element_from_empty_list(self):
        with self.assertRaises(IndexError):
            self.rul.first()

    def test_get_first_element(self):
        self.rul.add('a')
        self.assertEqual('a', self.rul.first())

    def test_get_item_by_index(self):
        self.rul.add('a')
        self.assertEqual('a', self.rul[0])


class RUL_populated_test(unittest.TestCase):

    def setUp(self):
        self.rul = RUL()
        self.items = ['item1', 'item2', 'item3', 'item4']
        for item in self.items:
            self.rul.add(item)

    def test_first_is_last_inserted(self):
        self.assertEqual(self.items[-1], self.rul.first())

    def test_items_are_in_LIFO_order(self):
        rul_list = [self.rul[i] for i in range(len(self.items))]
        rev_items = list(reversed(self.items))
        self.assertEqual(rev_items, rul_list)

    def test_add_same_element(self):
        self.rul.add(self.items[0])
        self.assertEqual(len(self.items), self.rul.size())

    def test_add_same_element_move_to_first(self):
        self.rul.add(self.items[0])
        self.assertEqual(self.items[0], self.rul.first())

    def test_add_empty_string(self):
        self.rul.add('')
        self.assertEqual(len(self.items), self.rul.size())

    def test_throws_for_bad_index(self):
        with self.assertRaises(IndexError):
            self.rul[len(self.items)]

    def test_items_are_in_order_after_duplicate_insert(self):
        self.rul.add(self.items[0])
        rul_list = [self.rul[i] for i in range(len(self.items))]
        test_items = ['item1', 'item4', 'item3', 'item2']
        self.assertEqual(test_items, rul_list)


class RUL_populated_limit_test(unittest.TestCase):

    def setUp(self):
        self.rul = RUL(limit=3)
        self.items = ['item1', 'item2', 'item3', 'item4']
        for item in self.items:
            self.rul.add(item)

    def test_limit_list(self):
        self.assertEqual(3, self.rul.size())

    def test_delete_last_element(self):
        for i in range(self.rul.get_limit()):
            self.assertEqual(self.items[-i-1], self.rul[i])

    def test_iterator(self):
        iterator = iter(self.rul)
        for i in range(self.rul.get_limit()):
            self.assertEqual(self.items[-i-1], iterator.next())
        with self.assertRaises(StopIteration):
            iterator.next()
