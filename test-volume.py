import unittest
import volume

class TestVolume(unittest.TestCase):

    def test-volume(self):
        self.assertAlmostEqual(volume.volume(2), 8)
        self.assertAlmostEqual(volume.volume(-2), 8)
        self.assertAlmostEqual(volume.volume(0), 0)

if __name__ == '__main__':
    unittest.main()