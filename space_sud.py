"""
Peter Senyk
A01376857
"""
import random as r
import actions
import boards
import checks
import pilot


def game():
    """
    runs the game
    """
    rows = 5
    columns = 5
    space = boards.make_space(rows, columns)
    player_stats = pilot.make_player()
    player_ship = pilot.select_ship(player_stats)
    character = {"Stats": player_stats, "Ship": player_ship, "Coordinates": {"X-coordinate": 0, "Y-coordinate": 0}}
    achieved_goal = False
    # there_is_a_challenger = False  #### MAY BE POSSIBLE TO REMOVE
    boards.describe_current_location(space, character)
    print(f"You're in the top-left hand corner of this quadrant [grid (0,0)], the goal is at the "
          f"bottom-right [gird ({rows - 1},{columns - 1})")
    while checks.is_alive(character) and not achieved_goal:
        player_action = input("Choose an action:\nS = Scan\nM = Move\n")
        if player_action.upper() == "M":
            actions.player_action_move(character, space)
        elif player_action.upper() == "S":
            actions.scan_space_grid(rows, columns, space, character)
        achieved_goal = checks.check_if_goal_attained(rows, columns, character)
    if character.get("HP") == 0:
        print("You died")


def guessing_game(character):
    """
    Challenges the character to a guessing game

    this function creates a random number between 1-5 inclusive, and asks the character to guess

    :param character: a dictionary of character location and HP
    :precondition: character must have an HP value of 1 or greater
    :post-condition: if the character guesses correctly they move on, if they guess wrong they loose 1 HP
    :return: a string based on whether the character guessed right or wrong
    """
    number_to_guess = r.randint(1, 5)
    player_guess = int(input("A challenger approaches... Test your luck and guess a number between 1 & 5 :\n"))
    if player_guess == number_to_guess:
        print("Lucky guess, this time...  HP=", character["Ship"]["HP"])
        return character["Ship"]["HP"]
    else:
        character["Ship"]["HP"] -= 1
        print("Wrong! the number was", number_to_guess, "Your HP =", character["Ship"]["HP"])
        return character["Ship"]["HP"]


def main():
    game()


if __name__ == "__main__":
    main()
