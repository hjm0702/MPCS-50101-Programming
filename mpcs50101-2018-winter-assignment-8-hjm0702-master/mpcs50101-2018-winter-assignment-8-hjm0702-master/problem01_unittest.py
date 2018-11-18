import problem01
import unittest

class TestBalancer(unittest.TestCase):
    def test_True(self):
        '''Test it is True/False when it should be true/False'''
        self.assertEqual(problem01.balancer("(())[]{}"), "Symbols are balanced!!!! :)")
        self.assertEqual(problem01.balancer("(("), "Symbols are not balanced :(")

    def test_False(self):
        '''Test it is False when it should be True'''
        self.assertNotEqual(problem01.balancer("(("), "Symbols are balanced!!!! :)")
        self.assertNotEqual(problem01.balancer("(())"), "Symbols are not balanced :(")

if __name__ == "__main__":
    unittest.main()
