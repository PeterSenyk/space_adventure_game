"""
Peter Senyk
A01376857
"""
import start_game as start
import training_level


def game():
    """
    runs the game
    """
    character = start.base_character()
    start.build_character(character)
    training_level.training_loop(character)


def main():
    game()


if __name__ == "__main__":
    main()
