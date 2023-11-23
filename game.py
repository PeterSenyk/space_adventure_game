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
    boards.describe_current_location(space, character)
    print(f"You're in the top-left hand corner of this quadrant [grid (0,0)], the goal is at the "
          f"bottom-right [gird ({rows - 1},{columns - 1})")
    while checks.is_alive(character) and not achieved_goal:
        actions.choose_an_action(character, space, rows, columns)
        achieved_goal = checks.check_if_goal_attained(rows, columns, character)
    if character["HP"] <= 0:
        print("You died\nGAME OVER")


def main():
    game()


if __name__ == "__main__":
    main()
