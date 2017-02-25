#make test: PYTHONPATH=. py.test -s tests
#adding a test name on end runs a specific test
#adding --tb=no to the end "cleans up" what is returned
#...then adding -v to the end will produce an organized listing of
  #all the tests and their results
#Try adding --tb=line or --tb=short before -v instead of --tb==no

import random
import string


WORD_LIST = ['apple', 'banana', 'carrot', 'dinosaur', 'python', 'project',
             'fire', 'goat', 'shrimp', 'lobster', 'rabbit', 'house']




#ensures that the input command will work across different pythons
try:
    _input = raw_input
except NameError:
    _input = input
    
    

# Internal helpers
#random.choice(word_list)
def _get_random_word(word_list):
    """
    Returns a random word from the word_list to use as the answer word.
    :param word_list: The list of possible answer words
    """
    return random.choice(word_list)


def _mask_word(word):
    """
    Takes the answer word and returns a string of '*' characters of the
    same length to show the user the masked word.
    :param word: The answer word for the current game
    Example: word - 'cat'     masked word - '***'
    """
    return len(word) * '*'


def _guess_is_valid(guessed_letter, previous_guesses):
    """
    Checks if the letter guessed is one character long, has not already been
    guessed, and verifies the character guessed is a letter in the alphabet.
    :param guessed_letter: The letter the user guesses
    :param previous_guesses: A string of all the letters previously guessed
    Returns True if given guess is valid, False otherwise.
    """
    # it's 1 character long, .isalpha(), and NOT in previous_guesses

    if len(guessed_letter) == 1 and guessed_letter not in previous_guesses and guessed_letter.isalpha():
        return True
    return False

    # guessed_letter.isaplha() True if in alphabet, False 


def _check_lose(remaining_misses):
    """
    Returns True if remaining guesses is equal to 0 and false otherwise.
    :param remaining_misses: How many misses are left before user loses
    """
    if remaining_misses == 0:
        return True
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

    game_config = {'answer_word': answer_word, 'masked_word': _mask_word(answer_word),
    'previous_guesses': '', 'remaining_misses': 5}

    return game_config


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
    # global guessed_chars
    # prev_guesses = game['previous_guesses']
    # unmasked_string = ''
    
    # letter_index = []
 
    # if _guess_is_valid(letter, prev_guesses):
    #     for elem in game['answer_word']:
    #         if elem == letter:
    #             letter_index.append(game['answer_word'].index(elem))
    #     for idx in letter_index:        
    #         for num, val in enumerate(game['masked_word']):
    #             if num != idx:
    #                 unmasked_string += '*'
    #             else:
    #                 unmasked_string += letter
    #     game['masked_word'] = unmasked_string
    if _guess_is_valid(letter, game['previous_guesses']):
        newstring = ''
        for num, val in enumerate(game['answer_word']):
            if val == letter:
                newstring += val
            else:
                newstring += game['masked_word'][num]
        
        game['masked_word'] = newstring
        game['previous_guesses'] += letter
        
        if letter not in game['answer_word']:
            game['remaining_misses'] -= 1


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


if __name__ == '__main__':
    game = start_new_game(WORD_LIST)
    user_input_guess(game)
