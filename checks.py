import random as r
import events
import combat


def check_if_trainee_goal_attained(character, training_space):
    if check_character_coordinates(character) == (0, 0) and character["Accolades"]["Ships Destroyed"] == 3:
        print("Congrats, You've completed your training")


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
    else:
        return False


def is_alive(ship):
    """
    Checks if the player is still alive

    this function checks if the characters HP value is above zero

    :param ship: a dictionary of character location and HP
    :precondition: character HP value must start above zero
    :return: Boolean True of False
    """
    if ship["Ship"]["HP"] <= 0:
        return False
    else:
        return True


def check_for_challenger():
    """
    Checks if there is a challenger at the character location

    this functions checks if there's a challenger by chance by using a random integer between 1-4 inclusive

    post-condition: if the random integer is 1, there will be a challenger at the character location
    :return: Boolean True
    """
    if r.randint(1, 4) == 1:
        return True


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



