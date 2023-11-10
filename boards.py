import random as r

def scan_space_grid(rows, columns, space, character):
    for row in range(rows):
        for column in range(columns):
            if column == character["Coordinates"]["X-coordinate"] and row == character["Coordinates"]["Y-coordinate"]:
                print(" X ", end="")
            elif column == columns - 1 and row == rows - 1:
                print(" $ ")
            elif space[(row, column)].get[0] == 1:
                print(":.'", end="")
            elif space[(row, column)][0] == 2:
                print(" o ", end="")
            else:
                print(" - ", end="")
        print()


def describe_current_location(rows, columns, space, character):

    location_of_character = [character["Coordinates"].get("X-coordinate"), character["Coordinates"].get("Y-coordinate")]
    location_key = tuple(location_of_character)
    scan_space_grid(rows, columns, space, character)
    return print(f"You're current coordinates are: ", location_of_character, "\nYou see :", space.get(location_key))


def populate_space():

    space_randomizer = r.randint(1, 10)
    if space_randomizer == 1:
        space_tile = [1, "You are in an asteroid belt, there are asteroids everywhere! Travel carefully."]
        return space_tile
    if space_randomizer == 2:
        space_tile = [2, "You are orbiting the dark side of a moon, You think of the legendary "
                         "ancient ballads of Pink Floyd."]
        return space_tile
    if space_randomizer == 3:
        space_tile = [3, "You come across a ship wreck, You start to wonder who could have caused this."]
        return space_tile
    if space_randomizer == 4:
        space_tile = [4, "You see the abandoned ArcCorp Space Station, You wonder what could have been left behind."]
        return space_tile
    if space_randomizer >= 5:
        space_tile = [5, "You are in the void of space, the sheer amount of nothingness is eerie."]
        return space_tile


def make_space(rows, columns):

    new_space = {(0,0): "You are in the Crusader Command Station"}
    for column in range(rows):
        for row in range(columns):
            new_space[(column, row)] = populate_space()
    return new_space


def game():
    rows = 4
    columns = 4
    space = make_space(rows, columns)
    print(space[0, 1][0])
    print(space[0, 2][0])
    print(space[0, 3][0])
    return


def main():
    game()


if __name__ == "__main__":
    main()
