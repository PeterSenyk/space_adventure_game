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
