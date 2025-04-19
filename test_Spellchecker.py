import unittest
from multiprocessing import Queue
from Spellchecker import get_closest_word, autocorrect_text

class TestSpellchecker(unittest.TestCase):

    def setUp(self):
        # Sample word dictionary for testing
        self.word_dict = {
            "banana": 100,
            "bandana": 50,
            "band": 30,
            "bananas": 20,
            "bandanas": 10,
            "banner": 5
        }

    def test_get_closest_word_exact_match(self):
        result = get_closest_word("banana", self.word_dict)
        self.assertEqual(result, ["banana"])

    def test_get_closest_word_typo(self):
        result = get_closest_word("banan", self.word_dict)
        self.assertEqual(result, ["banana"])

    def test_get_closest_word_multiple_suggestions(self):
        result = get_closest_word("bandanas", self.word_dict)
        self.assertEqual(result, ["bandanas", "bandana", "bananas"])

    def test_get_closest_word_no_suggestions(self):
        result = get_closest_word("xyz", self.word_dict)
        self.assertEqual(result, ["xyz"])

    def test_autocorrect_text(self):
        queue = Queue()
        autocorrect_text("banan", queue)
        corrected = queue.get()
        self.assertEqual(corrected, ["banana"])

if __name__ == "__main__":
    unittest.main()