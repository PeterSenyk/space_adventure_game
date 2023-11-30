import random as r
import checks


def construct_training_hostile():
    hostile_shield = r.randint(0, 1)
    hostile_hp = r.randint(1, 2)
    hostile_ship = {"Ship": {
        "Attack": r.randint(1, 2), "Movement": r.randint(1, 3), "HP": [hostile_hp, hostile_hp],
        "Targeting": r.randint(1, 3), "Shield": [hostile_shield, hostile_shield],
        "Cargo": []
    }}
    return hostile_ship


def construct_hostile_ship():
    hostile_shield = r.randint(0, 2)
    hostile_ship = {"Ship": {
        "Attack": r.randint(1, 2), "Movement": r.randint(1, 3), "HP": r.randint(1, 3),
        "Targeting": r.randint(1, 4), "Shield": [hostile_shield, hostile_shield],
        "Cargo": []
    }}
    return hostile_ship


def space_combat(character, hostile_ship):
    while character["Ship"]["HP"][0] > 0 and checks.is_alive(hostile_ship):
        player_action = input("Choose an action\nA = Attack\nR = Run\nD = Dodge\nS = Scan\n")
        if player_action.upper() == "A":
            attack_sequence(character, hostile_ship)
        if player_action.upper() == "R":
            run(character, hostile_ship)
            break
        if player_action.upper() == "D":
            dodge(character, hostile_ship)
        if player_action.upper() == "S":
            scan_ships(character, hostile_ship)
    if character["Ship"]["HP"][0] == 0:
        print("You have been destroyed by the hostile ship")
    elif hostile_ship["Ship"]["HP"][0] == 0:
        print("You have destroyed the hostile ship")


def attack_sequence(character, hostile_ship):
    comparison_results = compare_ships(character, hostile_ship)
    if comparison_results["Movement"] >= 0:
        print("You fire at the hostile ship")
        attack(character, hostile_ship)
        if checks.is_alive(hostile_ship):
            print(f"The hostile ship has", hostile_ship["Ship"]["HP"], "HP remaining")
            print("The hostile ship survives and fires back")
            attack(hostile_ship, character)
        else:
            character["Stats"]["Accolades"]["Ships Destroyed"] += 1
    else:
        print("The hostile ship fires at you")
        attack(hostile_ship, character)
        if character["Ship"]["HP"][0] > 0:
            print("You survive with", character["Ship"]["HP"], "HP remaining")
            print("You fire at the hostile ship")
            attack(character, hostile_ship)
            if checks.is_alive(hostile_ship):
                print("The hostile ship survives with", hostile_ship["Ship"]["HP"], "HP remaining")
            else:
                character["Stats"]["Accolades"]["Ships Destroyed"] += 1
        else:
            print("You were destroyed\nGAME OVER")


def attack(attacker, defender):
    if check_for_hit(attacker, defender):
        deal_attack_damage(attacker, defender)


def dodge(character, hostile_ship):
    dodge_chance = (character["Ship"]["Movement"] + r.randint(4, 7))
    hit_chance = r.randint(5, 9)
    if dodge_chance <= hit_chance:
        deal_attack_damage(hostile_ship, character)
    else:
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


def deal_attack_damage(attacker, defender):
    for point in range(attacker["Ship"]["Attack"]):
        if defender["Ship"]["Shield"][0] > 0:
            defender["Ship"]["Shield"][0] -= 1
            print("The Shields reflect 1 damage")
        elif defender["Ship"]["Shield"][0] <= 0 < defender["Ship"]["HP"][0]:
            defender["Ship"]["HP"][0] -= 1
            print("The hull takes 1 damage")


def deal_other_damage(defender, attack):
    for point in range(attack):
        if defender["Ship"]["Shield"][0] > 0:
            defender["Ship"]["Shield"][0] -= 1
            print("The Shields reflect 1 damage")
        elif defender["Ship"]["Shield"][0] <= 0 < defender["Ship"]["HP"][0]:
            defender["Ship"]["HP"][0] -= 1
            print("The hull takes 1 damage")


def shield_recharge(ship):
    if ship["Ship"]["Shield"][0] < ship["Ship"]["Shield"][1]:
        print("Your shields recharge by 1 point")
        ship["Ship"]["Shield"][0] += 1
    else:
        print("Your shields are at MAX capacity")


def compare_ships(character, hostile_ship):
    comparison_results = {
        "Attack": character["Ship"]["Attack"] - hostile_ship["Ship"]["Attack"],
        "Movement": character["Ship"]["Movement"] - hostile_ship["Ship"]["Movement"],
        "Targeting": character["Ship"]["Targeting"] - hostile_ship["Ship"]["Targeting"],
        "Shield": character["Ship"]["Shield"][0] - hostile_ship["Ship"]["Shield"][0],
         }
    return comparison_results


def scan_ships(character, hostile_ship):
    print("Your ship stats:\n", character["Ship"])
    print("Hostile ship stats:\n", hostile_ship["Ship"])
