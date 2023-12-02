import copy


def move_calculator(character, direction):
    """
    Calculates the characters move

    this function checks the players input and changes the grid location based on the direction

    :param character: a dictionary of the player character information.
    :param direction: a string value of "W" "A" "S" or "D"
    :precondition: direction must be a string of either "W" "A" "S" or "D"
    :post-condition: the players X or Y coordinates are changed based on input
    :raises ValueError: if direction is not one of the valid directions.
    """
    valid_directions = ["W", "A", "S", "D"]
    if direction.upper() not in valid_directions:
        raise ValueError(f"Invalid direction. Expected one {valid_directions}, got {direction}")
    if direction.upper() == "W":
        character["Coordinates"]["Y-coordinate"] -= 1
    elif direction.upper() == "S":
        character["Coordinates"]["Y-coordinate"] += 1
    elif direction.upper() == "D":
        character["Coordinates"]["X-coordinate"] += 1
    elif direction.upper() == "A":
        character["Coordinates"]["X-coordinate"] -= 1
    return character


def validate_move(space, character, direction):
    """
    Validates a character move

    this function compares the intended move to the game board

    :param character: a dictionary of the player character information
    :param space: a dictionary of grid paired with a list containing an integer, description, and symbol
    :param direction: a string value of "W" "A" "S" or "D"
    :precondition: direction must be a string of either "W" "A" "S" or "D"
    :post-condition: returns True if the move is in the game board, and False if the move is outside the board grid
    :return: Boolean True or False
    """
    temp_coordinates = copy.deepcopy(character)
    move_calculator(temp_coordinates, direction)
    if ((temp_coordinates["Coordinates"]["X-coordinate"], temp_coordinates["Coordinates"]["Y-coordinate"])
            in space.keys()):
        move_calculator(character, direction)
        return True
    else:
        print("Not a valid move")
        return False


def get_user_choice():
    """
    Asks the player for a direction to move

    this function asks the user which direction they want the character to move

    :return: a string value representing the direction the player wants to move
    """
    valid_directions = ["W", "A", "S", "D"]
    while True:
        direction_to_travel = input("Enter a direction to travel:\n[W] = Up\n[A] = Left\n[S] = Down\n[D] = Right\n")
        if direction_to_travel in valid_directions:
            return direction_to_travel
        else:
            print(f"Invalid input. Please choose one of {valid_directions}.")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
