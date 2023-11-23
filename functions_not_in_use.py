"""
These functions are not currently being used
"""


# Use this for player name ?
def capitalize_name(name):
    if len(name.strip()) == 0:
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