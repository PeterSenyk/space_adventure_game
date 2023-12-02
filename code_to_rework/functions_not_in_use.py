# """
# These functions are not currently being used
# """
#
# def game(): # backup for re-work
#     """
#     runs the game
#     """
#     rows = 6
#     columns = 6
#     space = boards.make_space(rows, columns)
#     player_stats = pilot.make_player()
#     player_ship = pilot.select_ship(player_stats)
#     character = {"Stats": player_stats, "Ship": player_ship, "Coordinates": {"X-coordinate": 0, "Y-coordinate": 0}}
#     achieved_goal = False
#     boards.describe_current_location(space, character)
#     print(f"You're in the top-left hand corner of this quadrant [grid (0,0)], the goal is at the "
#           f"bottom-right [gird ({rows - 1},{columns - 1})")
#     while checks.is_alive(character) and not achieved_goal:
#         actions.choose_an_action(character, space, rows, columns)
#         achieved_goal = checks.check_if_goal_attained(rows, columns, character)
#     if character["HP"] <= 0:
#         print("You died\nGAME OVER")
#
#
# # Use this for player name ?
# def capitalize_name(name):
#     if len(name.strip()) == 0:
#         raise ValueError('No empty names allowed!')
#     else:
#         return name.title()
#
#
# def makename():
#     capitalized_name = capitalize_name("nicole paige brookes")
#     print(capitalized_name)
#
#     try:
#         another_capitalized_name = capitalize_name("")
#     except ValueError as e:
#         print(e)
#     else:
#         print(another_capitalized_name)
#
#
# # REWORK ATTACK ---- break into atomic function, add Shields, Miss
# # def attack(character, challenger):
# #     if compare_ships(character, challenger):
# #         challenger["HP"] -= character["Ship"]["Attack"]
# #         print("You attack the enemy\ntheir HP= ", challenger["HP"])
# #         if challenger["HP"] < 1:
# #             print("You destroyed the hostile ship")
# #             # character["Stats"]["Ships Destroyed"] += 1  #### add this later ?
# #             return
# #         else:
# #             character["Ship"]["HP"] -= challenger["Attack"]
# #             print("The enemy ship attacks!\nYour HP= ", character["Ship"]["HP"])
# #             return
# #     else:
# #         character["Ship"]["HP"] -= challenger["Attack"]
# #         print("The enemy ship attacks!\nYour HP= ", character["Ship"]["HP"])
# #         if not is_alive(character):
# #             print("You have been destroyed")
# #             return
# #         else:
# #             challenger["HP"] -= character["Ship"]["Attack"]
# #             print("You attack the enemy!\ntheir HP= ", challenger["HP"])
# #             if challenger["HP"] < 1:
# #                 print("You destroyed the hostile ship")
# #                 # character["Stats"]["Ships Destroyed"] += 1  #### add this later ?
# #                 return
#
# import random as r
# import events
#
#
# # def check_if_goal_attained(rows, columns, character):
# #     """
# #     Checks if the game has been won
# #
# #     this function checks to see if the player had completed the goal of getting to the top right grid point
# #
# #     :param rows: a positive integer
# #     :param columns: a positive integer
# #     :param character: a dictionary of character location and HP
# #     :precondition: achieved_goal must start as false
# #     :post-condition: The function will change the value of achieved_goal to True, ending the game
# #     :return: Boolean value True
# #     """
# #     if (character["Coordinates"]["X-coordinate"], character["Coordinates"]["Y-coordinate"]) == (rows - 1, columns - 1):
# #         print("congrats you win")
# #         return True
# #     else:
# #         return False
#
#
# def is_alive(ship):
#     """
#     Checks if the player is still alive
#
#     this function checks if the characters HP value is above zero
#
#     :param ship: a dictionary of character location and HP
#     :precondition: character HP value must start above zero
#     :return: Boolean True of False
#     """
#     if ship["Ship"]["HP"][0] <= 0:
#         return False
#     else:
#         return True
#
#
# # def check_for_challenger():
# #     """
# #     Checks if there is a challenger at the character location
# #
# #     this functions checks if there's a challenger by chance by using a random integer between 1-4 inclusive
# #
# #     post-condition: if the random integer is 1, there will be a challenger at the character location
# #     :return: Boolean True
# #     """
# #     if r.randint(1, 4) == 1:
# #         return True
#
#
# def check_character_coordinates(character):
#     """
#     Checks the characters coordinates
#
#
#     :param character: character dictionary must be created
#     :precondition:
#     :post-condition: character coordinates are simplified into a tuple
#     :return: 2 integers
#     """
#     character_coordinates = (character["Coordinates"]["X-coordinate"], character["Coordinates"]["Y-coordinate"])
#     return character_coordinates
#
#
# def check_for_event(character, space_tile):
#     coordinates = check_character_coordinates(character)
#     event_chance = r.randint(1, 4)
#     if space_tile[coordinates][0] == 6:
#         if event_chance <= 2:
#             events.asteroid_belt(character)
#         if event_chance == 3:
#             combatant = combat.construct_hostile_ship()
#             combat.space_combat(character, combatant)
#
#
# def training_goal(character):
#     if character["Stats"]["Accolades"]["Ships Destroyed"] >= 3:
#         return True
#     else:
#         return False
#
#
#
#
# # def asteroid_damage(character):
# #     if character["Ship"]["Shield"][0] > 0:
# #         character["Ship"]["Shield"][0] -= 1
# #         print("The Shields reflect 1 damage")
# #     elif character["Ship"]["Shield"][0] <= 0 < character["Ship"]["HP"]:
# #         character["Ship"]["HP"] -= 1
# #         print("The hull takes 1 damage")
# #     else:
# #         print("You hit an asteroid head on, your ship is reduced to ashes and dust")
#
#
#
# def guessing_game(character):
#     """
#     Challenges the character to a guessing game
#
#     this function creates a random number between 1-5 inclusive, and asks the character to guess
#
#     :param character: a dictionary of character location and HP
#     :precondition: character must have an HP value of 1 or greater
#     :post-condition: if the character guesses correctly they move on, if they guess wrong they loose 1 HP
#     :return: a string based on whether the character guessed right or wrong
#     """
#     number_to_guess = r.randint(1, 5)
#     player_guess = int(input("A challenger approaches... Test your luck and guess a number between 1 & 5 :\n"))
#     if player_guess == number_to_guess:
#         print("Lucky guess, this time...  HP=", character["Ship"]["HP"])
#         return character["Ship"]["HP"]
#     else:
#         character["Ship"]["HP"] -= 1
#         print("Wrong! the number was", number_to_guess, "Your HP =", character["Ship"]["HP"])
#         return character["Ship"]["HP"]



# def populate_space():
#     """
#     Makes descriptions of space tiles
#
#     this function assigns room descriptions to the grid by using random numbers
#
#     :post-condition: returns a random room description in a list, with an integer allocated to it
#     :return: a list
#     """
#     space_randomizer = r.randint(1, 10)
#     if space_randomizer == 1:
#         space_tile = [1, "You are in an asteroid belt, there are asteroids everywhere! Travel carefully."]
#         return space_tile
#     if space_randomizer == 2:
#         space_tile = [2, "You are orbiting the dark side of a moon, You think of the legendary "
#                          "ancient ballads of Pink Floyd."]
#         return space_tile
#     if space_randomizer == 3:
#         space_tile = [3, "You come across a ship wreck, You start to wonder who could have caused this."]
#         return space_tile
#     if space_randomizer == 4:
#         space_tile = [4, "You see the abandoned ArcCorp Space Station, You wonder what could have been left behind."]
#         return space_tile
#     if space_randomizer >= 5:
#         space_tile = [5, "You are in the void of space, the sheer amount of nothingness is eerie."]
#         return space_tile

# def check_space_tile(character, space):
#     coordinates = get_player_coordinates(character)
#     tile_event_number = space[coordinates][0]
#     if tile_event_number == 3:
#         print("You see a training hostile")
#         hostile_ship = combat.construct_training_hostile()
#         combat.space_combat(character, hostile_ship)
#     if tile_event_number == 4:
#         print("Try to dodge the debris if you can")
#         correct_route = r.randint(1, 3)
#         choice = int(input("Choose a heading to avoid the debris, your choices are:\n [1] [2] or [3]\n"))
#         if choice in [1, 2, 3]:
#             if choice == correct_route:
#                 print("You avoided the debris !")
#                 combat.shield_recharge(character)
#                 if "Debris Avoided" not in character:
#                     character["Stats"]["Accolades"]["Debris Avoided"] = 1
#                 else:
#                     character["Stats"]["Accolades"]["Debris Avoided"] += 1
#             else:
#                 print("You collide with the debris")
#                 combat.deal_other_damage(character, 1)
#         else:
#             print("Choose a valid route")



# def move_character(character, direction):
#     """
#     Changes the characters X or Y coordinate
#
#     this function changes the characters X or Y coordinate based on the input
#
#     :param character: a dictionary of character location and HP
#     :param direction: a string
#     :precondition: direction must be a string value of either "n", "s", "e", or "w"
#     :precondition: the move is validated prior to changing the character coordinates
#     :post-condition: the characters coordinates are changed
#     """
#     move_calculator(character, direction)


# def training_space(space_tiles):
#     old_training_area = {
#         (0, 0): space_tiles[1], (1, 0): space_tiles[2],
#         (0, 1): space_tiles[3], (1, 1): space_tiles[2],
#         (0, 2): space_tiles[3], (1, 2): space_tiles[3],
#     }
#     return old_training_area