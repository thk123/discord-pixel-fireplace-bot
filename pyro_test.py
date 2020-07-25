import unittest
import pyro

class TestPyro(unittest.TestCase):
    def test_extract_message(self):
        self.assertEqual(pyro.extract_message('not starting with prefix', '!'), None)
        self.assertEqual(pyro.extract_message('!starting with prefix', '!'), 'starting with prefix')
        self.assertEqual(pyro.extract_message('@pyro hello', '@pyro'), 'hello')

    def test_arrow_keys(self):
        self.assertTrue(pyro.is_arrow_keys('left'))
        self.assertTrue(pyro.is_arrow_keys('rIght'))
        self.assertTrue(pyro.is_arrow_keys('Up'))
        self.assertTrue(pyro.is_arrow_keys('down'))
        self.assertFalse(pyro.is_arrow_keys('exclaim'))

if __name__ == '__main__':
    unittest.main()
