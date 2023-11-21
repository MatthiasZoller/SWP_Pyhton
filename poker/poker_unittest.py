import unittest
import poker as p


class Test_Poker(unittest.TestCase):
    def test_is_straight(self):
        hand = [(11, 2), (12, 3), (13, 1), (14, 0), (15, 2)]
        self.assertTrue(p.is_straight(hand))

    def test_is_full_house(self):
        hand = [(4, 0), (4, 1), (5, 2), (5, 3), (5, 0)]
        self.assertTrue(p.is_full_house(hand))

    def test_is_flush(self):
        hand = [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0)]
        self.assertTrue(p.is_flush(hand))


if __name__ == '__main__':
    unittest.main()
