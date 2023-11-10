import copy

def move_calculator(character, direction):
    """
    Calculates the characters move

    this function checks the players input and changes the grid location based on the direction

    :param character: a dictionary of character location and HP
    :param direction: a string value of "n" "s" "e" or "w"
    :precondition: move must be a string value of either "n", "s", "e", or "w"
    :post-condition: the players X or Y coordinates are changed based on input
    """
    if direction.lower() == "w":
        character["Coordinates"]["Y-coordinate"] -= 1
    elif direction.lower() == "s":
        character["Coordinates"]["Y-coordinate"] += 1
    elif direction.lower() == "d":
        character["Coordinates"]["X-coordinate"] += 1
    elif direction.lower() == "a":
        character["Coordinates"]["X-coordinate"] -= 1
    return character


def move_character(character, direction):
    """
    Changes the characters X or Y coordinate

    this function changes the characters X or Y coordinate based on the input

    :param character: a dictionary of character location and HP
    :param direction: a string
    :precondition: direction must be a string value of either "n", "s", "e", or "w"
    :precondition: the move is validated prior to changing the character coordinates
    :post-condition: the characters coordinates are changed
    """
    move_calculator(character, direction)


def validate_move(space, character, direction):
    """
    Validates a character move

    this function compares the intended move to the game board

    :param space: a dictionary of grid paired with a room description
    :param character: a dictionary of character location and HP
    :param direction: a string
    :precondition: direction must be a string value of either "n", "s", "e", or "w"
    :post-condition: returns True if the move is in the game board, and False if the move is outside the board grid
    :return: Boolean True or False
    """
    temp_coordinates = copy.deepcopy(character)
    move_calculator(temp_coordinates, direction)
    if ((temp_coordinates["Coordinates"]["X-coordinate"], temp_coordinates["Coordinates"]["Y-coordinate"])
            in space.keys()):
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
    direction_to_travel = input("Enter a direction to travel [w = Up, a = Left, s = Down, d = Right] :\n")
    return direction_to_travel