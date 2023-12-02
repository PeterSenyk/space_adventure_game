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
        if character["Ship"]["HP"][0] < character["Ship"]["HP"][1]:
            character["Ship"]["HP"][0] += 1
    else:
        hostile_ship = combat.construct_medium_hostile_ship()
        combat.space_combat(character, hostile_ship)


def abandoned_space_station(character):
    print("You send a salvage drone into the abandoned station")
    choose_to_leave = False
    chance_of_encounter = 0
    while not choose_to_leave or chance_of_encounter <= 10:
        print("Pick which component you want the salvage drone to look for:")
        choose_to_leave = pick_component(character)
        print("You're not the only one salvaging, the longer you stay the higher chance of attracting attention")
        chance_of_encounter += r.randint(1, 9)
    if choose_to_leave:
        return
    elif chance_of_encounter >= 10:
        hostile_ship = combat.construct_hard_hostile_ship()
        combat.space_combat(character, hostile_ship)


def pick_component(character):
    player_choice = input("[W] for weapons\n[E] for engines\n[S] for shield generators\n[H] for hull scraps\n[R] "
                          "for targeting sensors\n[Q] to leave the station")
    if player_choice.upper() == "W":
        print("The salvage drone returns with some weapon components\nYou gain 1 Attack point")
        character["Ship"]["Attack"] += 1
        return False
    elif player_choice.upper() == "E":
        character["Ship"]["Movement"] += 1
        return False
    elif player_choice.upper() == "S":
        character["Ship"]["Shield"][0] += 1
        character["Ship"]["Shield"][1] += 1
        return False
    elif player_choice.upper() == "H":
        character["Ship"]["HP"][0] += 1
        character["Ship"]["HP"][1] += 1
        return False
    elif player_choice.upper() == "R":
        character["Ship"]["Targeting"] += 1
    elif player_choice.upper() == "Q":
        return True
    else:
        print("Choose a valid selection")
        return False


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


def electro_magnetic_field(character):
    character["Ship"]["Shield"][0] = 0
    chance_of_combat = r.randint(1, 2)
    if chance_of_combat == 1:
        hostile_ship = combat.construct_pirate_hostile_ship()
        hostile_ship["Ship"]["Shield"][0] = 0
        combat.space_combat(character, hostile_ship)


def repair_outpost(character):
    print("Your ships hull is repaired and your shields have been recharged")
    character["Ship"]["HP"][0] = character["Ship"]["HP"][1]
    character["Ship"]["Shield"][0] = character["Ship"]["Shield"][1]


# hide symbol as something else !
def space_cloud(character):
    event_chance = r.randint(1, 10)
    if event_chance >= 4:
        character["Ship"]["Movement"] += 1
    else:
        character["Ship"]["Movement"] -= 1


def shady_outpost(character):
    print("You stop in the shady outpost to see what they have to offer\nA shop owner starts bartering with you "
          "attempting to sell you new weapons for your ship\nThey promise you that the weapons are better than the "
          "ones you currently have equipped\n")
    user_choice = input("To pass on this offer select: [N]\nTo barter with the shop owner select: [Y]")
    if user_choice.upper() == "Y":
        print("The shop owner asks you to make them an offer on the new weapons")
        credit_minimum = r.randint(1, 5) * 1000
        credit_maximum = credit_minimum + (r.randint(2, 3) * 1000)
        player_offer = int(input("Enter a value that you're willing to pay for the new weapons between 0 and 10000\n"))
        if credit_minimum <= player_offer <= credit_maximum:
            print("You make a good deal\nThe new weapons are pretty shiny\nYou gain 1 Attack point")
            character["Ship"]["Attack"] += 1
        elif player_offer < credit_minimum:
            print("You tryin' to rip me off ?!?\nThe new weapons installed are rusty\nYou loose 1 Attack point")
            character["Ship"]["Attack"] -= 1
        elif player_offer > credit_maximum:
            print("The shop owner takes you for a sucker\nThe new weapons look great, they make a weird noise when "
                  "starting up though\nYou loose 1 Attack point")
            character["Ship"]["Attack"] -= 1
    else:
        return


    def anomaly(character):
        print("As your ship slides towards the center of the ANOMALY several alarms go off before all electrical "
              "systems fail at once\nYour cockpit is glowing with the light coming from the ANOMALY\nThe glow flashes "
              "different colors of starlight and gets brighter\nIn a flash your systems turn back on and the sky"
              "around you is completely devoid of stars\nYour sensors show NOTHING, not even background radiation")
        player_choice = int(input("You have 2 option:\n input [1] to stay and wait for rescue\n input [2] "
                                  "to explore further"))
        if player_choice == 1:
            print("You realize you have enough life support and rations for 36 days\nYou decide to stay in place and "
                  "wait for rescue\nOn day 24 madness starts to creep into the minds of you and your crew")
        elif player_choice == 2:
            anomaly_chance = r.randint(1, 30)
            if anomaly_chance >= 3:
                print("You realize you have enough life support and rations for 36 days\nYou set a heading into "
                      "the ANOMALY, on day 24 your scanners pick up a glimmer of light")
            else:
                print("You realize you have enough life support and rations for 36 days\nYou set your engines "
                      "to full power and fly in steady heading, unbeknownst to you the ANOMALY did indeed have an "
                      "indestructible invisible inner surface\nYou collide with it at 40% of the speed of light")


