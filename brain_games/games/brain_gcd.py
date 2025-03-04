from math import gcd
from random import randint

from brain_games.game_engine import run_game


def gcd_game():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    question = f"{number1} {number2}"
    correct_answer = str(gcd(number1, number2))
    return question, correct_answer


def main():
    rule = "Find the greatest common divisor of given numbers."
    run_game(gcd_game, rule)


if __name__ == "__main__":
    main()
