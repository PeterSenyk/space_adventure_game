import boards
import checks
import movement


def choose_an_action(character, space, rows, columns):
    """
    allows the player to perform an action in game

    this function prompts the player to choose an action

    :param character: a dictionary of the player character information
    :param space: a dictionary of grid paired with a list containing an integer, description, and symbol
    :param rows: a positive integer of rows on the current map
    :param columns: a positive integer of columns on the current map
    :precondition: character HP is above zero
    :post-condition: the game moves on to the chosen action
    """
    while True:
        player_action = input("Choose an action:\nS = Scan\nM = Move\nP = Check Personal Stats\nH = Help\n").upper()
        if player_action == "M":
            player_action_move(character, space)
            break
        elif player_action == "S":
            scan_space_grid(character, space, columns, rows)
            break
        elif player_action == "P":
            personal_stats(character)
            break
        elif player_action == "H":
            help_information()
            break
        else:
            print("Invalid action, please choose again.")


def player_action_move(character, space):
    """
    conducts player movement

    this function takes the player movement input and makes sure it is a valid move, if it is it adjusts the players
    coordinates in the game.

    :param character: a dictionary of the player character information
    :param space: a dictionary of grid paired with a list containing an integer, description, and symbol
    :precondition: character HP is above zero
    :post-condition: the characters coordinates are adjusted based on the input
    """
    valid_move = False
    while not valid_move:
        direction = movement.get_user_choice()
        valid_move = movement.validate_move(space, character, direction)
    boards.describe_current_location(space, character)
    checks.check_space_tile(character, space)


def scan_space_grid(character, space, columns, rows):
    """
    displays a grid map of the current quadrant

    this function prints out a grid map based on the symbols from the space dictionary

    :param character: a dictionary of the player character information
    :param space: a dictionary of grid paired with a list containing an integer, description, and symbol
    :param rows: a positive integer of rows on the current map
    :param columns: a positive integer of columns on the current map
    :post-condition: a grid map is printed to the user
    """
    for row in range(rows):
        for column in range(columns):
            if column == character["Coordinates"]["X-coordinate"] and row == character["Coordinates"]["Y-coordinate"]:
                print("\033[7m[X]\033[m", end="")
            else:
                tile_grid = (column, row)
                print(space[tile_grid][2], end="")
        print()


def personal_stats(character):
    """
    displays the characters stats

    this function displays the characters health, shields, and accolades.

    :param character: a dictionary of the player character information
    :post-condition: character stats are printed to the user
    """
    print(character["Stats"]["Title"], " ", end="")
    print(character["Stats"]["Name"])
    print(f"Accolades: {character['Stats']['Accolades']}")
    print("Your ship HP is", character["Ship"]["HP"][0], "out of", character["Ship"]["HP"][1])
    print("Your ship shield is", character["Ship"]["Shield"][0], "out of",
          character["Ship"]["Shield"][1])


def help_information():
    print("Type [M] for move.\n    This action allows you to choose a direction to move your character")
    print("Type [S] for scan.\n    This action displays a grid map of your current quadrant")
    print("Type [P] for personal stats.\n    This action displays you characters health shields and accolades")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
