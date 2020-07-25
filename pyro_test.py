import unittest
import pyro

class TestPyro(unittest.TestCase):
    def test_extract_message(self):
        self.assertEqual(pyro.extract_message('not starting with prefix', '!'), None)
        self.assertEqual(pyro.extract_message('!starting with prefix', '!'), 'starting with prefix')
        self.assertEqual(pyro.extract_message('@pyro hello', '@pyro'), 'hello')


if __name__ == '__main__':
    unittest.main()
