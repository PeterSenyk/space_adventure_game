"""
Peter Senyk
A01376857
"""
import levels
import start_game as start


def game():
    """
    runs the game
    """
    character = start.base_character()
    start.build_character(character)
    levels.training_level(character)


def main():
    game()


if __name__ == "__main__":
    main()
