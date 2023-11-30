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

    if tile_event_number == 4:
        print("Try to dodge the debris if you can")
    pass


def level_one_goal(character):
    if character["Stats"]["Accolades"]["Ships Destroyed"] == 3:
        return True
