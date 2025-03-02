from brain_games.cli import welcome_user


def run_game(game, game_rule):
    name = welcome_user()
    print(game_rule)
    right_answers_counter = 0

    while right_answers_counter < 3:
        question, correct_answer = game()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")

        if user_answer == correct_answer:
            print("Correct!")
            right_answers_counter += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
