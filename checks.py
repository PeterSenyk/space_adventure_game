import combat
import random as r

import events


def is_alive(ship):
    """
    Checks if the player is still alive

    this function checks if the characters HP value is above zero

    :param ship: a dictionary of character location and HP
    :precondition: character HP value must start above zero
    :return: Boolean True of False
    """
    if ship["Ship"]["HP"][0] <= 0:
        return False
    else:
        return True


def get_player_coordinates(character):
    x_coordinate = character["Coordinates"]["X-coordinate"]
    y_coordinate = character["Coordinates"]["Y-coordinate"]
    coordinates = (x_coordinate, y_coordinate)
    return coordinates


def check_space_tile(character, space):
    coordinates = get_player_coordinates(character)
    tile_event_number = space[coordinates][0]
    match tile_event_number:
        case 3:
            events.training_combat(character)
        case 4:
            events.avoid_debris(character)
        case 5:
            if r.randint(1, 5) >= 4:
                combat.shield_recharge(character)
        case 6:
            events.asteroid_belt(character)
        case 7:
            # make a separate events !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            if r.randint(1, 10) >= 6:
                hostile_ship = combat.construct_medium_hostile_ship()
                combat.space_combat(character, hostile_ship)
            else:
                combat.shield_recharge(character)
        case 8:
            if r.randint(1, 10) >= 6:
                if character["Ship"]["HP"][0] <= character["Ship"]["HP"][1]:
                    character["Ship"]["HP"][0] += 1
            else:
                hostile_ship = combat.construct_medium_hostile_ship()
                combat.space_combat(character, hostile_ship)
        case 9:
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
        # case 10:
        #     events.return_stolen_item
        #             remove stolen items from cargo
        #             player level up to captain
        #             move to explorer space
        # case 11:
        #     combat.pirate_fight
        #     add stolen items to cargo

    # explorer space > upgrade to exploration ships, high hp and shields, explore anomoly @
    # can either return with info > end game or pass through anomoly = endless space until game over ???



# def check_space_tile(character, space):
#     coordinates = get_player_coordinates(character)
#     tile_event_number = space[coordinates][0]
#     if tile_event_number == 3:
#         print("You see a training hostile")
#         hostile_ship = combat.construct_training_hostile()
#         combat.space_combat(character, hostile_ship)
#     if tile_event_number == 4:
#         print("Try to dodge the debris if you can")
#         correct_route = r.randint(1, 3)
#         choice = int(input("Choose a heading to avoid the debris, your choices are:\n [1] [2] or [3]\n"))
#         if choice in [1, 2, 3]:
#             if choice == correct_route:
#                 print("You avoided the debris !")
#                 combat.shield_recharge(character)
#                 if "Debris Avoided" not in character:
#                     character["Stats"]["Accolades"]["Debris Avoided"] = 1
#                 else:
#                     character["Stats"]["Accolades"]["Debris Avoided"] += 1
#             else:
#                 print("You collide with the debris")
#                 combat.deal_other_damage(character, 1)
#         else:
#             print("Choose a valid route")


def level_one_goal(character):
    ships_destroyed = character["Stats"]["Accolades"]["Ships Destroyed"]
    debris_avoided = character["Stats"]["Accolades"]["Debris Avoided"]
    if ships_destroyed + debris_avoided == 4:
        return True


def level_two_goal(character):
    coordinates = (character["Coordinates"]["X-coordinate"], character["Coordinates"]["Y-coordinate"])
    if "Explorer Class Quantum Drive" in character["Ship"]["Cargo"] and coordinates == (2, 5):
        return True
