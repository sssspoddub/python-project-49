from brain_games.games.brain_gcd import brain_gcd
from brain_games.game_engine import run_game

def main():
    rule = "Find the greatest common divisor of given numbers."
    run_game(brain_gcd, rule)

if __name__ == "__main__":
    main()
