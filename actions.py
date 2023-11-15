import movement
import combat
import boards
import checks


def player_action_move(character, space):
    direction = movement.get_user_choice()
    valid_move = movement.validate_move(space, character, direction)
    there_is_a_challenger = False
    if valid_move:
        movement.move_character(character, direction)
        boards.describe_current_location(space, character)
        there_is_a_challenger = checks.check_for_challenger()
    if there_is_a_challenger:
        combatant = combat.construct_challenger()
        combat.space_combat(character, combatant)


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
