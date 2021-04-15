import pytest
from gallows import Game, MAX_PENALTIES


@pytest.fixture
def word_empty():
    return Game()


@pytest.fixture(params=['SkIlL', 'skill', 'SKILL'])
def game_loose(request):
    game = Game(request.param)
    game._penalties = MAX_PENALTIES - 1
    return game


@pytest.fixture(params=['FaCtOrY', 'factory', 'FACTORY'])
def game_win(request):
    game = Game(request.param)
    game._guessed_letters = {'F', 'C', 'T', 'O', 'R', 'Y'}
    return game


@pytest.fixture(params=['akz', 'aZzaazKka', 'swAchkdlZd'])
def word(request):
    return Game(request.param)


@pytest.fixture(params=[{'B', 'R', 'Y'}, {'A', 'B', 'S', 'R', 'Y', 'Z'}])
def word_repetitive(request):
    game = Game()
    game._guessed_letters = request.param
    return game
