import random as r
import checks


def construct_training_hostile():
    """
    constructs a hostile for level one

    this function constructs a hostile with stats meant for level one

    :return: a dictionary representing the stats of the constructed hostile
    """
    hostile_shield = r.randint(2, 2)
    hostile_hp = r.randint(2, 3)
    hostile_ship = {"Ship": {
        "Attack": r.randint(1, 2), "Movement": r.randint(2, 3), "HP": [hostile_hp, hostile_hp],
        "Targeting": r.randint(1, 3), "Shield": [hostile_shield, hostile_shield],
        "Cargo": []
    }}
    return hostile_ship


def construct_medium_hostile_ship():
    """
    constructs a hostile for level two

    this function constructs a hostile with stats meant for level tow

    :return: a dictionary representing the stats of the constructed hostile
    """
    hostile_shield = r.randint(3, 4)
    hostile_hp = r.randint(3, 5)
    hostile_ship = {"Ship": {
        "Attack": r.randint(4, 6), "Movement": r.randint(2, 4),  "HP": [hostile_hp, hostile_hp],
        "Targeting": r.randint(3, 4), "Shield": [hostile_shield, hostile_shield],
        "Cargo": []
    }}
    return hostile_ship


def construct_hard_hostile_ship():
    """
    constructs a hostile for level three

    this function constructs a hostile with stats meant for level three

    :return: a dictionary representing the stats of the constructed hostile
    """
    hostile_shield = r.randint(4, 6)
    hostile_hp = r.randint(5, 7)
    hostile_ship = {"Ship": {
        "Attack": r.randint(3, 6), "Movement": r.randint(2, 4),  "HP": [hostile_hp, hostile_hp],
        "Targeting": r.randint(4, 6), "Shield": [hostile_shield, hostile_shield],
        "Cargo": []
    }}
    return hostile_ship


def construct_pirate_hostile_ship():
    """
    constructs a hostile for the level two boss

    this function constructs a hostile with stats meant for the level two boss

    :return: a dictionary representing the stats of the constructed hostile
    """
    hostile_shield = r.randint(4, 7)
    hostile_hp = r.randint(4, 7)
    hostile_ship = {"Ship": {
        "Attack": r.randint(3, 4), "Movement": r.randint(2, 6),  "HP": [hostile_hp, hostile_hp],
        "Targeting": r.randint(5, 6), "Shield": [hostile_shield, hostile_shield],
        "Cargo": []
    }}
    return hostile_ship


def space_combat(character, hostile_ship):
    """
    conducts the space combat sequence

    this function allows the player to choose an action when they encounter a hostile ship

    :param character: a dictionary of the player character information.
    :param hostile_ship: a dictionary of the hostile ship information.
    :precondition: the character has an HP value above zero
    :post-condition: the play conducts the action that they've chosen
    """
    while checks.is_alive(character) and checks.is_alive(hostile_ship):
        while True:
            player_action = input("Choose an action\n[A] = Attack\n[R] = Run\n[D] = Dodge\n[S] = Scan\n")
            valid_action = ["A", "R", "D", "S"]
            if player_action.upper() in valid_action:
                break
            else:
                print(f"Invalid action please choose on of the following: {valid_action}")
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
        print("\033[31mYou have been destroyed by the hostile ship\033[m")
    elif hostile_ship["Ship"]["HP"][0] == 0:
        print("\033[32mYou have destroyed the hostile ship\033[m")


def attack_sequence(character, hostile_ship):
    """
     conducts the space combat sequence

     this function handles combat between the character and a hostile ship

     :param character: a dictionary of the player character information.
     :param hostile_ship: a dictionary of the hostile ship information.
     :precondition: the character has an HP value above zero
     :post-condition: character gains 1 'Ships Destroyed' accolade if they win the space combat, game over if they loose
     """
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
    """
     conducts an attack during combat.

     this function handles an attack action during space combat.

     :param defender: attacker is the dictionary in the position of attacking.
     :param attacker: defender is the dictionary in the position of defending.
     :precondition: the attacker and defender have an HP value above zero.
     :post-condition: if the attack lands this function moves on to dealing damage
     """
    if check_for_hit(attacker, defender):
        deal_attack_damage(attacker, defender)


def dodge(character, hostile_ship):
    """
     conducts a dodge during combat.

     this function handles a dodge action during space combat.

     :param character: a dictionary of the player character information.
     :param hostile_ship: a dictionary of the hostile ship information.
     :precondition: the character and hostile ship have an HP value above zero.
     :post-condition: increase the chance for the hostile ship to miss, allowing character to recharge the shield
     """
    dodge_chance = (character["Ship"]["Movement"] + r.randint(4, 7))
    hit_chance = r.randint(5, 9)
    if dodge_chance <= hit_chance:
        deal_attack_damage(hostile_ship, character)
    else:
        shield_recharge(character)


def run(character, hostile_ship):
    """
     allows the player to run combat.

     this function handles a run action during space combat.

     :param character: a dictionary of the player character information.
     :param hostile_ship: a dictionary of the hostile ship information.
     :precondition: the character and hostile ship have an HP value above zero.
     :post-condition: ends combat prior to either ship being destroyed.
     """
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
    """
     checks for an attack to land during combat

     this function handles a run action during space combat.

     :param defender: attacker is the dictionary in the position of attacking.
     :param attacker: defender is the dictionary in the position of defending.
     :precondition: the character and hostile ship have an HP value above zero.
     :post-condition: determines whether an attack lands during combat
     :return: a boolean True for attack hit, a boolean False for attack miss
     """
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
    """
     deal attack damage during combat

     this function handles dealing attack damage during combat.

     :param defender: attacker is the dictionary in the position of attacking.
     :param attacker: defender is the dictionary in the position of defending.
     :precondition: the character and hostile ship have an HP value above zero.
     :post-condition: determines what is damaged based on the amount of attack a ship has
     """
    attack_value = attacker["Ship"]["Attack"]
    deal_other_damage(defender, attack_value)


def deal_other_damage(defender, damage_value):
    """
     handles dealing damage

     this function handles dealing damage based on a damage value

     :param defender: attacker is the dictionary in the position of attacking.
     :param damage_value: a positive integer
     :precondition: the defender must have an HP value above zero.
     :post-condition: determines what is damaged based on the damage value
     """
    original_shield = defender["Ship"]["Shield"][0]
    original_hp = defender["Ship"]["HP"][0]
    for point in range(damage_value):
        if defender["Ship"]["Shield"][0] > 0:
            defender["Ship"]["Shield"][0] -= 1
        elif defender["Ship"]["Shield"][0] <= 0 < defender["Ship"]["HP"][0]:
            defender["Ship"]["HP"][0] -= 1
    shield_damage = original_shield - defender["Ship"]["Shield"][0]
    hull_damage = original_hp - defender["Ship"]["HP"][0]
    if shield_damage > 0:
        print(f"The shields reflect {shield_damage} damage\nThe hull took {hull_damage} damage")
    else:
        print(f"The hull took {hull_damage} damage")


def shield_recharge(ship):
    """
     recharges the shield of a ship

     this function handles shield recharging.

     :param ship: a dictionary of the ship information
     :precondition: the defender must have an HP value above zero.
     :post-condition: determines what is damaged based on the damage value
     """
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
    """
     displays both ships stats.

     this function displays the stats of the characters, and hostiles ship.

     :param character: a dictionary of the player character information.
     :param hostile_ship: a dictionary of the hostile ship information.
     :precondition: the character and hostile both must have an HP value above zero.
     :post-condition: outputs information of character and hostile ships
     """
    print("Your ship stats:\n", character["Ship"])
    print("Hostile ship stats:\n", hostile_ship["Ship"])


if __name__ == "__main__":
    import doctest
    doctest.testmod()
