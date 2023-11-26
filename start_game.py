import boards
import pilot
import space_ships


def build_character(character):
    get_player_last_name(character)
    print(f"Welcome to the Academy {character['Stats']['Title'][0]} {character['Stats']['Name']}")
    choose_training_ship(character)
    return character


def get_player_last_name(character):
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
    print(character['Stats']['Title'][0], character["Stats"]["Name"], "Here are your choices for a training ship with "
                                                                      "their respective stats")
    print("ANVIL AURORA: Attack [1], Movement [3], HP [5], Shield [2], Targeting [4], Cargo Space [2]")
    print("AEGIS TITAN: Attack [2], Movement [2], HP [5], Shield [2], Targeting [4], Cargo Space [2]")
    print("DRAKE CUTTER: Attack [3], Movement [2], HP [4], Shield [1], Targeting [5], Cargo Space [2]")
    training_ship = input("Please select:\n[A] for the ANVIL AURORA\n"
                          "[G] for the AEGIS TITAN\n[B] for the DRAKE CUTTER\n")
    if training_ship.upper() == "A":
        character["Ship"] = {"Name": "ANVIL ARROW", "Attack": 1,
                             "Movement": 3, "HP": 5, "Targeting": 4,
                             "Shield": [2, 2], "Cargo": []}
    if training_ship.upper() == "G":
        character["Ship"] = {"Name": "AEGIS GLADIUS", "Attack": 2,
                             "Movement": 2, "HP": 5, "Targeting": 4,
                             "Shield": [2, 2], "Cargo": []}
    if training_ship.upper() == "B":
        character["Ship"] = {"Name": "DRAKE BUCCANEER", "Attack": 3,
                             "Movement": 2, "HP": 4, "Targeting": 4,
                             "Shield": [2, 2], "Cargo": []}
