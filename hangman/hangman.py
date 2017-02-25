import random


WORD_LIST = ['apple', 'banana', 'carrot', 'dinosaur', 'python', 'project',
             'fire', 'goat', 'shrimp', 'lobster', 'rabbit', 'house']


try:
    _input = raw_input
except NameError:
    _input = input


# Internal helpers
def _get_random_word(word_list):
    return word_list[random.randint(0, len(word_list) - 1)]


def _mask_word(word):
    """
    Takes the answer word and returns a string of '*' characters of the
    same length to show the user the masked word.
    :param word: The answer word for the current game
    Example: word - 'cat'     masked word - '***'
    """
    print(word)
    return len(word) * '*'


def _guess_is_valid(guessed_letter, previous_guesses):
    """
    Checks if the letter guessed is one character long, has not already been
    guessed, and verifies the character guessed is a letter in the alphabet.
    :param guessed_letter: The letter the user guesses
    :param previous_guesses: A string of all the letters previously guessed
    Returns True if given guess is valid, False otherwise.
    """
    if guessed_letter.isalpha() and len(guessed_letter) == 1 and guessed_letter not in previous_guesses:
        return True
    else:
        return False


def _check_lose(remaining_misses):
    """
    Returns True if remaining guesses is equal to 0 and false otherwise.
    :param remaining_misses: How many misses are left before user loses
    """
    if remaining_misses == 0:
        return True
    else:
        return False


def _check_win(answer_word, masked_word):
    """
    Returns True if answer word matches the masked word and False otherwise.
    This works because the masked word is updated each time a correct letter
    is guessed to replace that '*' character with the correct letter. If the
    user has one, matched word and answer word will be the same.
    :param answer_word: The answer word for the current game
    :param masked_word: The answer word masked with '*' characters for letters
                        that haven't been guessed
    """
    if answer_word == masked_word:
        return True
    else:
        return False


def _check_game_over(answer_word, masked_word, remaining_misses):
    """
    Returns True if _check_win is True or _check_lose is True, and False
    otherwise.
    :param answer_word: The answer word for the current game
    :param masked_word: The answer word masked with '*' characters for letters
                        that haven't been guessed
    :param remaining_misses: How many misses are left before user loses
    """
    if _check_win(answer_word, masked_word) or _check_lose(remaining_misses):
        return True
    else:
        return False


# Public interface
def start_new_game(word_list, answer_word=None):
    """
    Creates and returns a new game configuration.
    :param answer_word: Optional manually chosen answer word for game with
                        default value of None if nothing is provided.
    This returns a dictionary that stores 4 pieces of game information:
    answer_word - The answer word that is the solution to the game
    masked_word - The answer word masked with '*' characters
    previous_guesses - The previous valid letter guesses the user has inputted
    remaining_misses - how many misses the user has left. Start with 5.
    """
    if answer_word == None:
        answer_word = _get_random_word(word_list)
        
    game_info = { 'answer_word': answer_word, 
                  'masked_word': _mask_word(answer_word),
                  'previous_guesses': '',
                  'remaining_misses': 5
                  }
    return game_info

def guess_letter(game, letter):
    """
    This function receives a valid guess and processes it.
    If it is a correct guess, it updates the masked_word in the dictionary
    by replacing the '*' characters with letters that have been correctly
    guessed.
    If it is an incorrect guess, update remaining_misses in the game so it has
    one less.
    Finally, update the previous_guesses in the game to reflect the letter that
    has been guessed.
    You are only updating values in your dictionary so no return required for
    this function.
    :param game: The dictionary storing current game information
    :param letter: The letter that is being guessed
    """
   
    if _guess_is_valid(letter, game['previous_guesses']):
        game['previous_guesses'] += letter
        new = ""
        for char in range(len(game['answer_word'])):
            if letter == game['answer_word'][char]:
                new += letter
            else:
                new += game['masked_word'][char]
        game['masked_word'] = new
    if letter not in game['answer_word']:
        game['remaining_misses'] -= 1
        # for num, val in enumerate(game['answer_word']):
        #     if letter == val: 
        #         game['masked_word'].replace(game['masked_word'][num], letter)
        # if letter not in game['answer_word']:
        #     game['remaining_misses'] -= 1
            
        # 
                
"""
>>> name['a']
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    name['a']
TypeError: string indices must be integers
>>> 

>>> name
'Santiago'
>>> name[3]
't'
>>> name.replace(name[3], 'A')
'SanAiago'
>>> 


>>> for num, val in enumerate(mylist):
    print(num, val)

    
0 Josh
1 Viet
2 Manny
3 Santiago
4 Martin
>>> 

for num, val in enumerate('Santiago'):
    if val == 'n':
        num
        
        
choices = ['pizza', 'pasta', 'salad', 'nachos']
>>> for num, val in enumerate(choices, start=999):
    print(num, val)

    
999 pizza
1000 pasta
1001 salad
1002 nachos
>>> 


"""

def user_input_guess(game):
    """
    Repeats user input guesses until game is over. If guess is invalid,
    repeat input until it is valid. Once guess is valid, process the guess.
    :param game: The dictionary storing current game information
    """
    while not _check_game_over(game['answer_word'], game['masked_word'],
                               game['remaining_misses']):
        guess = _input("Guess a letter: ")
        if not _guess_is_valid(guess, game['previous_guesses']):
            continue
        guess_letter(game, guess)
        print("This is the word to guess: %s" % game['masked_word'])
        print("You have %s misses remaining" % game['remaining_misses'])




        # guessed_letter = raw_input("Guess a letter: ")






if __name__ == '__main__':
    game = start_new_game(WORD_LIST)
    user_input_guess(game)
