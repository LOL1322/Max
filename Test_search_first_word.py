import unittest
from ad import first_word

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(first_word("hello word"), "hello")


if __name__ == '__main__':
    unittest.main()
