#Michael Buzzetta
#I pledge my honor that I have abided by the Stevens Honor System


"""
This function takes an input and returns the amount of coins required to make
that amount of money
"""
def change(amount, coins):

    if amount <= 0:
        return 0
    elif coins == []:
        return float("inf")
    elif coins[-1] > amount:
        return change(amount, coins[:-1])
    else:
        use_it = 1 + change(amount - coins[-1], coins)
        lose_it = change(amount, coins[:-1])
        return min(use_it, lose_it)

import unittest
import lab3
class Test(unittest.TestCase):
    def test01(self):
        self.assertEqual(lab3.change(0, []), 0)
    def test02(self):
        self.assertEqual(lab3.change(1, []), float("inf"))
    def test03(self):
        self.assertEqual(lab3.change(1, [1, 5, 10]), 1)
    def test04(self):
        self.assertEqual(lab3.change(7, [1, 5, 10]), 3)
    def test05(self):
        self.assertEqual(lab3.change(29, [1, 5, 10, 20, 50, 100]), 6)
if __name__ == "__main__":
    unittest.main()
