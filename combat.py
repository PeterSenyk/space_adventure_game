import random as r
from checks import is_alive


def construct_hostile_ship():
    hostile_ship = {"Ship": {
        "Attack": r.randint(1, 2), "Movement": r.randint(1, 3), "HP": r.randint(1, 3),
        "Targeting": r.randint(1, 4), "Shield": [1, r.randint(0, 1)],
        "Cargo": r.randint(0, 1)
    }}
    return hostile_ship


def space_combat(character, hostile_ship):
    print("You come across a hostile ship")
    print(hostile_ship)
    while is_alive(character) and is_alive(hostile_ship):
        # print(character["Ship"]["HP"])
        # print(challenger["HP"])
        player_action = input("Choose an action\nA = Attack\nR = Run\nD = Dodge\n")
        if player_action.upper() == "A":
            attack_sequence(character, hostile_ship)
        if player_action.upper() == "R":
            run(character, hostile_ship)
            break
        if player_action.upper() == "D":
            dodge(character, hostile_ship)


def attack_sequence(character, hostile_ship):
    comparison_results = compare_ships(character, hostile_ship)
    if comparison_results["Movement"] >= 0:
        print("You attack the hostile ship")
        attack(character, hostile_ship)
        if is_alive(hostile_ship):
            print(f"The hostile ship has", hostile_ship["Ship"]["HP"], "HP remaining")
            print("The hostile ship survives and attacks back")
            attack(hostile_ship, character)
        else:
            print("You destroy the hostile ship !")
            character["Stats"]["Accolades"]["Ships Destroyed"] += 1
    else:
        print("The hostile ship attacks")
        attack(hostile_ship, character)
        if is_alive(character):
            print("You survive with", character["Ship"]["HP"], "HP remaining")
            print("You attack the hostile ship")
            attack(character, hostile_ship)
            if is_alive(hostile_ship):
                print("The hostile ship survives with", hostile_ship["Ship"]["HP"], "HP remaining")
            else:
                print("You destroy the hostile ship !")
                character["Stats"]["Accolades"]["Ships Destroyed"] += 1
        else:
            print("You were destroyed\nGAME OVER")


def attack(attacker, defender):
    if check_for_hit(attacker, defender):
        check_shields(attacker, defender)


def dodge(character, hostile_ship):
    dodge_chance = (character["Ship"]["Movement"] + r.randint(1, 6))
    hit_chance = r.randint(5, 9)
    if dodge_chance <= hit_chance:
        print(dodge_chance)
        print(hit_chance)
        check_shields(hostile_ship, character)
    else:
        print(dodge_chance)
        print(hit_chance)
        shield_recharge(character)


def run(character, hostile_ship):
    comparison_results = compare_ships(character, hostile_ship)
    if comparison_results["Movement"] > 0:
        print("You evade the hostile ship, and disappear into the darkness of space")
        return True
    elif comparison_results["Movement"] <= 0:
        character["Ship"]["HP"] -= comparison_results["Movement"]
        print("You attempt evasive maneuvers, but the hostile ship stays on target, "
              "you escape into the darkness but not without taking some damage")
        return True


def check_for_hit(attacker, defender):
    if attacker["Ship"]["Targeting"] >= defender["Ship"]["Movement"]:
        print("The attack lands")
        return True
    else:
        if r.randint(1, 10) >= 6:
            print("The attack lands")
            return True
        else:
            print("The attack misses")
            shield_recharge(defender)
            return False


def check_shields(attacker, defender):
    for point in range(attacker["Ship"]["Attack"]):
        if defender["Ship"]["Shield"][0] > 0:
            defender["Ship"]["Shield"][0] -= 1
            print("The Shields reflect 1 damage")
        elif defender["Ship"]["Shield"][0] <= 0 < defender["Ship"]["HP"]:
            defender["Ship"]["HP"] -= 1
            print("The hull takes 1 damage")
        else:
            print("SHIP DESTROYED !")


def shield_recharge(ship):
    if ship["Ship"]["Shield"][0] < ship["Ship"]["Shield"][1]:
        print("Your shields recharge by 1 point")
        ship["Ship"]["Shield"][0] += 1
    else:
        print("Your shields are at MAX capacity")


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
        "Shield": character["Ship"]["Shield"][0] - hostile_ship["Ship"]["Shield"][0],
        "Cargo": character["Ship"]["Cargo"] - hostile_ship["Ship"]["Cargo"],
    }
    return comparison_results
