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
    """
    build a hand of 10 letters for the user
    Parameters:    None
    Returns:
    a list of strings with single letters
    """     
    #step1: create a copy of the LETTER_POOL and save all keys in a list
    letter_count_dict = {}
    letter_list = []
    for letter, count in LETTER_POOL.items():
        letter_count_dict[letter] = count
        letter_list.append(letter)
    #step2:randomly pick 10 letters from the letter_pool: for each pick, update count, remove letter from letter_list if count gets to 0;  
    hand = []
    while len(hand) < 10:
        index = randint(0, len(letter_list) - 1)
        letter = letter_list[index]
        count = letter_count_dict[letter] 
        hand.append(letter)
        letter_count_dict[letter] = count - 1
        # new_count = count  - 1
        if count == 1:
            letter_list.pop(index)

    return hand

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass