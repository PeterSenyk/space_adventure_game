"""
Peter Senyk
A01376857
"""
import actions
import boards
import checks
import pilot


def game():
    """
    runs the game
    """
    rows = 6
    columns = 6
    space = boards.make_space(rows, columns)
    player_stats = pilot.make_player()
    player_ship = pilot.select_ship(player_stats)
    character = {"Stats": player_stats, "Ship": player_ship, "Coordinates": {"X-coordinate": 0, "Y-coordinate": 0}}
    achieved_goal = False
    # there_is_a_challenger = False  #### MAY BE POSSIBLE TO REMOVE
    boards.describe_current_location(space, character)
    print(f"You're in the top-left hand corner of this quadrant [grid (0,0)], the goal is at the "
          f"bottom-right [gird ({rows - 1},{columns - 1})")
    while checks.is_alive(character) and not achieved_goal:
        player_action = input("Choose an action:\nS = Scan\nM = Move\n")
        if player_action.upper() == "M":
            actions.player_action_move(character, space)
        elif player_action.upper() == "S":
            actions.scan_space_grid(rows, columns, space, character)
        achieved_goal = checks.check_if_goal_attained(rows, columns, character)
    if character.get("HP") == 0:
        print("You died")


def main():
    game()


if __name__ == "__main__":
    main()
