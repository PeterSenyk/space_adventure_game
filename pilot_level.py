import combat
import checks
import actions
import random as r


def pilot_loop(character):
    training_goal = False
    space_tiles = pilot_space_tiles()
    space = pilot_space(space_tiles)
    while game_checks.is_alive(character) and not training_goal:
        actions.choose_an_action(character, space, 3, 3)
        check_pilot_tile(character, space)
        training_goal = check_if_pilot_goal_attained(character)


def pilot_space(space_tiles):
    pilot_area = {
        (0, 0): space_tiles[10], (1, 0): space_tiles[6], (2, 0): space_tiles[8],
        (0, 1): space_tiles[5], (1, 1): space_tiles[6], (2, 1): space_tiles[60],
        (0, 2):space_tiles[8], (1, 2): space_tiles[7], (2, 2): space_tiles[5]
    }
    return pilot_area


def pilot_space_tiles():
    space_tiles = {
        5: [5, "You are in the void of space, the sheer amount of nothingness is eerie.", " - "],
        6: [6, "You are in an asteroid belt, there are asteroids everywhere! Travel carefully.", ":::"],
        7: [7, 'You are orbiting the dark side of a moon, You think of the legendary ancient ballads of '
               'Pink Floyd.', " o "],
        8: [8, "You come across a ship wreck, You start to wonder who could have caused this.", " # "],
        9: [9, "You see the abandoned ArcCorp Space Station, You wonder what could have been left behind.", " & "],
        10: [10, "You're in Arc-Corp station AD-V09 in the outskirts of the Out-land Quadrant", "AC9"],
        60: [60, "You find the crew responsible for the theft from the Arc-Corp R&D station", "<$>"],
    }
    return space_tiles


def check_if_pilot_goal_attained(character):
    if character["Stats"]["Accolades"]["Ships Destroyed"] >= 2 and game_checks.get_player_coordinates(character) == (1, 2):
        print("Thank you for retrieving the stolen materials")
        return True


def construct_medium_hostile():
    hostile_shield = r.randint(1, 3)
    hostile_hp = r.randint(2, 4)
    hostile_ship = {"Ship": {
        "Attack": r.randint(1, 3), "Movement": r.randint(2, 4), "HP": [hostile_hp, hostile_hp],
        "Targeting": r.randint(2, 4), "Shield": [hostile_shield, hostile_shield],
        "Cargo": []
    }}
    return hostile_ship


def check_pilot_tile(character, space):
    coordinates = game_checks.get_player_coordinates(character)
    tile_event_number = space[coordinates][0]
    if tile_event_number == 3:
        hostile_ship = construct_medium_hostile()
        combat.space_combat(character, hostile_ship)
