from random import choice, randint

from brain_games.game_engine import run_game

operations = ["+", "-", "*"]


def brain_calc():
    number1 = randint(1, 10)
    number2 = randint(1, 10)
    operation = choice(operations)
    if operation == "+":
        correct_answer = str(number1 + number2)
    elif operation == "-":
        correct_answer = str(number1 - number2)
    else:
        correct_answer = str(number1 * number2)
    question = f"{number1} {operation} {number2}"
    return question, correct_answer


def main():
    rule = "What is the result of the expression?"
    run_game(brain_calc, rule)


if __name__ == "__main__":
    main()
