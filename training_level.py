from code_to_rework import checks
import actions

def training_loop(character):
    training_goal = False
    space_tiles = training_space_tiles()
    space = training_space(space_tiles)
    while checks.is_alive(character) and not training_goal:
        actions.choose_an_action(character, space, 2, 3)
    pass


def training_space(space_tiles):
    training_area = {
        (0, 0): space_tiles[1], (1, 0): space_tiles[2],
        (0, 1): space_tiles[3], (1, 1): space_tiles[2],
        (0, 2): space_tiles[3], (1, 2): space_tiles[3],
    }
    return training_area


def training_space_tiles():
    space_tiles = {
        1: [1, "You're in the docking bay of the Arc-Corp training academy.", "AC1"],
        2: [2, "You're in an empty grid in the training zone, take a moment to breathe.", " - "],
        3: [3, "The training combat area is outlined by a ring of bright lights.", "[H]"]
    }
    return space_tiles


def check_if_trainee_goal_attained(character):
    if character["Accolades"]["Ships Destroyed"] == 2:
        print("Congrats, You've completed your training")
        return True
