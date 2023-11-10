import random as r

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

