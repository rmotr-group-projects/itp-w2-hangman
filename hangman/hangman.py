import random
import string
letters = string.ascii_lowercase

WORD_LIST = ['apple', 'banana', 'carrot', 'dinosaur', 'python', 'project',
             'fire', 'goat', 'shrimp', 'lobster', 'rabbit', 'house']

try:
    _input = raw_input
except NameError:
    _input = input

def _get_random_word(word_list):
    
    return random.choice(word_list)

def dic_crypted(word):
    
    masked = {}
    for i in range(len(word)) : 
        masked[i] = ['False', word[i]]
    return masked  


def decrypt_dic(dic) : 
    str = ''
    for i in range(len(dic)) : 
        if dic[i][0] == 'True' : 
            str += dic[i][1]
        else : 
            str += '*'
    return str

def update(dic, letter='*') : 
    for i in range(len(dic)) : 
        if dic[i][1] == letter : 
            dic[i][0] = 'True'
    str = decrypt_dic(dic)
    return str 

def _guess_is_valid(guessed_letter, previous_guesses):
    
    if len(guessed_letter) == 1 and guessed_letter not in previous_guesses and guess_letter in letters : 
        return True 
    else : 
        return False

def _check_lose(remaining_misses):
    
    if remaining_misses == 0 : 
        return True 
    else : 
        False
            
def _check_game_over(answer_word, dic, remaining_misses):
    
    if answer_word == decrypt_dic(dic) or _check_lose(remaining_misses) : 
        return True
    else : 
        return False

def _check_win(answer_word, dic):
    if answer_word == decrypt_dic(dic) : 
        return True
    else : 
        return False


def start_new_game(dic, answer_word=None) :
    
    masked = update(dic) 
    return {

        'answer_word' : answer, 
        'masked_word' : masked, 
        'previous_guesses' : '', 
        'remaining_misses' : 5

    }


def guess_letter(game, letter, dic):
    
    if letter in game['answer_word'] : 
        
        game['masked_word'] = update(dic, letter)

    else : 
        
        game['remaining_misses'] -= 1
    
    game['previous_guesses'] += letter

def start(game, dic, answer) : 
    while not _check_game_over(game['answer_word'], dic, game['remaining_misses']) :  
        print("This is the word to guess: %s" % game['masked_word'])
        print("You have %s misses remaining" % game['remaining_misses'])
        #print answer You like cheating? Uncomment here! 
        input = raw_input("Letter : ")
        guess_letter(game, input, dic)
        if not _guess_is_valid(input, game['previous_guesses']):
            continue

answer = _get_random_word(WORD_LIST)
dic = dic_crypted(answer)
game = start_new_game(dic, answer)
start(game, dic, answer)
print("Thanks for playing!")
