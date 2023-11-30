import combat
import random as r


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
    if tile_event_number == 3:
        print("You see a training hostile")
        hostile_ship = combat.construct_training_hostile()
        combat.space_combat(character, hostile_ship)
    if tile_event_number == 4:
        print("Try to dodge the debris if you can")
        correct_route = r.randint(1, 3)
        choice = int(input("Choose a heading to avoid the debris, your choices are:\n [1] [2] or [3]\n"))
        if choice == correct_route:
            print("You avoided the debris !")
            combat.shield_recharge(character)
            if "Debris Avoided" not in character:
                character["Stats"]["Accolades"]["Debris Avoided"] = 1
            else:
                character["Stats"]["Accolades"]["Debris Avoided"] += 1
        else:
            print("You collide with the debris")
            combat.deal_other_damage(character, 1)
    pass


def level_one_goal(character):
    ships_destroyed = character["Stats"]["Accolades"]["Ships Destroyed"]
    debris_avoided = character["Stats"]["Accolades"]["Debris Avoided"]
    if ships_destroyed + debris_avoided == 4:
        return True
