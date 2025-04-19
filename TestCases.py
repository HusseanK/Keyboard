import Spellchecker
import unittest

all_words = ["bananas", "appls", "var"]
results = ["banana", "apple", "car"]

class TestSpellCheck(unittest.TestCase):
    def test_spell(self):
        for i in range(len(all_words)):
            result = Spellchecker.test_autocorrect_text_improved(all_words[i])
            self.assertIn(results[i], result)

if __name__ == "__main__":
    unittest.main()



'''
First spell-check results:

    all_words = ["banannas", "appls", "var"]
    results = ["bananas", "apples", "car"]
    Ran 1 test in 16.416s
        OK
    Completes however is slow, lets make it better

'''

'''
Idea:
First have all words sorted by a length property, instead of alphabetical
Then once we have the word, we search only within range(len(word)-1, len(word)+1) distance
That way we cut out a LOT of the actual dict

Idea 1:
Start with a binary search of len(word), finding it in the dict
Then from there we create 2 indexes that spread -/+ till we reach -/+ 1
Then we have our ranges
'''

'''
First spell-check results:
    all_words = ["banannas", "appls", "var"]
    results = ["bananas", "apples", "car"]
    Ran 1 test in 3.058s
        OK
    Improved speed!!!
    from:
        16secs
    to:
        3secs
'''
'''
Improvements to the Big.txt file using nltk.corpus words

however apparently apples and bananas aren't in the word list. which is strange.
    - This is only a test-project, however i could have theoretically imported a few books etc for the word-dict
        which seemed very pointless for this project.

all_words = ["bananas", "appls", "var"]
results = ["banana", "apple", "car"]
Ran 1 test in 2.053s
    OK

The improvement still shows quite a big improvement though
from:
    3secs
to:
    2secs
'''