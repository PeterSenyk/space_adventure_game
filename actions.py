import checks
import movement
# import combat
# import boards
# from code_to_rework import checks


def choose_an_action(character, space, rows, columns):
    player_action = input("Choose an action:\nS = Scan\nM = Move\nP = Check Personal Stats\n")
    if player_action.upper() == "M":
        player_action_move(character, space)
    elif player_action.upper() == "S":
        scan_space_grid(character, space, columns, rows)
    elif player_action.upper() == "P":
        personal_stats(character)


def player_action_move(character, space):
    direction = movement.get_user_choice()
    valid_move = movement.validate_move(space, character, direction)
    if not valid_move:
        return
    checks.check_space_tile(character, space)


def scan_space_grid(character, space, columns, rows):
    for row in range(rows):
        for column in range(columns):
            if column == character["Coordinates"]["X-coordinate"] and row == character["Coordinates"]["Y-coordinate"]:
                print("[X]", end="")
            else:
                tile_grid = (column, row)
                print(space[tile_grid][2], end="")
        print()


def personal_stats(character):
    print(character["Stats"]["Title"]," ", end="")
    print(character["Stats"]["Name"])
    print(f"Accolades: {character['Stats']['Accolades']}")

