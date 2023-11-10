"""
Peter Senyk
A01376857
"""
import random as r

import boards

import pilot

import movement

import combat


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
    while is_alive(character) and not achieved_goal:
        player_action = input("Choose an action:\nS = Scan\nM = Move\n")
        if player_action.upper() == "M":
            player_action_move(character, space)
        elif player_action.upper() == "S":
            scan_space_grid(rows, columns, space, character)
        achieved_goal = check_if_goal_attained(rows, columns, character)
    if character.get("HP") == 0:
        print("You died")


def player_action_move(character, space):
    direction = movement.get_user_choice()
    valid_move = movement.validate_move(space, character, direction)
    there_is_a_challenger = False
    if valid_move:
        movement.move_character(character, direction)
        boards.describe_current_location(space, character)
        there_is_a_challenger = check_for_challenger()
    if there_is_a_challenger:
        # guessing_game(character)
        combatant = combat.construct_challenger()
        combat.space_combat(character, combatant)


def check_if_goal_attained(rows, columns, character):
    """
    Checks if the game has been won

    this function checks to see if the player had completed the goal of getting to the top right grid point

    :param rows: a positive integer
    :param columns: a positive integer
    :param character: a dictionary of character location and HP
    :precondition: achieved_goal must start as false
    :post-condition: The function will change the value of achieved_goal to True, ending the game
    :return: Boolean value True
    """
    if (character["Coordinates"]["X-coordinate"], character["Coordinates"]["Y-coordinate"]) == (rows - 1, columns - 1):
        print("congrats you win")
        return True


def is_alive(character):
    """
    Checks if the player is still alive

    this function checks if the characters HP value is above zero

    :param character: a dictionary of character location and HP
    :precondition: character HP value must start above zero
    :return: Boolean True of False
    """
    if character["Ship"]["HP"] <= 0:
        return False
    else:
        return True


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


def check_for_challenger():
    """
    Checks if there is a challenger at the character location

    this functions checks if there's a challenger by chance by using a random integer between 1-4 inclusive

    post-condition: if the random integer is 1, there will be a challenger at the character location
    :return: Boolean True
    """
    if r.randint(1, 4) == 1:
        return True


def scan_space_grid(rows, columns, space, character):
    for row in range(rows):
        for column in range(columns):
            if column == character["Coordinates"]["X-coordinate"] and row == character["Coordinates"]["Y-coordinate"]:
                print("[X]", end="")
            elif column == columns - 1 and row == rows - 1:
                print(" $ ")
            elif space[column, row][0] == 1:
                print(":::", end="")
            elif space[column, row][0] == 2:
                print(" o ", end="")
            elif space[column, row][0] == 3:
                print(" # ", end="")
            elif space[column, row][0] == 4:
                print(" & ", end="")
            elif space[column, row][0] >= 5:
                print(" - ", end="")
        print()


def main():
    game()


if __name__ == "__main__":
    main()
