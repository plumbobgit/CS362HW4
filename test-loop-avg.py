import unittest
import "loop-avg"

class TestAverage(unittest.TestCase):

    def test-average(self):
        self.assertAlmostEqual(loop-avg.average([2, 2, 2]), 2)
        self.assertAlmostEqual(loop-avg.average([2, -2, 2]), .66)
        self.assertAlmostEqual(loop-avg.average([0, 2, 2]), 1.33)

if __name__ == '__main__':
    unittest.main()