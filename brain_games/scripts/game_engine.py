from brain_games.scripts.main import greet
from brain_games.cli import welcome_user


def run_game():
    welcome_user()
    greet()


def right_answer():
    print('Correct!')


def get_answer():
    user_answer = input("Your answer: ")
    return user_answer


def wrong_answer():
    print('Wrong answer!')


def main():
    run_game()
