import unittest
import volume

class TestFull-Name(unittest.TestCase):

    def test-fullName(self):
        self.assertEqual(full-name.fullName("Brandon", "Plumbo"), "Brandon Plumbo")
        self.assertEqual(full-name.fullName("Brandon"), "Brandon ")
        self.assertEqual(full-name.fullName("Brandon", 1), "Brandon 1")

if __name__ == '__main__':
    unittest.main()