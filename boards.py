import random as r


def describe_current_location(space, character):
    """
    Describes the current grid location

    this function describes the grid location and room to the player

    :param space: a dictionary of grid paired with a room description
    :param character: a dictionary of character location and HP
    :precondition: board must be a grid in a tuple, paired with a room description
    :precondition: character grid location must be in the board grids
    :post-condition: describes the location and room to the player
    :return: prints a string to the player
    """
    location_of_character = [character["Coordinates"].get("X-coordinate"), character["Coordinates"].get("Y-coordinate")]
    location_key = tuple(location_of_character)
    return print(f"You're current coordinates are: ", location_of_character, "\n", space[location_key][1])


def populate_space():
    """
    Makes descriptions of space tiles

    this function assigns room descriptions to the grid by using random numbers

    :post-condition: returns a random room description
    :return: a string
    """
    space_randomizer = r.randint(1, 10)
    if space_randomizer == 1:
        space_tile = [1, "You are in an asteroid belt, there are asteroids everywhere! Travel carefully."]
        return space_tile
    if space_randomizer == 2:
        space_tile = [2, "You are orbiting the dark side of a moon, You think of the legendary "
                         "ancient ballads of Pink Floyd."]
        return space_tile
    if space_randomizer == 3:
        space_tile = [3, "You come across a ship wreck, You start to wonder who could have caused this."]
        return space_tile
    if space_randomizer == 4:
        space_tile = [4, "You see the abandoned ArcCorp Space Station, You wonder what could have been left behind."]
        return space_tile
    if space_randomizer >= 5:
        space_tile = [5, "You are in the void of space, the sheer amount of nothingness is eerie."]
        return space_tile


def make_space(rows, columns):
    """
    Makes the board grid

    this function generates the board based on rows and columns, and assigns a room description to each grid

    :param rows: a positive integer
    :param columns: a positive integer
    :precondition: rows must be a positive integer equal to 1 or greater
    :precondition: column must be a positive integer equal to 1 or greater
    :post-condition: returns a board with grids and room descriptions
    :return: a dictionary
    """
    new_space = {}
    for row in range(rows):
        for column in range(columns):
            new_space[(column, row)] = populate_space()
    return new_space
