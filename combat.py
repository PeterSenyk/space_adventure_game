import random as r
from checks import is_alive


def construct_challenger():
    challenger = {"Attack": r.randint(1, 2), "Movement": r.randint(1, 3),
                  "HP": r.randint(1, 2), "Targeting": r.randint(1, 4), "Shield": r.randint(0, 1),
                  "Cargo":  r.randint(0, 1)}
    return challenger


def space_combat(character, challenger):
    print("You come across a hostile ship")
    while is_alive(character) and challenger["HP"] > 0:
        print(character["Ship"]["HP"])
        print(challenger["HP"])
        player_action = input("Choose an action\nA = Attack\nR = Run\nD = Dodge\n")
        if player_action.upper() == "A":
            attack(character, challenger)
        if player_action.upper() == "R":
            run(character, challenger)  # add function
        if player_action.upper() == "D":
            dodge(character, challenger)  # add function


def attack(character, challenger):
    if compare_movement(character, challenger):
        challenger["HP"] -= character["Ship"]["Attack"]
        print("You attack the enemy\ntheir HP= ", challenger["HP"])
        if challenger["HP"] < 1:
            print("You destroyed the hostile ship")
            # character["Stats"]["Ships Destroyed"] += 1  #### add this later ?
            return
        else:
            character["Ship"]["HP"] -= challenger["Attack"]
            print("The enemy ship attacks!\nYour HP= ", character["Ship"]["HP"])
            return
    else:
        character["Ship"]["HP"] -= challenger["Attack"]
        print("The enemy ship attacks!\nYour HP= ", character["Ship"]["HP"])
        if not is_alive(character):
            print("You have been destroyed")
            return
        else:
            challenger["HP"] -= character["Ship"]["Attack"]
            print("You attack the enemy!\ntheir HP= ", challenger["HP"])
            if challenger["HP"] < 1:
                print("You destroyed the hostile ship")
                # character["Stats"]["Ships Destroyed"] += 1  #### add this later ?
                return


def compare_movement(character, challenger):
    if character["Ship"]["Movement"] >= challenger["Movement"]:
        return True
    else:
        return False
