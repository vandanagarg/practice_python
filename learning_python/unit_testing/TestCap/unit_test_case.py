import unittest
import unit_test

class TestCap(unittest.TestCase):  #inherit from unittest class nd function is TestCase

    def test_one_word(self):
        text = 'python'
        result = unit_test.cap_test(text)
        self.assertEqual(result, "Python")

    def test_multiple_words(self):
        text = "monty python"
        result = unit_test.cap_test(text)
        self.assertEqual(result, "Monty Python")

if __name__ == "__main__":
    unittest.main()
