import random as r
from checks import is_alive


def combat_order_of_events():
    construct_challenger()
    compare_ships()
    space_combat()


def construct_hostile_ship():
    hostile_ship = {"Ship": {
        "Attack": r.randint(1, 2), "Movement": r.randint(1, 3), "HP": r.randint(1, 3),
        "Targeting": r.randint(1, 4), "Shield": r.randint(0, 1),
        "Cargo": r.randint(0, 1)
    }}
    return hostile_ship


def space_combat(character, challenger):
    print("You come across a hostile ship")
    while is_alive(character) and challenger["HP"] > 0:
        # print(character["Ship"]["HP"])
        # print(challenger["HP"])
        player_action = input("Choose an action\nA = Attack\nR = Run\nD = Dodge\n")
        if player_action.upper() == "A":
            attack(character, challenger)
        if player_action.upper() == "R":
            run(character, challenger)  # add function
        if player_action.upper() == "D":
            dodge(character, challenger)  # add function


def dodge(character, challenger):
    pass


def run(character, challenger):
    pass


# REWORK ATTACK ---- break into atomic function, add Shields, Miss
# def attack(character, challenger):
#     if compare_ships(character, challenger):
#         challenger["HP"] -= character["Ship"]["Attack"]
#         print("You attack the enemy\ntheir HP= ", challenger["HP"])
#         if challenger["HP"] < 1:
#             print("You destroyed the hostile ship")
#             # character["Stats"]["Ships Destroyed"] += 1  #### add this later ?
#             return
#         else:
#             character["Ship"]["HP"] -= challenger["Attack"]
#             print("The enemy ship attacks!\nYour HP= ", character["Ship"]["HP"])
#             return
#     else:
#         character["Ship"]["HP"] -= challenger["Attack"]
#         print("The enemy ship attacks!\nYour HP= ", character["Ship"]["HP"])
#         if not is_alive(character):
#             print("You have been destroyed")
#             return
#         else:
#             challenger["HP"] -= character["Ship"]["Attack"]
#             print("You attack the enemy!\ntheir HP= ", challenger["HP"])
#             if challenger["HP"] < 1:
#                 print("You destroyed the hostile ship")
#                 # character["Stats"]["Ships Destroyed"] += 1  #### add this later ?
#                 return


def compare_ships(character, hostile_ship):
    comparison_results = {
        "Attack": character["Ship"]["Attack"] - hostile_ship["Ship"]["Attack"],
        "Movement": character["Ship"]["Movement"] - hostile_ship["Ship"]["Movement"],
        "HP": character["Ship"]["HP"] - hostile_ship["Ship"]["HP"],
        "Targeting": character["Ship"]["Targeting"] - hostile_ship["Ship"]["Targeting"],
        "Shield": character["Ship"]["Shield"] - hostile_ship["Ship"]["Shield"],
        "Cargo": character["Ship"]["Cargo"] - hostile_ship["Ship"]["Cargo"],
    }
    return comparison_results
