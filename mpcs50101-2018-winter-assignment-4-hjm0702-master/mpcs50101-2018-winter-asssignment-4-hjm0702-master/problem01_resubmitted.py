import unittest
import problem01


class test_temperature(unittest.TestCase):
    def test_is_notstring(self):
        '''Test a input is string or not'''
        self.assertFalse(problem01.temperature("hi"),True)

    def test_accuracy(self):
        '''Test that when input is 32, output must be 0'''
        self.assertEqual(round(problem01.temperature("32.01"),2),0.01)

if __name__ == '__main__':
    unittest.main()
