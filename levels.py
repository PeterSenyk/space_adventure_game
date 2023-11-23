import boards
import checks


def training_space():
    training_area = {
        (0, 0): 1, (1, 0): 2,
        (0, 1): 3, (1, 1): 2,
        (0, 2): 3, (1, 2): 3,
    }
    return training_area


def training_goal(character):
    if character["Stats"]["Accolades"]["Ships Destroyed"] >= 3:
        return True
    else:
        return False


def outlaw_space():
    outlaw_quadrabt = {
        (0, 0): 10, (1, 0): 6, (2, 0): 8,
        (0, 1): 5, (1, 1): 6, (2, 1): 60,
        (0, 2): 8, (1, 2): 7, (2, 2): 5
    }
    return outlaw_quadrabt


def outlaw_goal(character):
    ships_destroyed = character["Stats"]["Accolades"]["Ships Destroyed"]
    if ships_destroyed >= 6 and "Stolen shield capacitor" in character["Ship"]["Cargo"]:
        return True
    else:
        return False


def outer_quadrant_space():
    outer_quadrant = {
        (0, 0): 5, (1, 0): 5, (2, 0): 5, (3, 0): 5, (4, 0): 5,
        (0, 1): 5, (1, 1): 5, (2, 1): 5, (3, 1): 5, (4, 1): 5,
        (0, 2): 5, (1, 2): 5, (2, 2): 5, (3, 2): 5, (4, 2): 99,
        (0, 3): 5, (1, 3): 5, (2, 3): 5, (3, 3): 5, (4, 3): 5,
        (0, 4): 5, (1, 4): 5, (2, 4): 5, (3, 4): 9, (4, 4): 5,
    }
    return outer_quadrant


def random_space_goal(character, random_area):
    coordinates = checks.check_character_coordinates(character)
    if random_area[coordinates][0] == 99:
        return True
    else:
        return False
