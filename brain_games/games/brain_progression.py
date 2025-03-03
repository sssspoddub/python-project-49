from random import randint, choice
from brain_games.game_engine import run_game


def brain_progression():
    length = randint(5, 10)
    start = randint(1, 20)
    step = randint(2, 10)

    progression = []
    for i in range(length):
        progression.append(str(start + i * step))

    hidden_number = choice(progression)
    correct_answer = hidden_number
    progression[progression.index(hidden_number)] = ".."

    question = " ".join(progression)
    return question, correct_answer


def main():
    rule = "What number is missing in the progression?"
    run_game(brain_progression, rule)


if __name__ == "__main__":
    main()
