import actions
import boards
import checks


def level_one_loop(character):
    space = boards.make_space(5, 5, 2, 4)
    level_one_goal = False
    while checks.is_alive(character) and not level_one_goal:
        actions.choose_an_action(character, space, 5, 5)
        level_one_goal = checks.level_one_goal(character)
    if not checks.is_alive(character):
        print("Your ship exploded !\nGame Over")
    else:
        print("Congratulations you've completed level one !")
        character["Stats"]["Title"] = "Fighter Pilot"
        print(character)
