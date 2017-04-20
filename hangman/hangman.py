import random


WORD_LIST = ['apple', 'banana', 'carrot', 'dinosaur', 'python', 'project',
             'fire', 'goat', 'shrimp', 'lobster', 'rabbit', 'house']


try:
    _input = raw_input
except NameError:
    _input = input


# Internal helpers
def _get_random_word(word_list):
    answer_word = word_list[random.randint(0, len(word_list)-1)]
    return answer_word
    


def _mask_word(word):
    
    masked_word = len(str(word))*'*'
    return masked_word


def _guess_is_valid(guessed_letter, previous_guesses):
    """
    Checks if the letter guessed is one character long, has not already been
    guessed, and verifies the character guessed is a letter in the alphabet.
    :param guessed_letter: The letter the user guesses
    :param previous_guesses: A string of all the letters previously guessed
    Returns True if given guess is valid, False otherwise.
    """
    
    if len(guessed_letter) != 1:
        return False
    elif guessed_letter in previous_guesses:
        return False
    elif not guessed_letter.isalpha():
        return False
    else:
        return True



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
    if _check_win(answer_word, masked_word) is True:
        return True
    elif _check_lose(remaining_misses) is True:
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
   
    if not answer_word:  #if answer_word == None:
        answer_word = _get_random_word(word_list)
    masked_word = _mask_word(answer_word)
    previous_guesses = ''
    remaining_misses = 5 
    game = {'answer_word': answer_word, 'masked_word': masked_word, 'previous_guesses': previous_guesses, 'remaining_misses': remaining_misses}
                
    return game


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
    '''game = start_new_game(word_list, answer_word=None)'''
    # https://repl.it/EMRT
    
    answer_word_list = list(game['answer_word'])
    masked_word_list = list(game['masked_word'])
    print(game)
    if _guess_is_valid(letter, game['previous_guesses']):
        game['previous_guesses'] = game['previous_guesses'] + letter
        for i in range(len(answer_word_list)):
            if answer_word_list[i] == letter:
                masked_word_list[i] = letter
        if letter not in masked_word_list:
            game['remaining_misses'] -= 1

    game['masked_word'] = ''.join(masked_word_list)


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
