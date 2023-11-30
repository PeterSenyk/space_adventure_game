import random as r
import combat

def training_combat(character):
    print("You see a training hostile")
    hostile_ship = combat.construct_training_hostile()
    combat.space_combat(character, hostile_ship)


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
            asteroid_damage(character)


def asteroid_damage(character):
    if character["Ship"]["Shield"][0] > 0:
        character["Ship"]["Shield"][0] -= 1
        print("The Shields reflect 1 damage")
    elif character["Ship"]["Shield"][0] <= 0 < character["Ship"]["HP"]:
        character["Ship"]["HP"] -= 1
        print("The hull takes 1 damage")
    else:
        print("You hit an asteroid head on, your ship is reduced to ashes and dust")


def clean_asteroid_game_direction(direction):
    if direction.upper() == "W":
        return 1
    elif direction.upper() == "S":
        return 2
    elif direction.upper() == "A":
        return 3
    elif direction.upper() == "D":
        return 4


def guessing_game(character):
    """
    Challenges the character to a guessing game

    this function creates a random number between 1-5 inclusive, and asks the character to guess

    :param character: a dictionary of character location and HP
    :precondition: character must have an HP value of 1 or greater
    :post-condition: if the character guesses correctly they move on, if they guess wrong they loose 1 HP
    :return: a string based on whether the character guessed right or wrong
    """
    number_to_guess = r.randint(1, 5)
    player_guess = int(input("A challenger approaches... Test your luck and guess a number between 1 & 5 :\n"))
    if player_guess == number_to_guess:
        print("Lucky guess, this time...  HP=", character["Ship"]["HP"])
        return character["Ship"]["HP"]
    else:
        character["Ship"]["HP"] -= 1
        print("Wrong! the number was", number_to_guess, "Your HP =", character["Ship"]["HP"])
        return character["Ship"]["HP"]
