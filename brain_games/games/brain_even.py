from random import randint

from brain_games.game_engine import run_game


def brain_even():
    number = randint(1, 20)
    if number % 2 == 0:
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return number, correct_answer


def main():
    rule = 'Answer "yes" if the number is even, otherwise answer "no".'
    run_game(brain_even, rule)


if __name__ == "__main__":
    main()
