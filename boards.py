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
    :return: prints a string to the player of their current coordinates and the tile description
    """
    location_of_character = [character["Coordinates"]["X-coordinate"], character["Coordinates"]["Y-coordinate"]]
    location_key = tuple(location_of_character)
    print(f"Your current coordinates are: {location_of_character}\n{space[location_key][1]}")


def make_space(rows, columns, min_event, max_event):
    """
    Makes the board grid

    this function generates the board based on rows and columns, and assigns a room description to each grid


    :param rows: a positive integer
    :param columns: a positive integer
    :param max_event: a positive integer detailing the minimum event number that can be called for a space tile
    :param min_event:a positive integer detailing the maximum event number that can be called for a space tile
    :precondition: rows must be a positive integer equal to 1 or greater
    :precondition: column must be a positive integer equal to 1 or greater
    :post-condition: returns a board with grids and room descriptions
    :return: a dictionary
    """
    new_space = {}
    tile_dict = space_tiles_dict()
    for row in range(rows):
        for column in range(columns):
            space_tile = r.randint(min_event, max_event)
            new_space[(column, row)] = tile_dict[space_tile]
    return new_space


def space_tiles_dict():
    """
    returns a dictionary of events for space tiles.

    this function returns a dictionary of space tiles paired with an event number, tile description, and symbol.

    :return: a dictionary
    """
    space_tiles = {
        0: [0, "You're in the docking bay of the Arc-Corp training academy.", "AC1"],
        1: [1, "You're in an empty grid in the training zone, take a moment to breathe.", "\033[40m - \033[m"],
        2: [2, "The training combat area is outlined by a ring of bright lights.", "\033[31m\033[40m[H]\033[m"],
        3: [3, "You see lots of debris ahead of you, watch out !", "\033[35m\033[40mxXx\033[m"],
        4: [4, "You come across a repair outpost", "\033[32m\033[40m[+]\033[m"],
        5: [5, "You are in the void of space, the sheer amount of nothingness is eerie.", "\033[37m\033[40m - \033[m"],
        6: [6, "You are in an asteroid belt, there are asteroids everywhere! Travel carefully.",
            "\033[37m\033[40m:::\033[m"],
        7: [7, 'You are orbiting the dark side of a moon, You think of the legendary ancient ballads of '
               'Pink Floyd.', "\033[35m\033[40m( )\033[m"],
        8: [8, "You come across a ship wreck, You start to wonder who could have caused "
               "this.", "\033[31m\033[40m # \033[m"],
        9: [9, "You see an abandoned ArcCorp Space Station, You wonder what could have been left behind.",
            "\033[33m\033[40m & \033[m"],
        10: [10, "You've entered a region filled with the colorful gases and dust of a distant nebula,"
                 " a stellar nursery where stars are born.", "\033[36m\033[40m*~*\033[m"],
        11: [5, "You are in the void of space, the sheer amount of nothingness is eerie.", "\033[37m\033[40m - \033[m"],
        12: [5, "You are in the void of space, the sheer amount of nothingness is eerie.", "\033[37m\033[40m - \033[m"],
        13: [13, "Your sensors detect an electro-magnetic field, read-outs are showing that your shields have lost "
                 "all power.", "\033[33m\033[40m~*~\033[m"],
        14: [9, "You see an abandoned ArcCorp Space Station, You wonder what could have been left behind.",
             "\033[33m\033[40m & \033[m"],
        15: [15, "You find yourself in a pocket of gas in space.", "\033[36m\033[40m{G}\033[m"],
        16: [16, "You come across a shady looking outpost.", "\033[35m\033[40m[¿]\033[m"],
        # 59: [59, "You see Arc-Corp Station 7, Return the stolen tech here.", "\033[32m\033[40m[AC7]\033[m"],
        60: [60, "You find the crew responsible for the theft from the Arc-Corp R&D station.",
             "\033[31m\033[40m<$>\033[m"],
    }
    return space_tiles


def main():
    return


if __name__ == "__main__":
    main()
