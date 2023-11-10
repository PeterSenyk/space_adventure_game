"""
Peter Senyk
A01376857
"""
import random as r

import boards as b


def game():
    """
    runs the game
    """
    rows = 5
    columns = 5
    space = make_space(rows, columns)
    player_stats = make_player()
    player_ship = select_ship(player_stats)
    character = {"Stats": player_stats, "Ship": player_ship, "Coordinates": {"X-coordinate": 0, "Y-coordinate": 0}}
    achieved_goal = False
    there_is_a_challenger = False
    describe_current_location(rows, columns, space, character)
    # print(f"You're in the top-left hand corner of a of this quadrant [grid (0,0)], the goal is at the "
    #       f"bottom-right [gird ({rows - 1},{columns - 1})")
    print(character)
    while is_alive(character) and not achieved_goal:
        direction = get_user_choice()
        valid_move = validate_move(space, character, direction)
        if valid_move:
            move_character(character, direction)
            describe_current_location(rows, columns, space, character)
    #         there_is_a_challenger = check_for_challenger()
    #     if there_is_a_challenger:
    #         guessing_game(character)
    #     achieved_goal = check_if_goal_attained(rows, columns, character)
    # if character.get("HP") == 0:
    #     print("You died")


def check_if_goal_attained(rows, columns, character):
    """
    Checks if the game has been won

    this function checks to see if the player had completed the goal of getting to the top right grid point

    :param rows: a positive integer
    :param columns: a positive integer
    :param character: a dictionary of character location and HP
    :precondition: achieved_goal must start as false
    :post-condition: The function will change the value of achieved_goal to True, ending the game
    :return: Boolean value True
    """
    if (character["Coordinates"]["X-coordinate"], character["Coordinates"]["Y-coordinate"]) == (rows - 1, columns - 1):
        print("congrats you win")
        return True


def is_alive(character):
    """
    Checks if the player is still alive

    this function checks if the characters HP value is above zero

    :param character: a dictionary of character location and HP
    :precondition: character HP value must start above zero
    :return: Boolean True of False
    """
    if character["Ship"]["HP"] <= 0:
        return False
    else:
        return True


# def guessing_game(character):
#     """
#     Challenges the character to a guessing game
#
#     this function creates a random number between 1-5 inclusive, and asks the character to guess
#
#     :param character: a dictionary of character location and HP
#     :precondition: character must have an HP value of 1 or greater
#     :post-condition: if the character guesses correctly they move on, if they guess wrong they loose 1 HP
#     :return: a string based on whether the character guessed right or wrong
#     """
#     number_to_guess = r.randint(1, 5)
#     player_guess = int(input("A challenger approaches... Test your luck and guess a number between 1 & 5 :\n"))
#     if player_guess == number_to_guess:
#         print("Lucky guess, this time...  HP=", character.get("HP"))
#         return character["HP"]
#     else:
#         character["HP"] -= 1
#         print("Wrong! the number was", number_to_guess, "Your HP =", character.get("HP"))
#         return character["HP"]


# def check_for_challenger():
#     """
#     Checks if there is a challenger at the character location
#
#     this functions checks if there's a challenger by chance by using a random integer between 1-4 inclusive
#
#     post-condition: if the random integer is 1, there will be a challenger at the character location
#     :return: Boolean True
#     """
#     if r.randint(1, 4) == 1:
#         return True


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

    :param board: a dictionary of grid paired with a room description
    :param character: a dictionary of character location and HP
    :param direction: a string
    :precondition: direction must be a string value of either "n", "s", "e", or "w"
    :post-condition: returns True if the move is in the game board, and False if the move is outside the board grid
    :return: Boolean True or False
    """
    temp_coordinates = copy.deepcopy(character)
    move_calculator(temp_coordinates, direction)
    print(temp_coordinates)
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


def scan_space_grid(rows, columns, space, character):
    for row in range(rows):
        for column in range(columns):
            if column == character["Coordinates"]["X-coordinate"] and row == character["Coordinates"]["Y-coordinate"]:
                print("[X]", end="")
            elif column == columns - 1 and row == rows - 1:
                print(" $ ")
            elif space[column, row][0] == 1:
                print(":::", end="")
            elif space[column, row][0] == 2:
                print(" o ", end="")
            elif space[column, row][0] == 3:
                print(" # ", end="")
            elif space[column, row][0] == 4:
                print(" & ", end="")
            elif space[column, row][0] >= 5:
                print(" - ", end="")
        print()


def describe_current_location(rows, columns, space, character):
    """
    Describes the current grid location

    this function describes the grid location and room to the player

    :param rows:
    :param columns:
    :param board: a dictionary of grid paired with a room description
    :param character: a dictionary of character location and HP
    :precondition: board must be a grid in a tuple, paired with a room description
    :precondition: character grid location must be in the board grids
    :post-condition: describes the location and room to the player
    :return: prints a string to the player
    """
    location_of_character = [character["Coordinates"].get("X-coordinate"), character["Coordinates"].get("Y-coordinate")]
    location_key = tuple(location_of_character)
    scan_space_grid(rows, columns, space, character)
    return print(f"You're current coordinates are: ", location_of_character, "\n", space[location_key][1])


def populate_space():
    """
    Makes space descriptions

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


def select_ship(player_stats):
    """
    Selects a ship for the game

    this funtion lets the player select their ship for the game

    :return:
    """
    print(player_stats["Name"], "Here are your choices for a ship")
    print("ANVIL ARROW: Attack [1], Movement [3], HP [5] Cargo Space [2]")
    print("AEGIS GLADIUS: Attack [2], Movement [2], HP [5], Cargo Space [2]")
    print("DRAKE BUCCANEER: Attack [3], Movement [2], HP [4], Cargo Space [2]")
    new_ship = input("Please select A for the ANVIL ARROW, G for the AEGIS GLADIUS, or B for the DRAKE BUCCANEER\n")
    if new_ship.upper() == "A":
        return {"Ship": "ANVIL ARROW", "Attack": 1, "Movement": 3, "HP": 5, "Cargo": 2}
    if new_ship.upper() == "G":
        return {"Ship": "AEGIS GLADIUS", "Attack": 2, "Movement": 2, "HP": 5, "Cargo": 2}
    if new_ship.upper() == "B":
        return {"Ship": "DRAKE BUCCANEER", "Attack": 3, "Movement": 2, "HP": 4, "Cargo": 2}


def make_player():
    """
    Makes a character

    this function makes a character based on starting stats

    :param starting_stats:
    :precondition: starting_stats is a list of integers in order of X-coordinate, Y-coordinate, then HP
    :post-condition: a character dictionary is completed with starting coordinates and HP
    :return: a dictionary
    """
    player_last_name = input("Please type your last name\n")
    player_name = "Captain " + player_last_name
    print("Congratulations", player_name, "on graduating the Space Academy at the top of your class\n")
    player_stats = {"Name": player_name}
    return player_stats


def main():
    game()


if __name__ == "__main__":
    main()
