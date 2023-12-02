import combat
import random as r
import events


def is_alive(ship):
    """
    Checks if the input ship is still alive.

    this function checks if the input ships HP value is above zero.

    :param ship: a dictionary of character location and HP.
    :precondition: character HP value must start above zero.
    :return: Boolean True of False.
    """
    if ship["Ship"]["HP"][0] <= 0:
        return False
    else:
        return True


def get_player_coordinates(character):
    """
    gets the players current coordinates.

    this function gets the players x and y coordinate from the character dictionary.

    :param character: a dictionary of the player character information.
    :return: the players coordinate as a tuple.
    """
    x_coordinate = character["Coordinates"]["X-coordinate"]
    y_coordinate = character["Coordinates"]["Y-coordinate"]
    coordinates = (x_coordinate, y_coordinate)
    return coordinates


def check_space_tile(character, space):
    """
    checks the current space tile and triggers an event.

    this function checks the players current space tile and triggers an event based on the number associated with it.
    :param character: a dictionary of the player character information.
    :param space: a dictionary of grid paired with a list containing an integer, description, and symbol.
    :post-condition: an event may be triggered for the player.
    """
    coordinates = get_player_coordinates(character)
    tile_event_number = space[coordinates][0]
    match tile_event_number:
        case 2:
            events.training_combat(character)
        case 3:
            events.avoid_debris(character)
        case 4:
            events.repair_outpost(character)
        case 5:
            if r.randint(1, 5) >= 4:
                combat.shield_recharge(character)
        case 6:
            events.asteroid_belt(character)
        case 7:
            # make a separate events !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            if r.randint(1, 10) >= 6:
                hostile_ship = combat.construct_medium_hostile_ship()
                combat.space_combat(character, hostile_ship)
            else:
                combat.shield_recharge(character)
        case 8:
            events.dark_side_of_moon(character)
        case 9:
            events.abandoned_space_station(character)
        case 10:
            events.bring_back_stolen_tech(character)
        case 11:
            events.pirate_combat(character)
        case 12:
            pass
        case 13:
            events.electro_magnetic_field(character)
        case 14:
            events.repair_outpost(character)
        case 15:
            events.space_cloud(character)
        case 16:
            events.shady_outpost(character)


def level_one_goal(character):
    """
    checks if the level one goal has been achieved

    this function checks if the player has completed level one
    :param character: a dictionary of the player character information.
    :return: a boolean True or False.
    """
    ships_destroyed = character["Stats"]["Accolades"]["Ships Destroyed"]
    debris_avoided = character["Stats"]["Accolades"]["Debris Avoided"]
    if ships_destroyed + debris_avoided == 4:
        return True
    else:
        return False


def level_two_goal(character):
    """
    checks if the level two goal has been achieved

    this function checks if the player has completed level one
    :param character: a dictionary of the player character information.
    :return: a boolean True or False
    """
    stolen_tech_returned = events.bring_back_stolen_tech(character)
    if stolen_tech_returned:
        return True
    else:
        return False


def level_three_goal(character):
    """
    checks if the level three goal has been achieved

    this function checks if the player has completed level one
    :param character: a dictionary of the player character information.
    :return: a boolean True or False
    """
    coordinates = get_player_coordinates(character)
    if coordinates == (0, 2):
        return True
    else:
        return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()
