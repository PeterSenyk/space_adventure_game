import actions
import boards
import checks
import start_game


def level_one(character):
    space = boards.make_space(5, 5, 2, 4)
    level_one_goal = False
    print(f"Welcome to training {character['Stats']['Title']} {character['Stats']['Name']}\nIn order to "
          f"complete your training you will need to achieve a combined total of 4 hostiles defeated and/or "
          f"debris dodged")
    while checks.is_alive(character) and not level_one_goal:
        actions.choose_an_action(character, space, 5, 5)
        level_one_goal = checks.level_one_goal(character)
    if not checks.is_alive(character):
        print("Your ship exploded !\nGame Over")
    else:
        print("Congratulations you've completed level one !\n You've achieved the title of Fighter Pilot\nYou're being"
              "deployed to the Out-Land Quadrant to help deal with the space pirate issue that they're experiencing")
        character["Stats"]["Title"] = "Fighter Pilot"


def level_two(character):
    character["Coordinates"]["X-coordinate"] = 0
    character["Coordinates"]["Y-coordinate"] = 2
    print("Before you deploy were setting you up with a brand new Fighter Class ship")
    start_game.choose_fighter_ship(character)
    outland_space = boards.make_space(7, 7, 5, 8)
    outland_space[(0, 2)] = [10, "You're in Arc-Corp station AD-V09 in the outskirts of the 'Outland Quadrant'", "AC9"]
    outland_space[(2, 6)] = [12, "You see Arc-Corp Station 7, Return the stolen tech here", "AC7"]
    outland_space[(6, 5)] = [11, "You find the crew responsible for the theft from the Arc-Corp R&D station", "<$>"]
    level_two_goal = False
    print(f"Welcome to the Out-Land Quadrant {character['Stats']['Title']} {character['Stats']['Name']}\nYour mission "
          f"is to destroy the space pirate who stole the new Quantum Tech from our outpost, beware of the hazards on "
          f"the way")
    while checks.is_alive(character) and not level_two_goal:
        actions.choose_an_action(character, outland_space, 7, 7)
        level_two_goal = checks.level_two_goal(character)
    if not checks.is_alive(character):
        print("Your ship exploded !\nGame Over")
    else:
        print("Congratulations you've completed level one !\n You've achieved the title of Fighter Pilot")
        character["Stats"]["Title"] = "Fighter Pilot"
