import combat
import random as r

import events


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


def get_player_coordinates(character):
    x_coordinate = character["Coordinates"]["X-coordinate"]
    y_coordinate = character["Coordinates"]["Y-coordinate"]
    coordinates = (x_coordinate, y_coordinate)
    return coordinates


def check_space_tile(character, space):
    coordinates = get_player_coordinates(character)
    tile_event_number = space[coordinates][0]
    match tile_event_number:
        case 3:
            events.training_combat(character)
        case 4:
            events.avoid_debris(character)
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


    # explorer space > upgrade to exploration ships, high hp and shields, explore anomoly @
    # can either return with info > end game or pass through anomoly = endless space until game over ???





def level_one_goal(character):
    ships_destroyed = character["Stats"]["Accolades"]["Ships Destroyed"]
    debris_avoided = character["Stats"]["Accolades"]["Debris Avoided"]
    if ships_destroyed + debris_avoided == 4:
        return True


def level_two_goal(character):

    stolen_tech_returned = events.bring_back_stolen_tech(character)
    if stolen_tech_returned:
        return True
