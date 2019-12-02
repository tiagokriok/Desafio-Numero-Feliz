import unittest
from  CheckHappy import checkHappy

class TestHappy(unittest.TestCase):
    def test_get(self):

        happy = checkHappy()

        test = [
            (7,True),
            (49,True),
            (97,True),
            (130,True),
            (10,True),
            (11,False),
            (13,True)
        ]

        for num, expected in test:
            with self.subTest(num=num):
                self.assertEqual(happy.isHappy(num),expected)

if __name__ == "__main__":
    unittest.main()