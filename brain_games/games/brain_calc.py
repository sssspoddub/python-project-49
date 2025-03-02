from brain_games.scripts.main import greet
from brain_games.scripts.game_engine import get_answer, right_answer, wrong_answer
from random import randint, choice
from brain_games.cli import welcome_user

operations = ['*', '+', '-']


def calculator():
    name = welcome_user()
    right_answers_counter = 0
    while right_answers_counter < 3:
        number = randint(1, 10)
        number2 = randint(1, 10)
        operation = choice(operations)
        print('What is the result of the expression?')
        if operation == '*':
            answer = str(number * number2)
        elif operation == '+':
            answer = str(number + number2)
        else:
            answer = str(number - number2)
        print(f'Question: {number} {operation} {number2}')
        user_answer = get_answer()
        if user_answer == answer:
            right_answer()
            right_answers_counter += 1
        else:
            wrong_answer()
            right_answers_counter = 0
    print(f'Congratulations, {name}')


def main():
    greet()
    calculator()


if __name__ == "__main__":
    main()
