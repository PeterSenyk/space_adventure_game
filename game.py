"""
Peter Senyk
A01376857
"""
import game_loop
import start_game as start
import json


def run_game():
    """
    runs the game
    """
    character = start.base_character()
    start.build_character(character)
    # game_loop.level_one(character)
    # game_loop.level_two(character)
    game_loop.level_three(character)


def main():
    run_game()


if __name__ == "__main__":
    main()
