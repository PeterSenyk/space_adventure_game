"""
Peter Senyk
A01376857
"""
import random as r


def game():
    """
    runs the game
    """
    rows = 5
    columns = 5
    board = make_board(rows, columns)
    player_stats = make_player()
    player_ship = select_ship(player_stats)
    character = {"Stats": player_stats, "Ship": player_ship}
    achieved_goal = False
    there_is_a_challenger = False
    describe_current_location(rows, columns, board, character)
    # print(f"You're in the bottom-left hand corner of a maze [grid (0,0)], the goal is at the "
    #       f"top-right [gird ({rows - 1},{columns - 1})")
    # while is_alive(character) and not achieved_goal:
    #     direction = get_user_choice()
    #     valid_move = validate_move(board, character, direction)
    #     if valid_move:
    #         move_character(character, direction)
    #         describe_current_location(rows, columns, board, character)
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
    if (character.get("X-coordinate"), character.get("Y-coordinate")) == (rows - 1, columns - 1):
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
    if direction.lower() == "n":
        character["Y-coordinate"] -= 1
    elif direction.lower() == "s":
        character["Y-coordinate"] += 1
    elif direction.lower() == "e":
        character["X-coordinate"] += 1
    elif direction.lower() == "w":
        character["X-coordinate"] -= 1
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


def validate_move(board, character, direction):
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
    temp_character = character.copy()
    move_calculator(temp_character, direction)
    temp_character_location = [(temp_character.get("X-coordinate")), (temp_character.get("Y-coordinate"))]
    if tuple(temp_character_location) in board.keys():
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
    direction_to_travel = input("Enter a direction to travel [n = north, e = east, s = south, w = west] :\n")
    return direction_to_travel


def print_board_grid(rows, columns, character):
    for row in range(rows):
        for column in range(columns):
            if column == character["X-coordinate"] and row == character["Y-coordinate"]:
                print(" X ", end="")
            elif column == columns - 1 and row == rows - 1:
                print(" $ ")
            else:
                print(" - ", end="")
        print()


def describe_current_location(rows, columns, board, character):
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
    location_of_character = [character.get("X-coordinate"), character.get("Y-coordinate")]
    location_key = tuple(location_of_character)
    print_board_grid(rows, columns, character)
    return print(f"You're current coordinates are: ", location_of_character, "\nYou see :", board.get(location_key))


def make_room():
    """
    Makes room descriptions

    this function assigns room descriptions to the grid by using random numbers

    :post-condition: returns a random room description
    :return: a string
    """
    room_randomizer = r.randint(1, 5)
    if room_randomizer == 1:
        return "You see brick walls in a dimly lit room, the smell is unbearable."
    if room_randomizer == 2:
        return "You see a four-way intersection, with timber walls lined with torches lighting the way."
    if room_randomizer == 3:
        return "You see a  courtyard full of shrubs and grass, the sun it out and shining."
    if room_randomizer == 4:
        return "You see a large kitchen, you could cook for 30 people in here, but maybe another time..."
    if room_randomizer == 5:
        return "You see large stone columns leading to the ceiling, there is a large banquet table in the middle."


def make_board(rows, columns):
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
    new_board = {}
    for column in range(rows):
        for row in range(columns):
            new_board[(column, row)] = make_room()
    return new_board


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
    player_stats = {"X-coordinate": 0, "Y-coordinate": 0, "Name": player_name}
    return player_stats


def main():
    game()


if __name__ == "__main__":
    main()
