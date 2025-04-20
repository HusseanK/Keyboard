from nltk.metrics import edit_distance
import json

#Open the Json file
with open("keyboard_creator/spell_checker/word_dict.json", 'r') as f:
    word_dict = json.load(f)

def binary_search(word_list, word_length: int) -> int:
    #Simple binary search, Checking through the word length
    low = 0
    high = len(word_list) - 1
    mid = 0
    #Checks through word_list[mid][1][1] which is the length of the word
    while low <= high:
        mid = (high + low) // 2
        if word_list[mid][1][1] < word_length:
            low = mid + 1
        elif word_list[mid][1][1] > word_length:
            high = mid - 1
        else:
            #Returns middle index, first num at len(word)
            return mid
    return -1

def expanded_window(word_list: dict[str,list[int]], middle_index:int, word_length:int) -> tuple:
    '''
    Basically just iterating through the word list to find a range
    The range will go from -1 word length to +1 word length
    '''
    low = middle_index
    high = middle_index
    while word_list[low][1][1] != word_length - 2:
        low -= 1
    while word_list[high][1][1] != word_length + 2:
        high += 1
    return [low+1, high-1]

def get_closest_word(input_word: str, word_list: dict[str,list[int]] = word_dict) -> list[str]:
    max_distance = 2
    '''
    This uses an algorithm within nlk.metrics to find "edit_distance" of a word
        An edit distance is just how many chars need-
        to be added/removed/changed in order to reach the desired word

    It then receives the word dict i've created and the word
    '''

    if len(input_word) >= 3:
        #First find the mid index using a binary search
        middle_index = binary_search(word_list, len(input_word)) #int
        #Then make a range using my expanded window algo
        min_ind, max_ind = expanded_window(word_list, middle_index, len(input_word)) #tuple
        word_list = word_list[min_ind:max_ind]
    else:
        middle_index = binary_search(word_list, len(input_word)+1)
        min_ind, max_ind = expanded_window(word_list, middle_index, len(input_word)+1) #tuple
        word_list = word_list[min_ind:max_ind]


    suggestions = []

    '''
    Temporarily removed, i noticed that it makes more sense to still return 3words regardless
    There are too many similar words in English that a typo can be caught as the correct word
    '''
    #Returns the word if it's already correct
    # if input_word.lower() in [word_list[item][0].lower() for item in range(len(word_list))]:
    #     return [input_word.lower()]

    '''
    Basically my tuple is [word, [frequency, length]]
    
    Search each tuple, then my suggestions is appending:
    [word, distance, frequency]
    '''
    for word in range(len(word_list)):
        distance = edit_distance(input_word.lower(), word_list[word][0].lower())
        if distance <= max_distance:
            suggestions.append((word_list[word][0], distance, word_list[word][1][0]))
    if suggestions:
        suggestions.sort(key=lambda x: x[1])  # Sort by distance
        #Cut down to top 6 results, and then first sort by distance, then frequency of word
        suggestions = sorted(suggestions[:12], key = lambda x: (x[1], -x[2]))
        suggestions = suggestions[:3] #Cut to top 3 (3 suggests)
        return [suggestion[0] for suggestion in suggestions]
    else:
        return [input_word]  # No good suggestion, return as-is

def autocorrect_text(input_text, queue) -> str:
    corrected = get_closest_word(input_text, word_dict)
    queue.put(corrected)





'''
Unit testing below, done within the test_cases.py file
separate function due to my spell-check using Process and Queues
Which aren't necessary for testing purposes
'''

def unit_test_auto_correct(input_text) -> str:
    corrected = get_closest_word(input_text, word_dict)
    return corrected