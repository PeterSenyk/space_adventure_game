import boards
import checks
import movement


def choose_an_action(character, space, rows, columns):
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
    direction = movement.get_user_choice()
    valid_move = movement.validate_move(space, character, direction)
    if not valid_move:
        return
    else:
        boards.describe_current_location(space, character)
        checks.check_space_tile(character, space)


def scan_space_grid(character, space, columns, rows):
    for row in range(rows):
        for column in range(columns):
            if column == character["Coordinates"]["X-coordinate"] and row == character["Coordinates"]["Y-coordinate"]:
                print("\033[7m[X]\033[m", end="")
            else:
                tile_grid = (column, row)
                print(space[tile_grid][2], end="")
        print()


def personal_stats(character):
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
