import unittest
from autocorrect import correct_text


class TestAutocorrect(unittest.TestCase):

    def test_empty_input(self):
        self.assertEqual(correct_text(""), "")

    def test_whitespace_input(self):
        self.assertEqual(correct_text("   "), "")

    def test_returns_string(self):
        result = correct_text("I hav a gud day")
        self.assertIsInstance(result, str)

    def test_nonempty_input(self):
        result = correct_text("I hav a gud day")
        self.assertNotEqual(result, "")


if __name__ == "__main__":
    unittest.main()
