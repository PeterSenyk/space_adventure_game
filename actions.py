import movement
import combat
import boards
from code_to_rework import checks


def choose_an_action(character, space, rows, columns):
    player_action = input("Choose an action:\nS = Scan\nM = Move\nP = Check Personal Stats\n")
    if player_action.upper() == "M":
        player_action_move(character, space)
    elif player_action.upper() == "S":
        scan_space_grid(rows, columns, space, character)
    elif player_action.upper() == "P":
        personal_stats(character)


def player_action_move(character, space):
    direction = movement.get_user_choice()
    valid_move = movement.validate_move(space, character, direction)
    if not valid_move:
        return
    movement.move_character(character, direction)
    boards.describe_current_location(space, character)
    # if there_is_a_challenger:
    #     combatant = combat.construct_hostile_ship()
    #     combat.space_combat(character, combatant)
    # else:
    #     combat.shield_recharge(character)


def scan_space_grid(rows, columns, space, character):
    for row in range(rows):
        for column in range(columns):
            if column == character["Coordinates"]["X-coordinate"] and row == character["Coordinates"]["Y-coordinate"]:
                print("[X]", end="")
            elif column == columns - 1 and row == rows - 1:
                print(" $ ")
            else:
                tile_number = space[(row, column)][0]
                tile_desc = boards.space_tiles_dict()
                print(tile_desc[tile_number][2], end="")
        print()


def personal_stats(character):
    print(character["Stats"])
