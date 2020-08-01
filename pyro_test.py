import unittest
import pyro


class TestPyro(unittest.TestCase):
    def test_extract_message(self):
        self.assertEqual(pyro.extract_message('not starting with prefix', '!'), None)
        self.assertEqual(pyro.extract_message('!starting with prefix', '!'), 'starting with prefix')
        self.assertEqual(pyro.extract_message('no prefix', ''), 'no prefix')
        self.assertEqual(pyro.extract_message('@pyro hello', '@Pyro'), 'hello')

    def test_arrow_keys(self):
        self.assertTrue(pyro.is_arrow_keys('left'))
        self.assertTrue(pyro.is_arrow_keys('rIght'))
        self.assertTrue(pyro.is_arrow_keys('Up'))
        self.assertTrue(pyro.is_arrow_keys('down'))
        self.assertFalse(pyro.is_arrow_keys('exclaim'))

    def test_valid_commands(self):
        self.assertTrue(pyro.is_valid_command(''))
        self.assertTrue(pyro.is_valid_command('log'))
        self.assertTrue(pyro.is_valid_command('nonsense'))

        self.assertFalse(pyro.is_valid_command('a very '
                                               'loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong comman'))
        self.assertFalse(pyro.is_valid_command('shutdown'))
        self.assertFalse(pyro.is_valid_command('tricky shutdown'))
        self.assertFalse(pyro.is_valid_command('  Shutdown'))


if __name__ == '__main__':
    unittest.main()
