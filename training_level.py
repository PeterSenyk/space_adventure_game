import combat
import game_checks
import actions
import random as r


def training_loop(character):
    training_goal = False
    space_tiles = training_space_tiles()
    space = training_space(space_tiles)
    while game_checks.is_alive(character) and not training_goal:
        actions.choose_an_action(character, space, 3, 2)
        check_training_tile(character, space)
        training_goal = check_if_trainee_goal_attained(character)


def training_space(space_tiles):
    training_area = {
        (0, 0): space_tiles[1], (1, 0): space_tiles[2],
        (0, 1): space_tiles[3], (1, 1): space_tiles[3],
        (0, 2): space_tiles[3], (1, 2): space_tiles[4],
    }
    return training_area


def training_space_tiles():
    space_tiles = {
        1: [1, "You're in the docking bay of the Arc-Corp training academy.", "AC1"],
        2: [2, "You're in an empty grid in the training zone, take a moment to breathe.", " - "],
        3: [3, "The training combat area is outlined by a ring of bright lights.", "[H]"],
        4: [4, "You see the landing pad at the end of the training area", "[_]"]
    }
    return space_tiles


def check_if_trainee_goal_attained(character):
    if character["Stats"]["Accolades"]["Ships Destroyed"] >= 2 and game_checks.get_player_coordinates(character) == (1, 2):
        print("Congrats, You've completed your training")
        return True


def construct_training_hostile():
    hostile_shield = r.randint(0, 1)
    hostile_hp = r.randint(1, 2)
    hostile_ship = {"Ship": {
        "Attack": r.randint(1, 2), "Movement": r.randint(1, 3), "HP": [hostile_hp, hostile_hp],
        "Targeting": r.randint(1, 3), "Shield": [hostile_shield, hostile_shield],
        "Cargo": []
    }}
    return hostile_ship


def check_training_tile(character, space):
    coordinates = game_checks.get_player_coordinates(character)
    tile_event_number = space[coordinates][0]
    if tile_event_number == 3:
        hostile_ship = construct_training_hostile()
        combat.space_combat(character, hostile_ship)
