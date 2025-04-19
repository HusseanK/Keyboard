from nltk.metrics import edit_distance
import json
from multiprocessing import Process, Queue

is_running = False

#Open the Json file
with open("word_dict.json", 'r') as f:
    word_dict = json.load(f)

# with open("word_dict_old.json", 'r') as f:
#     word_dict_old = json.load(f)



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

def expanded_window(word_list, middle_index, word_length) -> tuple:
    #Basically just iterating through the word list to find a range
    #The range will go from -1 word length to +1 word length
    low = middle_index
    high = middle_index
    while word_list[low][1][1] != word_length - 2:
        low -= 1
    while word_list[high][1][1] != word_length + 2:
        high += 1

    return [low+1, high-1]

def get_closest_word(input_word, word_list=word_dict, max_distance: int = 2) -> list[str]:
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


    #Below is same code as earlier, just re-made with the new idea

    #Checks each tuple inside the dict, and compares the first word
    if input_word.lower() in [word_list[item][0].lower() for item in range(len(word_list))]:
        #If the word exists, return word
        return [input_word.lower()]
    
    suggestions = []
    '''
    Oh boy this is more complicated
    Basically my tuple is [word, [frequency, length]]
    
    So i'm basically searching each word, then my suggestions is appending:
    [word, distance, frequency]

    and then its the same code as earlier, great!
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
    global is_running
    if not is_running:
        is_running = True
        corrected = get_closest_word(input_text, word_dict)
        queue.put(corrected)











def test_autocorrect_text_improved(input_text) -> str:
    corrected = get_closest_word(input_text, word_dict)
    return corrected



# #Old before binary search + window

# def test_autocorrect_text(input_text) -> str:
#     corrected = old_get_closest_word(input_text, word_dict_old)
#     return corrected

# def old_get_closest_word(input_word, word_list, max_distance: int = 2) -> list[str]:
#     if input_word.lower() in word_list:
#         #If the word exists, return word
#         return [input_word]  # No good suggestion, return as-is
#     suggestions = []
#     for word in word_list:
#         distance = edit_distance(input_word.lower(), word.lower())
#         if distance <= max_distance:
#             suggestions.append((word, distance, word_list[word]))
#     if suggestions:
#         suggestions.sort(key=lambda x: x[1])  # Sort by distance
#         #Cut down to top 6 results, and then first sort by distance, then frequency of word
#         suggestions = sorted(suggestions[:6], key = lambda x: (x[1], -x[2]))
#         suggestions = suggestions[:3] #Cut to top 3 (3 suggests)
        
#         return [suggestion[0] for suggestion in suggestions]
#     else:
#         return [input_word]  # No good suggestion, return as-is

