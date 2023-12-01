import random as r
import combat


def training_combat(character):
    print("You see a training hostile")
    hostile_ship = combat.construct_training_hostile()
    combat.space_combat(character, hostile_ship)


def avoid_debris(character):
    print("Try to dodge the debris if you can")
    correct_route = r.randint(1, 3)
    try:
        choice = int(input("Choose a heading to avoid the debris, your choices are:\n [1] [2] or [3]\n"))
    except ValueError:
        print("Choose a valid selection")
    else:
        if choice in [1, 2, 3]:
            if choice == correct_route:
                print("You avoided the debris !")
                combat.shield_recharge(character)
                character["Stats"]["Accolades"]["Debris Avoided"] += 1
            else:
                print("You collide with the debris")
                combat.deal_other_damage(character, 1)


def asteroid_belt(character):
    print("Theres more asteroids than you expected, you're going to have to fly by instinct here")
    asteroids = r.randint(1, 3)
    for attempts in range(asteroids):
        correct_path = r.randint(1, 4)
        get_flight_path = input("You only see small windows to pass through, pick a direction to steer\n"
                                "W = Up\nS = Down\nA = Left\nD = Right\n")
        chosen_path = clean_asteroid_game_direction(get_flight_path)
        if chosen_path == correct_path:
            combat.shield_recharge(character)
        else:
            combat.deal_other_damage(character, 1)


def clean_asteroid_game_direction(direction):
    if direction.upper() == "W":
        return 1
    elif direction.upper() == "S":
        return 2
    elif direction.upper() == "A":
        return 3
    elif direction.upper() == "D":
        return 4


def dark_side_of_moon(character):
    if r.randint(1, 10) >= 6:
        if character["Ship"]["HP"][0] <= character["Ship"]["HP"][1]:
            character["Ship"]["HP"][0] += 1
    else:
        hostile_ship = combat.construct_medium_hostile_ship()
        combat.space_combat(character, hostile_ship)


def abandoned_space_station(character):
    if r.randint(1, 10) == 10:
        character["Ship"]["Attack"] += 1
    if r.randint(1, 10) == 9:
        character["Ship"]["Movement"] += 1
    if r.randint(1, 10) == 8:
        character["Ship"]["Shield"][1] += 1
    if r.randint(1, 10) == 7:
        character["Ship"]["HP"][1] += 1
    else:
        hostile_ship = combat.construct_medium_hostile_ship()
        combat.space_combat(character, hostile_ship)


def pirate_combat(character):
    hostile = combat.construct_pirate_hostile_ship()
    combat.space_combat(character, hostile)
    if character["Ship"]["HP"][0] > 0:
        character["Ship"]["Cargo"].append("Explorer Class Quantum Drive")


def bring_back_stolen_tech(character):
    coordinates = (character["Coordinates"]["X-coordinate"], character["Coordinates"]["Y-coordinate"])
    if "Explorer Class Quantum Drive" in character["Ship"]["Cargo"] and coordinates == (2, 6):
        character["Ship"]["Cargo"].pop()
        return True
    else:
        return False

