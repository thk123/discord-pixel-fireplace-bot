import unittest
import pyro

class TestPyro(unittest.TestCase):
    def test_extract_message(self):
        self.assertEqual(pyro.extract_message('not starting with prefix', '!'), None)
        self.assertEqual(pyro.extract_message('!starting with prefix', '!'), 'starting with prefix')
        self.assertEqual(pyro.extract_message('@pyro hello', '@pyro'), 'hello')

    def test_arrow_keys(self):
        self.assertEqual(pyro.is_arrow_keys('left'), 'left')
        self.assertEqual(pyro.is_arrow_keys('right'), 'right')
        self.assertEqual(pyro.is_arrow_keys('up'), 'up')
        self.assertEqual(pyro.is_arrow_keys('down'), 'down')
        self.assertEqual(pyro.is_arrow_keys('exclaim'), None)

if __name__ == '__main__':
    unittest.main()
