from random import randint

from brain_games.game_engine import run_game

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_game():
    number = randint(1, 100)
    if is_prime(number):
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return str(number), correct_answer


def main():
    run_game(get_game, RULE)


if __name__ == "__main__":
    main()
