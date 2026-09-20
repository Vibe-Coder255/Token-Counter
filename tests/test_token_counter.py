import unittest

from Services.token_counter import count_tokens


class TokenCounterTests(unittest.TestCase):
    def test_counts_non_zero_tokens(self):
        text = "Hello world, this is a test."
        self.assertGreater(count_tokens(text), 0)

    def test_same_text_same_count(self):
        text = "Token counting should be consistent."
        self.assertEqual(count_tokens(text), count_tokens(text))

    def test_empty_text_is_zero(self):
        self.assertEqual(count_tokens(""), 0)


if __name__ == "__main__":
    unittest.main()
