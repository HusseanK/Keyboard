import re
from collections import Counter
import json
from nltk.corpus import words
import nltk


'''
Just a quick way i made my own dictionary
I did this to count *frequency* of words
i used the "big.txt" as my go-to analysis (It's sherlock holmes, lol)

Basically justs makes a .json file that has each word and a num-frequency
Also its sorted, removes words that had started/ended with "_"
Also removed the numbers(dates etc) manually, because they were all at the top (and fast to do)'''

# Also going to import words from the nltk.corpus, just to catch any words that big.txt has missed
# with open("big.txt", "a", encoding="utf-8") as f:
#     for word in words.words():
#         f.write(word + "\n")

if __name__ == "__main__":
    
    def extract_words(text):
        valid_words = set(words.words())
        #Returns each word as a str
        extracted_words = re.findall(r'\b[a-zA-Z]+\b', text)

        extracted_words = list(filter(lambda x: x in valid_words, extracted_words))
        extracted_words = [word.lower() for word in extracted_words]
        return extracted_words

    with open("big.txt", "r", encoding="utf-8", errors="ignore") as f:
        #opening big.txt file, then using the Counter module to create a dict based on frequency
        full_dict = Counter(extract_words(f.read()))

    length_of_words = dict()
    #Change the full-dict to include length of word

    for key, value in full_dict.items():
        if key not in length_of_words:
            length_of_words[key] = []
        length_of_words[key].extend((value, len(key)))

    #Sorts by length of word
    final_tuple = sorted(length_of_words.items(), key=lambda item: item[1][1])

    result_tuple = []

    #removing weird characters if they exist
    for i in range(len(final_tuple)):
        if final_tuple[i][0].startswith("_") or final_tuple[i][0].endswith("_"):
            pass
        else:
            result_tuple.append(final_tuple[i])

    #and then just dumping it all into a json file for later
    with open("word_dict.json", 'a') as f2:
        f2.write(json.dumps(result_tuple, ensure_ascii=False, indent=1))


        # #json.dumps doesn't really indent tuples within tuples properly
        # #So i just iterated over all words and added ,\n to make it pretty
        # f2.write("{")
        # for each_word in result_tuple:
        #     f2.write(json.dumps(each_word, ensure_ascii=False)+",\n")
        # f2.write("}")



    # #sorting the dict by the words (A-Z)  - REMOVED
    # final_dict = dict(sorted(full_dict.items()))

    # # Quickly removing any chars with underscores
    # result_dict = {}

    # for key in final_dict:
    #     if key.startswith("_") or key.endswith("_"):
    #         pass
    #     else:
    #         result_dict[key] = final_dict[key]

    # #and then just dumping it all into a json file for later
    # with open("word_dict_old.json", 'a') as f2:
    #     f2.write(json.dumps(result_dict, ensure_ascii=False, indent=4))