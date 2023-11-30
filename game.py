"""
Peter Senyk
A01376857
"""
import game_loop
import start_game as start


def game():
    """
    runs the game
    """
    character = start.base_character()
    start.build_character(character)
    game_loop.level_one_loop(character)


def main():
    game()


if __name__ == "__main__":
    main()
