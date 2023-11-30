"""
These functions are not currently being used
"""

def game(): # backup for re-work
    """
    runs the game
    """
    rows = 6
    columns = 6
    space = boards.make_space(rows, columns)
    player_stats = pilot.make_player()
    player_ship = pilot.select_ship(player_stats)
    character = {"Stats": player_stats, "Ship": player_ship, "Coordinates": {"X-coordinate": 0, "Y-coordinate": 0}}
    achieved_goal = False
    boards.describe_current_location(space, character)
    print(f"You're in the top-left hand corner of this quadrant [grid (0,0)], the goal is at the "
          f"bottom-right [gird ({rows - 1},{columns - 1})")
    while checks.is_alive(character) and not achieved_goal:
        actions.choose_an_action(character, space, rows, columns)
        achieved_goal = checks.check_if_goal_attained(rows, columns, character)
    if character["HP"] <= 0:
        print("You died\nGAME OVER")


# Use this for player name ?
def capitalize_name(name):
    if len(name.strip()) == 0:
        raise ValueError('No empty names allowed!')
    else:
        return name.title()


def makename():
    capitalized_name = capitalize_name("nicole paige brookes")
    print(capitalized_name)

    try:
        another_capitalized_name = capitalize_name("")
    except ValueError as e:
        print(e)
    else:
        print(another_capitalized_name)


# REWORK ATTACK ---- break into atomic function, add Shields, Miss
# def attack(character, challenger):
#     if compare_ships(character, challenger):
#         challenger["HP"] -= character["Ship"]["Attack"]
#         print("You attack the enemy\ntheir HP= ", challenger["HP"])
#         if challenger["HP"] < 1:
#             print("You destroyed the hostile ship")
#             # character["Stats"]["Ships Destroyed"] += 1  #### add this later ?
#             return
#         else:
#             character["Ship"]["HP"] -= challenger["Attack"]
#             print("The enemy ship attacks!\nYour HP= ", character["Ship"]["HP"])
#             return
#     else:
#         character["Ship"]["HP"] -= challenger["Attack"]
#         print("The enemy ship attacks!\nYour HP= ", character["Ship"]["HP"])
#         if not is_alive(character):
#             print("You have been destroyed")
#             return
#         else:
#             challenger["HP"] -= character["Ship"]["Attack"]
#             print("You attack the enemy!\ntheir HP= ", challenger["HP"])
#             if challenger["HP"] < 1:
#                 print("You destroyed the hostile ship")
#                 # character["Stats"]["Ships Destroyed"] += 1  #### add this later ?
#                 return

import random as r
import events


# def check_if_goal_attained(rows, columns, character):
#     """
#     Checks if the game has been won
#
#     this function checks to see if the player had completed the goal of getting to the top right grid point
#
#     :param rows: a positive integer
#     :param columns: a positive integer
#     :param character: a dictionary of character location and HP
#     :precondition: achieved_goal must start as false
#     :post-condition: The function will change the value of achieved_goal to True, ending the game
#     :return: Boolean value True
#     """
#     if (character["Coordinates"]["X-coordinate"], character["Coordinates"]["Y-coordinate"]) == (rows - 1, columns - 1):
#         print("congrats you win")
#         return True
#     else:
#         return False


def is_alive(ship):
    """
    Checks if the player is still alive

    this function checks if the characters HP value is above zero

    :param ship: a dictionary of character location and HP
    :precondition: character HP value must start above zero
    :return: Boolean True of False
    """
    if ship["Ship"]["HP"][0] <= 0:
        return False
    else:
        return True


# def check_for_challenger():
#     """
#     Checks if there is a challenger at the character location
#
#     this functions checks if there's a challenger by chance by using a random integer between 1-4 inclusive
#
#     post-condition: if the random integer is 1, there will be a challenger at the character location
#     :return: Boolean True
#     """
#     if r.randint(1, 4) == 1:
#         return True


def check_character_coordinates(character):
    """
    Checks the characters coordinates


    :param character: character dictionary must be created
    :precondition:
    :post-condition: character coordinates are simplified into a tuple
    :return: 2 integers
    """
    character_coordinates = (character["Coordinates"]["X-coordinate"], character["Coordinates"]["Y-coordinate"])
    return character_coordinates


def check_for_event(character, space_tile):
    coordinates = check_character_coordinates(character)
    event_chance = r.randint(1, 4)
    if space_tile[coordinates][0] == 6:
        if event_chance <= 2:
            events.asteroid_belt(character)
        if event_chance == 3:
            combatant = combat.construct_hostile_ship()
            combat.space_combat(character, combatant)


def training_goal(character):
    if character["Stats"]["Accolades"]["Ships Destroyed"] >= 3:
        return True
    else:
        return False
