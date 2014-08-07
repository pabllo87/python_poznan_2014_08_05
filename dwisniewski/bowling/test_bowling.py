import unittest
from bowling import PlayerScore


class BowlingGameTest(unittest.TestCase):

    def setUp(self):
        self.g = PlayerScore()

    def roll_many(self, count, pins):
        for i in range(count):
            self.g.roll(pins)

    def test_gutter_game(self):
        self.roll_many(count=20, pins=0)
        self.assertEqual(0, self.g.score())

    def test_all_ones(self):
        self.roll_many(count=20, pins=1)
        self.assertEqual(20, self.g.score())

    def test_roll_raises_exception_on_text(self):
        with self.assertRaises(TypeError):
            self.g.roll("1")

#    @unittest.skip("Not implemented yet")
    def test_one_spare(self):
        self.g.roll(5)
        self.g.roll(5)  # Spare
        self.g.roll(1)
        self.roll_many(count=17, pins=0)
        self.assertEqual(12, self.g.score())

    def test_one_strike(self):
        self.g.roll(10)  # Strike
        self.g.roll(3)
        self.g.roll(4)
        self.roll_many(count=16, pins=0)
        self.assertEqual(24, self.g.score())

    def test_perfect_game(self):
        self.roll_many(count=12, pins=10)
        self.assertEqual(300, self.g.score())

if __name__ == "__main__":
    unittest.main()
