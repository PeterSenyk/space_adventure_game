"""
Peter Senyk
A01376857
"""
import game_loop
import start_game as start


def run_game():
    """
    runs the game
    """
    character = start.base_character()
    start.build_character(character)
    if not game_loop.level_one(character):
        print("Unfortunately you did not survive level one")
        return
    if not game_loop.level_two(character):
        print("Unfortunately you did not survive level two")
        return
    if not game_loop.level_three(character):
        print("Unfortunately you did not survive level three")
        return


def main():
    return


if __name__ == "__main__":
    main()
