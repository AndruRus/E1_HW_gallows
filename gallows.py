import random

MAX_PENALTIES = 4
LETTER_SPACE = '_'
WORDS = [
    'skillfactory',
    'testing',
    'blackbox',
    'pytest',
    'unittest',
    'coverage',
    ]

# game statuses
WIN = 'WIN'
LOOSE = 'LOOSE'
GUESSED = 'GUESSED'
WRONG = 'WRONG_LETTER'
NOT_SINGLE = 'NOT_SINGLE_LETTER'
REPETITIVE = 'REPETITIVE_LETTER'


class Game:
    def __init__(self, word=''):
        self.ended = False
        self._word = word.upper()
        self._word_letters = set(self._word)
        self._guessed_letters = set()
        self._penalties = 0
        self._status = None

    def process_letter(self, letter):
        letter = letter.upper()
        self._check_letter(letter)
        if self._status == GUESSED:
            self._guessed_letters.add(letter)
            self._check_win()
        elif self._status == WRONG:
            self._penalties += 1
            self._check_penalties()

        self._print_status_message()
        self.print_game_string()

    def _check_letter(self, letter):
        if len(letter) != 1:
            self._status = NOT_SINGLE
        elif letter in self._guessed_letters:
            self._status = REPETITIVE
        elif letter in self._word:
            self._status = GUESSED
        else:
            self._status = WRONG

    def _check_penalties(self):
        if self._penalties >= MAX_PENALTIES:
            self._status = LOOSE
            self.ended = True

    def _check_win(self):
        if self._guessed_letters == self._word_letters:
            self._status = WIN
            self.ended = True

    def _print_status_message(self):
        if self._status == WIN:
            print('Вы выиграли!')
        elif self._status == LOOSE:
            print(f'Попыток больше нет — {MAX_PENALTIES}. Вы проиграли!')
        elif self._status == WRONG:
            print('Вы ошиблись буквой')
            print(f'Количество попыток: {MAX_PENALTIES - self._penalties}')
        elif self._status == REPETITIVE:
            print('Вы уже использовали эту букву')
        elif self._status == NOT_SINGLE:
            print('Введите букву')

    def print_game_string(self):
        game_string = [letter if (letter in self._guessed_letters) else LETTER_SPACE for letter in self._word]
        print(*game_string)


def print_greeting():
    print('Игра «Виселица»! Отгадайте все буквы в слове.')
    print('Вы можете ввести только одну букву за попытку.')
    print('За неправельную букву Вы получаете штрафной балл.')
    print(f'Игра закончится если вы наберёте {MAX_PENALTIES} штрафных баллов.')
    print('Желаем удачи!')


def main():
    word = random.choice(WORDS)
    game = Game(word)
    print_greeting()
    game.print_game_string()
    while not game.ended:
        letter = input('\nУгадайте букву: ')
        game.process_letter(letter)


if __name__ == '__main__':
    main()
