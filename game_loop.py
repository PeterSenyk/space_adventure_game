import actions
import boards
import checks
import events
import start_game


def level_one(character):
    """
    executes the first level of the game.

    this functions runs the first level of the game where the player must defeat enemies or dodge debris.

    :param character: a dictionary of the player character information.
    :precondition: character dictionary should have a name input by the player
    :post-condition: Completes level one of the game and updates the character's title to 'Fighter Pilot'.
    """
    space = boards.make_space(5, 5, 1, 4)
    level_one_goal = False
    print(f"Welcome to training {character['Stats']['Title']} {character['Stats']['Name']}\nIn order to "
          f"complete your training you will need to achieve a combined total of 4 hostiles defeated and/or "
          f"debris dodged")
    while checks.is_alive(character) and not level_one_goal:
        actions.choose_an_action(character, space, 5, 5)
        level_one_goal = checks.level_one_goal(character)
    if not checks.is_alive(character):
        return False
    else:
        print("Congratulations you've completed level one !\n You've achieved the title of Fighter Pilot\nYou're being "
              "deployed to the Out-Land Quadrant to help deal with the space pirate issue that they're experiencing")
        character["Stats"]["Title"] = "Fighter Pilot"
        return True


def level_two(character):
    """
    executes the second level of the game.

    this functions runs the second level of the game where the player retrieves and returns a stolen item.

    :param character: a dictionary of the player character information.
    :precondition: character dictionary should be updated from level one.
    :post-condition: Completes level one of the game and updates the character's title to 'Captain'.
    """
    character["Coordinates"]["X-coordinate"] = 0
    character["Coordinates"]["Y-coordinate"] = 2
    print("Before you deploy were setting you up with a brand new Fighter Class ship")
    start_game.choose_fighter_ship(character)
    out_land_space = boards.make_space(7, 7, 4, 8)
    out_land_space[(0, 2)] = [70, "You're in Arc-Corp station AD-V09 in the outskirts of the 'Out-land Quadrant'",
                              "\033[32m\033[40mAC9\033[m"]
    out_land_space[(2, 6)] = [59, "You see Arc-Corp Station 7, Return the stolen tech here",
                              "\033[32m\033[40mAC7\033[m"]
    out_land_space[(6, 5)] = [60, "You find the crew responsible for the theft from the Arc-Corp R&D station",
                              "\033[31m\033[40m<$>\033[m"]
    level_two_goal = False
    print(f"Welcome to the Out-Land Quadrant {character['Stats']['Title']} {character['Stats']['Name']}\nYour mission "
          f"is to destroy the space pirate who stole the new Quantum Tech from our outpost, beware of the hazards on "
          f"the way")
    while checks.is_alive(character) and not level_two_goal:
        actions.choose_an_action(character, out_land_space, 7, 7)
        level_two_goal = checks.level_two_goal(character)
    if not checks.is_alive(character):
        return False
    else:
        print("Congratulations you've completed level two !\n You've achieved the title of Captain")
        character["Stats"]["Title"] = "Captain"
        return True


def level_three(character):
    """
    executes the third level of the game.

    this functions runs the third level of the game where the player investigates a space anomaly.

    :param character: a dictionary of the player character information.
    :precondition: character dictionary should be updated from level two.
    :post-condition: Completes level one of the game and updates the character's title to 'Admiral'.
    """
    character["Coordinates"]["X-coordinate"] = 4
    character["Coordinates"]["Y-coordinate"] = 6
    print("You're going to need an Explorer Class ship to investigate the ANOMALY")
    start_game.choose_explorer_ship(character)
    anomaly_space = boards.make_space(8, 8, 4, 16)
    anomaly_space[(0, 2)] = [99, "You reach the site of the ANOMALY\nYour sensors display what appears to be fractal "
                                 "white noise\nAt the center of the distortion the sensors cannot resolve anything "
                                 "resembling normal space\nThe reading on your sensors shows that you're approaching "
                                 "the center of the ANOMALY", "\033[30m\033[44m @ \033[m"]
    level_three_goal = False
    print(f"Welcome to the Out-Land Quadrant {character['Stats']['Title']} {character['Stats']['Name']}\n ")
    while checks.is_alive(character) and not level_three_goal:
        actions.choose_an_action(character, anomaly_space, 7, 7)
        level_three_goal = checks.level_three_goal(character)
    if not checks.is_alive(character):
        return False
    else:
        events.anomaly()
        return True
