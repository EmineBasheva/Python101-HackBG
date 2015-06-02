from histogram import Histogram
import unittest


class TestHistogram(unittest.TestCase):

    def setUp(self):
        self.h = Histogram()
        self.h.add("Apache")
        self.h.add("Apache")
    
    def test_add(self):
        self.assertEqual(self.h.get_dict()["Apache"], 2)

    def test_count(self):
        self.assertEqual(self.h.count("Apache"), 2)

    def test_items(self):
        self.assertEqual(self.h.items(), self.h.get_dict().items())


if __name__ == '__main__':
    unittest.main()