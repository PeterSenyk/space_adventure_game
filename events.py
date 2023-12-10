import random as r
import combat


def training_combat(character):
    """
    randomizes a hostile ship for the training level.

    this function creates a randomized hostile ship for training combat

    :param character: a dictionary of the player character information.
    :post-condition: a dictionary of the hostile information is created.
    """
    print("You see a training hostile")
    hostile_ship = combat.construct_training_hostile()
    combat.space_combat(character, hostile_ship)


def avoid_debris(character):
    """
    the player must avoid space debris to complete this event

    this function asks the player to choose a number, if it matches the correct_route the player is successful
    :param character: a dictionary of the player character information.
    :post-condition: if the player wins they recharge 1 shield point, if they loose they take 1 damage.
    """
    print("Try to dodge the debris if you can")
    correct_route = r.randint(1, 3)
    while True:
        try:
            choice = int(input("Choose a heading to avoid the debris, your choices are:\n [1] [2] or [3]\n"))
            if choice in [1, 2, 3]:
                break
            else:
                print("Please choose either [1], [2], or [3]]")
        except ValueError:
            print("Choose a valid selection")
    if choice == correct_route:
        print("You avoided the debris !")
        combat.shield_recharge(character)
        character["Stats"]["Accolades"]["Debris Avoided"] += 1
    else:
        print("You collide with the debris")
        combat.deal_other_damage(character, 1)


def asteroid_belt(character):
    """
    the player must avoid up to three asteroids in this event

    this function challenges the player to avoid multiple asteroids by choosing which direction to fly in
    :param character: a dictionary of the player character information.
    :post-condition: every debris the player avoids, they recharge 1 shield point, else they take 1 damage
    """
    print("Theres more asteroids than you expected, you're going to have to fly by instinct here")
    asteroids = r.randint(1, 3)
    for attempts in range(asteroids):
        correct_path = r.randint(1, 4)
        while True:
            get_flight_path = input("You only see small windows to pass through, pick a direction to steer\n"
                                    "[W] = Up\n[S] = Down\n[A] = Left\n[D] = Right\n")
            valid_choices = ["W", "A", "S", "D"]
            if get_flight_path.upper() in valid_choices:
                chosen_path = clean_asteroid_game_direction(get_flight_path)
                if chosen_path == correct_path:
                    combat.shield_recharge(character)
                    break
                else:
                    combat.deal_other_damage(character, 1)
                    break
            else:
                print("Please choose a valid direction.\nEither [W], [A], [S], or [D]")


def clean_asteroid_game_direction(direction):
    """
    cleans the asteroid event direction

    this function turn the asteroid event direction into an integer to test against the random number

    :param direction: is a string of either "W", "A", "S", or "D"
    :return: an integer between 1 and 4
    """
    if direction.upper() == "W":
        return 1
    elif direction.upper() == "S":
        return 2
    elif direction.upper() == "A":
        return 3
    elif direction.upper() == "D":
        return 4


def dark_side_of_moon(character):
    """
    random change of the character healing 1 HP or encountering an enemy
    :param character: a dictionary of the player character information.
    :post-condition: the character is healed or encounters a hostile ship
    """
    if r.randint(1, 10) >= 6:
        if character["Ship"]["HP"][0] < character["Ship"]["HP"][1]:
            print("You have a chance to repair your ship, you gain 1 HP\nCurrent HP: ", character["Ship"]['HP'][0],
                  "out of", character["Ship"]['HP'][1])
            character["Ship"]["HP"][0] += 1
    else:
        hostile_ship = combat.construct_medium_hostile_ship()
        combat.space_combat(character, hostile_ship)


def abandoned_space_station(character):
    """
    allows the player to salvage parts for stat boosts, with increasing risk of encountering a hard hostile
    :param character: a dictionary of the player character information.
    :return:
    """
    print("You send a salvage drone into the abandoned station")
    choose_to_leave = False
    chance_of_encounter = 0
    while not choose_to_leave or chance_of_encounter >= 10:
        print("Pick which component you want the salvage drone to look for:")
        choose_to_leave = pick_component(character)
        print("You're not the only one salvaging, the longer you stay the higher chance of attracting attention")
        chance_of_encounter += r.randint(1, 9)
        if chance_of_encounter >= 10:
            hostile_ship = combat.construct_hard_hostile_ship()
            combat.space_combat(character, hostile_ship)
            break


def pick_component(character):
    """
    takes the players choice of salvage for a stat boost
    :param character: a dictionary of the player character information.
    :return: a boolean True or False
    """
    while True:
        player_choice = input("[W] for weapons\n[E] for engines\n[S] for shield generators\n[H] for hull scraps\n[R] "
                              "for targeting sensors\n[Q] to leave the station\n")
        valid_choices = ["W", "E", "S", "H", "R", "Q"]
        if player_choice.upper() in valid_choices:
            break
        else:
            print("Choose a valid selection")
    if player_choice.upper() == "W":
        print("The salvage drone returns with some weapon components\nYou gain 1 Attack point")
        character["Ship"]["Attack"] += 1
    elif player_choice.upper() == "E":
        print("The salvage drone returns with some weapon components\nYou gain 1 Movement point")
        character["Ship"]["Movement"] += 1
    elif player_choice.upper() == "S":
        print("The salvage drone returns with some weapon components\nYou gain 1 Shield point")
        character["Ship"]["Shield"][0] += 1
        character["Ship"]["Shield"][1] += 1
    elif player_choice.upper() == "H":
        print("The salvage drone returns with some weapon components\nYou gain 1 HP point")
        character["Ship"]["HP"][0] += 1
        character["Ship"]["HP"][1] += 1
    elif player_choice.upper() == "R":
        print("The salvage drone returns with some weapon components\nYou gain 1 Targeting point")
        character["Ship"]["Targeting"] += 1
    elif player_choice.upper() == "Q":
        print("You leave the abandoned station")
        return True
    return False


def pirate_combat(character):
    """
    randomizes a pirate hostile for the level two boss fight

    :param character: a dictionary of the player character information.
    :post-condition: if the player wins the combat, the "Explorer Class Quantum Drive" will be added to ship cargo.
    """
    hostile = combat.construct_pirate_hostile_ship()
    combat.space_combat(character, hostile)
    if character["Ship"]["HP"][0] > 0:
        character["Ship"]["Cargo"].append("Explorer Class Quantum Drive")


def bring_back_stolen_tech(character):
    """
    completes the level two goal if the player cargo includes "Explorer Class Quantum Drive"

    :param character: a dictionary of the player character information.
    :return: a boolean True of False
    """
    coordinates = (character["Coordinates"]["X-coordinate"], character["Coordinates"]["Y-coordinate"])
    if "Explorer Class Quantum Drive" in character["Ship"]["Cargo"] and coordinates == (2, 6):
        character["Ship"]["Cargo"].pop()
        return True
    else:
        return False


def electro_magnetic_field(character):
    """
    a dangerous event that reduces the player shield to zero, with the chance of encountering a medium hostile ship

    :param character:
    """
    character["Ship"]["Shield"][0] = 0
    chance_of_combat = r.randint(1, 2)
    if chance_of_combat == 1:
        hostile_ship = combat.construct_medium_hostile_ship()
        hostile_ship["Ship"]["Shield"][0] = 0
        combat.space_combat(character, hostile_ship)


def repair_outpost(character):
    """
    restores the players HP and shield

    this function restores the player shield and HP to full

    :param character: a dictionary of the player character information.
    :post-condition: the player HP and shield are restored to maximum
    """
    print("Your ships hull is repaired and your shields have been recharged")
    character["Ship"]["HP"][0] = character["Ship"]["HP"][1]
    character["Ship"]["Shield"][0] = character["Ship"]["Shield"][1]


def space_cloud(character):
    """
    the player has a chance of either +1 or -1 Movement point

    :param character: a dictionary of the player character information.
    :post-condition: the player movement attribute is modified
    """
    event_chance = r.randint(1, 10)
    if event_chance >= 4:
        print("The cloud of gas runs through your engines clearing out any debris,\nYou gain 1 Movement")
        character["Ship"]["Movement"] += 1
    else:
        print("The gas cloud causes your engines to burn HOT\nYou loose 1 Movement")
        character["Ship"]["Movement"] -= 1


def shady_outpost(character):
    """
    the player can barter with a shop owner to try and buy better weapons for the shio

    the function lets the player barter for weapons, if you over or under pay you lose1 Attack, if you get the
    value right you gain 1 Attack.
    :param character: a dictionary of the player character information.
    :post-condition: the players attack stat is modified
    """
    print("You stop in the shady outpost to see what they have to offer\nA shop owner starts bartering with you "
          "attempting to sell you new weapons for your ship\nThey promise you that the weapons are better than the "
          "ones you currently have equipped\n")
    user_choice = input("To pass on this offer select: [N]\nTo barter with the shop owner select: [Y]\n")
    if user_choice.upper() == "Y":
        print("The shop owner asks you to make them an offer on the new weapons")
        credit_minimum = r.randint(1, 5) * 1000
        credit_maximum = credit_minimum + (r.randint(2, 3) * 1000)
        while True:
            try:
                player_offer = int(input("Enter a value that you're willing to pay for the new weapons between "
                                         "0 and 10000\n"))
            except ValueError:
                print("Please choose a value between 0 and 10000")
            else:
                if credit_minimum <= player_offer <= credit_maximum:
                    print("You make a good deal\nThe new weapons are pretty shiny\nYou gain 1 Attack point")
                    character["Ship"]["Attack"] += 1
                    break
                elif player_offer < credit_minimum:
                    print("You tryin' to rip me off ?!?\nThe new weapons installed are rusty\nYou loose 1 Attack point")
                    character["Ship"]["Attack"] -= 1
                    break
                elif player_offer > credit_maximum:
                    print("The shop owner takes you for a sucker\nThe new weapons look great, they make a weird "
                          "noise when starting up though\nYou loose 1 Attack point")
                    character["Ship"]["Attack"] -= 1
                    break
    else:
        return


def anomaly():
    """
    this is the end of the game.

    this function acts as a cutscene at the end of the game.

    :post-condition: the game ends.
    """
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


def main():
    pass


if __name__ == "__main__":
    main()
