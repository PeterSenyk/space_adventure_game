def select_ship(player_stats):
    """
    Selects a ship for the game

    this funtion lets the player select their ship for the game

    :post-condition: a dictionary is added to the character dictionary adding starting ship stats
    :return: a dictionary
    """
    print(player_stats["Name"], "Here are your choices for a ship")
    print("ANVIL ARROW: Attack [1], Movement [3], HP [5], Shield [2], Targeting [4], Cargo Space [2]")
    print("AEGIS GLADIUS: Attack [2], Movement [2], HP [5], Shield [2], Targeting [4], Cargo Space [2]")
    print("DRAKE BUCCANEER: Attack [3], Movement [2], HP [4], Shield [1], Targeting [5], Cargo Space [2]")
    new_ship = input("Please select:\n[A] for the ANVIL ARROW\n"
                     "[G] for the AEGIS GLADIUS\n[B] for the DRAKE BUCCANEER\n")
    if new_ship.upper() == "A":
        return {"Ship": "ANVIL ARROW", "Attack": 1,
                "Movement": 3, "HP": 5, "Targeting": 4,
                "Shield": [2, 2], "Cargo": []}
    if new_ship.upper() == "G":
        return {"Ship": "AEGIS GLADIUS", "Attack": 2,
                "Movement": 2, "HP": 5, "Targeting": 4,
                "Shield": [2, 2], "Cargo": []}
    if new_ship.upper() == "B":
        return {"Ship": "DRAKE BUCCANEER", "Attack": 3,
                "Movement": 2, "HP": 4, "Targeting": 4,
                "Shield": [2, 2], "Cargo": []}


def make_player():
    """
    Makes a character

    this function makes a character based on player input

    :post-condition: a character dictionary is completed with starting coordinates and HP
    :return: a dictionary
    """
    player_name_input = input("Please type your last name\n")
    player_last_name = player_name_input
    player_titles = ["Trainee", "Pilot", "Captain"]
    print(f"Congratulations {player_titles[0]} {player_last_name} on graduating the Space Academy at the top of your class\n")
    player_stats = {"Name": player_last_name, "Accolades": {"Credits": 1000, "Ships Destroyed": 0}}
    return player_stats