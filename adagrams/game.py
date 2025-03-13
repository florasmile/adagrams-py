from random import randint

LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}
def draw_letters():
    #goal: generate a list of 10 letters randomly selected from LETTER_POOL
    #step1: create a list of letters
    all_letters = []
    for letter in LETTER_POOL.keys():
        all_letters.append(letter)
    #step2:use iteration, generate 26 randomly nums (0-25) as index, select letters from list, append it to the new list
    result = []
    for i in range(10):
        index = randint(0, 25)
        result.append(all_letters[index])
    return result

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass