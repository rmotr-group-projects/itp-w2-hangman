import unittest

from hangman.hangman import (_get_random_word, _mask_word, _guess_is_valid,
                             _check_lose, _check_win, _check_game_over,
                             _check_game_over, start_new_game, guess_letter)


class TestHangman(unittest.TestCase):

    def test_get_random_word(self):
        word_list = ['cat', 'dog', 'mouse']
        self.assertEqual(_get_random_word(word_list) in word_list, True)

    def test_mask_word(self):
        self.assertEqual(_mask_word('howdy'), '*****')

    def test_guess_valid(self):
        self.assertEqual(_guess_is_valid('a', 'bcd'), True)

    def test_guess_invalid_repeat(self):
        self.assertEqual(_guess_is_valid('a', 'abcd'), False)

    def test_guess_invalid_nonalpha(self):
        self.assertEqual(_guess_is_valid('1', 'abcd'), False)

    def test_guess_invalid_too_long(self):
        self.assertEqual(_guess_is_valid('sf', 'abcd'), False)

    def test_guess_invalid_empty(self):
        self.assertEqual(_guess_is_valid('', 'abcd'), False)

    def test_check_lose_true(self):
        self.assertEqual(_check_lose(0), True)

    def test_check_lose_false(self):
        self.assertEqual(_check_lose(2), False)

    def test_check_win_true(self):
        self.assertEqual(_check_win('cat', 'cat'), True)

    def test_check_win_false(self):
        self.assertEqual(_check_win('cat', '**t'), False)

    def test_check_game_over_true_win(self):
        self.assertEqual(_check_game_over('cat', 'cat', 3), True)

    def test_check_game_over_true_lose(self):
        self.assertEqual(_check_game_over('cat', 'c**', 0), True)

    def test_check_game_over_false(self):
        self.assertEqual(_check_game_over('cat', '**t', 4), False)

    def test_start_game_no_default_value(self):
        word_list = ['happy']
        expected = {
            'answer_word': 'happy',
            'masked_word': '*****',
            'previous_guesses': '',
            'remaining_misses': 5
        }

        game = start_new_game(word_list)
        self.assertEqual(game, expected)

    def test_start_game_default_value(self):
        word_list = ['happy', 'party']
        expected = {
            'answer_word': 'santiago',
            'masked_word': '********',
            'previous_guesses': '',
            'remaining_misses': 5
        }

        game = start_new_game(word_list, 'santiago')
        self.assertEqual(game, expected)

    def test_guess_letter_correct(self):
        word_list = []
        expected = {
            'answer_word': 'santiago',
            'masked_word': '*a***a**',
            'previous_guesses': 'a',
            'remaining_misses': 5
        }

        game = start_new_game(word_list, 'santiago')
        guess_letter(game, 'a')
        self.assertEqual(game, expected)

    def test_guess_letter_incorrect(self):
        word_list = []
        expected = {
            'answer_word': 'santiago',
            'masked_word': '********',
            'previous_guesses': 'b',
            'remaining_misses': 4
        }

        game = start_new_game(word_list, 'santiago')
        print game
        guess_letter(game, 'b')
        print game
        self.assertEqual(game, expected)

    def test_win(self):
        word_list = []
        game = start_new_game(word_list, 'cat')

        guess_letter(game, 'c')
        self.assertEqual(
            _check_game_over(game['answer_word'],
                             game['masked_word'],
                             game['remaining_misses']),
            False)

        guess_letter(game, 'a')
        self.assertEqual(
            _check_game_over(game['answer_word'],
                             game['masked_word'],
                             game['remaining_misses']),
            False)

        guess_letter(game, 'b')
        self.assertEqual(
            _check_game_over(game['answer_word'],
                             game['masked_word'],
                             game['remaining_misses']),
            False)

        guess_letter(game, 't')
        self.assertEqual(
            _check_game_over(game['answer_word'],
                             game['masked_word'],
                             game['remaining_misses']),
            True)
        self.assertEqual(
            _check_win(game['answer_word'],
                       game['masked_word']),
            True)

        expected = {
            'answer_word': 'cat',
            'masked_word': 'cat',
            'previous_guesses': 'cabt',
            'remaining_misses': 4
        }
        self.assertEqual(game, expected)

    def test_lose(self):
        word_list = []
        game = start_new_game(word_list, 'house')

        guess_letter(game, 'a')
        self.assertEqual(
            _check_game_over(game['answer_word'],
                             game['masked_word'],
                             game['remaining_misses']),
            False)

        guess_letter(game, 'b')
        self.assertEqual(
            _check_game_over(game['answer_word'],
                             game['masked_word'],
                             game['remaining_misses']),
            False)

        guess_letter(game, 'c')
        self.assertEqual(
            _check_game_over(game['answer_word'],
                             game['masked_word'],
                             game['remaining_misses']),
            False)

        guess_letter(game, 'd')
        self.assertEqual(
            _check_game_over(game['answer_word'],
                             game['masked_word'],
                             game['remaining_misses']),
            False)

        guess_letter(game, 'e')
        self.assertEqual(
            _check_game_over(game['answer_word'],
                             game['masked_word'],
                             game['remaining_misses']),
            False)

        guess_letter(game, 'f')
        self.assertEqual(
            _check_game_over(game['answer_word'],
                             game['masked_word'],
                             game['remaining_misses']),
            True)
        self.assertEqual(_check_lose(game['remaining_misses']), True)

        expected = {
            'answer_word': 'house',
            'masked_word': '****e',
            'previous_guesses': 'abcdef',
            'remaining_misses': 0
        }
        self.assertEqual(game, expected)
