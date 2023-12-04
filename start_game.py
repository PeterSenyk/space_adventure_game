def base_character():
    """
    holds the dictionary of a base character

    this function holds the dictionary for the base character

    :return: a dictionary for the base starting character
    """
    character = {"Stats": {"Title": "Trainee", "Name": "", "Accolades": {"Ships Destroyed": 0, "Debris Avoided": 0}},
                 "Ship": {"Name": "", "Attack": 2, "Movement": 2, "HP": [5, 5], "Targeting": 4,
                          "Shield": [2, 2], "Cargo": []},
                 "Coordinates": {"X-coordinate": 0, "Y-coordinate": 0}}
    return character


def build_character(character):
    """
    builds the character to start the game.

    this function builds on the base character dictionary.

    :param character: a dictionary of the player character information.
    :post-condition: the starting character is built with a name and a starting ship.
    :return: a dictionary of the player character information.
    """
    get_player_last_name(character)
    print(f"Welcome to the Academy {character['Stats']['Title']} {character['Stats']['Name']}")
    valid_ship = False
    while not valid_ship:
        valid_ship = choose_training_ship(character)
    return character


def get_player_last_name(character):
    """
    formats the players last name.

    this functions accepts an input and formats it to have a capitalized first letter follower by lower case letters

    :param character: a dictionary of the player character information.
    :post-condition: a capitalized last name is added to the character dictionary.

    character = character = {
            "Stats": {"Title": "Trainee", "Name": "", "Accolades": {"Ships Destroyed": 0, "Debris Avoided": 0}},
            "Ship": {"Name": "", "Attack": 2, "Movement": 2, "HP": [5, 5], "Targeting": 4,
                     "Shield": [2, 2], "Cargo": []},
            "Coordinates": {"X-coordinate": 0, "Y-coordinate": 0}}
    >>> get_player_last_name({
            "Stats": {"Title": "Trainee", "Name": "", "Accolades": {"Ships Destroyed": 0, "Debris Avoided": 0}},
            "Ship": {"Name": "", "Attack": 2, "Movement": 2, "HP": [5, 5], "Targeting": 4,
                     "Shield": [2, 2], "Cargo": []},
            "Coordinates": {"X-coordinate": 0, "Y-coordinate": 0}})
    >>> last_name = senyk
    >>> character
    {"Stats": {"Title": "Trainee", "Name": "Senyk", "Accolades": {"Ships Destroyed": 0, "Debris Avoided": 0}},
    "Ship": {"Name": "", "Attack": 2, "Movement": 2, "HP": [5, 5], "Targeting": 4,
             "Shield": [2, 2], "Cargo": []},
    "Coordinates": {"X-coordinate": 0, "Y-coordinate": 0}}
    """
    last_name = capitalize_name(input("Enter your last name to register for the Arc-Corp Space Academy\n"))
    character["Stats"]["Name"] = last_name


def capitalize_name(name):
    last_name = name.strip().lower()
    last_name_cleaned = last_name.title()
    return last_name_cleaned


def choose_training_ship(character):
    """
    Selects a ship for the game

    this funtion lets the player select their ship for the game

    :post-condition: a dictionary is added to the character dictionary adding starting ship stats
    :return: a dictionary
    """
    print(character['Stats']['Title'], character["Stats"]["Name"], "Here are your choices for a training ship with "
                                                                   "their respective stats")
    print("ANVIL AURORA: Attack [2], Movement [3], HP [4], Shield [2], Targeting [4], Cargo Space [2]")
    print("AEGIS TITAN: Attack [3], Movement [2], HP [4], Shield [3], Targeting [3], Cargo Space [2]")
    print("DRAKE CUTTER: Attack [4], Movement [2], HP [3], Shield [2], Targeting [4], Cargo Space [2]")
    training_ship = input("Please select:\n[A] for the ANVIL AURORA\n"
                          "[T] for the AEGIS TITAN\n[C] for the DRAKE CUTTER\n")
    if training_ship.upper() == "A":
        character["Ship"] = {"Name": "ANVIL AURORA", "Attack": 2,
                             "Movement": 3, "HP": [4, 4], "Targeting": 4,
                             "Shield": [2, 2], "Cargo": []}
        valid_ship = True
        return valid_ship
    if training_ship.upper() == "T":
        character["Ship"] = {"Name": "AEGIS TITAN", "Attack": 3,
                             "Movement": 2, "HP": [4, 4], "Targeting": 3,
                             "Shield": [3, 3], "Cargo": []}
        valid_ship = True
        return valid_ship
    if training_ship.upper() == "C":
        character["Ship"] = {"Name": "DRAKE CUTTER", "Attack": 4,
                             "Movement": 2, "HP": [3, 3], "Targeting": 4,
                             "Shield": [2, 2], "Cargo": []}
        valid_ship = True
        return valid_ship
    if training_ship.upper() == "Z":
        character["Ship"] = {"Name": "F8C - TEST", "Attack": 100,
                             "Movement": 100, "HP": [100, 100], "Targeting": 100,
                             "Shield": [100, 100], "Cargo": []}
        valid_ship = True
        return valid_ship
    else:
        print("Please choose a valid selection")


def choose_fighter_ship(character):
    """
    Selects a ship for the game

    this funtion lets the player select their ship for the game

    :post-condition: a dictionary is added to the character dictionary adding starting ship stats
    :return: a dictionary
    """
    print(character['Stats']['Title'], character["Stats"]["Name"], "Here are your choices for a Fighter ship with "
                                                                   "their respective stats")
    print("ANVIL ARROW: Attack [4], Movement [5], HP [4], Shield [4], Targeting [5], Cargo Space [2]")
    print("AEGIS GLADIUS: Attack [5], Movement [3], HP [6], Shield [5], Targeting [4], Cargo Space [2]")
    print("DRAKE BUCCANEER: Attack [6], Movement [4], HP [3], Shield [4], Targeting [5], Cargo Space [2]")
    fighter_ship = input("Please select:\n[A] for the ANVIL ARROW\n"
                         "[G] for the AEGIS GLADIUS\n[B] for the DRAKE BUCCANEER\n")
    if fighter_ship.upper() == "A":
        character["Ship"] = {"Name": "ANVIL ARROW", "Attack": 4,
                             "Movement": 5, "HP": [4, 4], "Targeting": 5,
                             "Shield": [4, 4], "Cargo": []}
        valid_ship = True
        return valid_ship
    if fighter_ship.upper() == "G":
        character["Ship"] = {"Name": "AEGIS GLADIUS", "Attack": 5,
                             "Movement": 3, "HP": [6, 6], "Targeting": 4,
                             "Shield": [5, 5], "Cargo": []}
        valid_ship = True
        return valid_ship
    if fighter_ship.upper() == "B":
        character["Ship"] = {"Name": "DRAKE BUCCANEER", "Attack": 6,
                             "Movement": 4, "HP": [3, 3], "Targeting": 5,
                             "Shield": [4, 4], "Cargo": []}
        valid_ship = True
        return valid_ship
    if fighter_ship.upper() == "Z":
        character["Ship"] = {"Name": "F8C - TEST", "Attack": 100,
                             "Movement": 100, "HP": [100, 100], "Targeting": 100,
                             "Shield": [100, 100], "Cargo": []}
        valid_ship = True
        return valid_ship
    else:
        print("Please choose a valid selection")


def choose_explorer_ship(character):
    """
    Selects a ship for the game

    this funtion lets the player select their ship for the game

    :post-condition: a dictionary is added to the character dictionary adding starting ship stats
    :return: a dictionary
    """
    print(character['Stats']['Title'], character["Stats"]["Name"], "Here are your choices for a Fighter ship with "
                                                                   "their respective stats")
    print("CONSTELLATION AQUILA: Attack [7], Movement [5], HP [7], Shield [6], Targeting [7], Cargo Space [2]")
    print("MISC FREELANCER: Attack [6], Movement [5], HP [10], Shield [7], Targeting [6], Cargo Space [2]")
    print("DRAKE CORSAIR: Attack [8], Movement [4], HP [6], Shield [7], Targeting [7], Cargo Space [2]")
    explorer_ship = input("Please select:\n[A] for the CONSTELLATION AQUILA\n"
                          "[F] for the MISC FREELANCER\n[C] for the DRAKE CORSAIR\n")
    if explorer_ship.upper() == "A":
        character["Ship"] = {"Name": "CONSTELLATION AQUILA", "Attack": 7,
                             "Movement": 5, "HP": [7, 7], "Targeting": 7,
                             "Shield": [6, 6], "Cargo": []}
        valid_ship = True
        return valid_ship
    if explorer_ship.upper() == "G":
        character["Ship"] = {"Name": "MISC FREELANCER", "Attack": 6,
                             "Movement": 5, "HP": [10, 10], "Targeting": 6,
                             "Shield": [7, 7], "Cargo": []}
        valid_ship = True
        return valid_ship
    if explorer_ship.upper() == "C":
        character["Ship"] = {"Name": "DRAKE CORSAIR", "Attack": 8,
                             "Movement": 4, "HP": [6, 6], "Targeting": 7,
                             "Shield": [7, 7], "Cargo": []}
        valid_ship = True
        return valid_ship
    if explorer_ship.upper() == "Z":
        character["Ship"] = {"Name": "F8C - TEST", "Attack": 100,
                             "Movement": 100, "HP": [100, 100], "Targeting": 100,
                             "Shield": [100, 100], "Cargo": []}
        valid_ship = True
        return valid_ship
    else:
        print("Please choose a valid selection")
