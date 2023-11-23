import boards
import pilot


def start_of_game():
    character_created = False
    character = {"Stats": {"Title": "", "Name": "", "Accolades": []}, "Ship": {}, "Coordinates": {"X-coordinate": 0, "Y-coordinate": 0}}
    while not character_created:
        last_name = get_player_last_name()

    pass


def get_player_last_name():
    last_name = capitalize_name(input("Enter your last name to register for the Arc-Corp Space Academy\n"))



    def capitalize_name(name):
        last_name = name.strip().lower
        if len(last_name) == 0:
            raise ValueError('No empty names allowed!')
        else:
            return name.title()

    def makename():
        capitalized_name = capitalize_name("nicole paige brookes")
        print(capitalized_name)

        try:
            another_capitalized_name = capitalize_name("")
        except ValueError as e:
            print(e)
        else:
            print(another_capitalized_name)
