"""
Peter Senyk
A01376857
"""
import start_game as start
import checks
import boards
import actions


def game():
    """
    runs the game
    """
    character = {"Stats": {"Title": ["Trainee", "Ace", "Captain"], "Name": "", "Accolades": []},
                 "Ship": {"Name": "", "Attack": 2, "Movement": 2, "HP": [5, 5], "Targeting": 4,
                          "Shield": [2, 2], "Cargo": []},
                 "Coordinates": {"X-coordinate": 0, "Y-coordinate": 0}}
    start.build_character(character)
    print(character)
    while character["Ship"]["HP"] > 0 and not checks.training_goal:
        space = boards.training_space()
        actions.choose_an_action(character, space, 2, 3)


def main():
    game()


if __name__ == "__main__":
    main()
