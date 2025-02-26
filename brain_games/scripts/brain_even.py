from random import randint

import prompt

from brain_games.scripts.main import greet


def is_even(number: int):
    return number % 2 == 0


def brain_even():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    correct_answer_counter = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while correct_answer_counter < 3:
        random_number = randint(1, 20)
        print(f'Question: {random_number}')
        user_answer = input("Your answer: ")
        if is_even(random_number) and user_answer.lower() == "yes":
            print("Correct!")
            correct_answer_counter += 1
        elif not is_even(random_number) and user_answer.lower() == "no":
            print("Correct!")
            correct_answer_counter += 1
        else:
            print("Wrong answer!")
            correct_answer_counter = 0
    print(f'Congratulations, {name}!')


def main():
    greet()
    brain_even()


if __name__ == "__main__":
    main()
