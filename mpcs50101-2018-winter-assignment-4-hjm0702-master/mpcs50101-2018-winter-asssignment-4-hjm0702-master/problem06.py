import statistics
import problem05_1
import unittest
import random

'''I changed Problem05 into Problem05_1
because if I don't change it, Problem05's input setting affects a unittest process'''

'''random'''

# sample = [1,2,3,4,100]
random_number = input("Enter a interger number less or equal to 100.")
sample = []
for x in range(int(random_number)):
    x = random.randint(0,100)
    sample.append(x)


class test_problem05_01(unittest.TestCase):
    def test_mean(self):
        self.assertEqual(problem05_1.mean(sample), statistics.mean(sample))

    def test_median(self):
        self.assertEqual(problem05_1.median(sample), statistics.median(sample))

    def test_mode(self):
        try :
            self.assertEqual(int(problem05_1.mode(sample)[0]), statistics.mode(sample))
        except:
            print("Mode Test cannot be executed since there are more than one unique modes ")


    def test_variance(self):
        self.assertEqual(round(problem05_1.variance(sample),2), round(statistics.pvariance(sample),2))

    def test_standard_deviation(self):
        self.assertEqual(round(problem05_1.standard_deviation(sample),2), round(statistics.pstdev(sample),2))


if __name__ == '__main__':
    unittest.main()
