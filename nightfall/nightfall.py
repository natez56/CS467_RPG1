from game_methods import *
from text_parser import *


def main():
    # Run the starting menu of the game and start, load, or exit the game
    starting_selection = starting_menu()

    if starting_selection == "start":
        # need to add Ranger and Wizard class to intialize
        character_choice = choose_character()

        player_name = choose_name(character_choice)

        # set up the game and use the name chosen by the player for
        # their character
        current_room = start_game(player_name)

        player = current_room.get_player()

        print("Initial location: {}".format(current_room.get_name()))

    elif starting_selection == "load":
        current_room = initial_load_game()

        player = current_room.get_player()
    else:
        print("\nThank you for playing Nightfall. "
              "Have a fortuitous evening. \n")
        exit()

    while not is_game_over(player):
        print("\nWhat would you like to do? ")

        # Grab the command from the user and execute the action if valid
        user_input = get_input()

        action = parse_input(user_input)

        # Handle the user command
        print(action)  # DELETE THIS LINE AFTER TESTING 6879076890768968907689
        current_room = get_current_room()
        print("Current room " + current_room.get_name())  # DELETE THIS LATER

        # Handle any error output
        if action["error"] is not None:
            print(action["error"])

        # Handle the standard actions
        elif action["standard_action"] is not None:
            handle_standard_action(current_room, player, action)

        # Handle the directions
        elif action["direction"] is not None:
            # Handle room names
            if action["direction"] != "north" and \
               action["direction"] != "east" and \
               action["direction"] != "south" and \
               action["direction"] != "west":
                desired_room = action["direction"]

                adjacent_rooms = current_room.get_adjacent_rooms()
                direction = ""

                if desired_room in adjacent_rooms.values():
                    # Get the key to get the direction
                    for key in adjacent_rooms.keys():
                        if adjacent_rooms[key] == desired_room:
                            direction = key

                    if direction != "":
                        current_room = travel(current_room, direction)
                    else:
                        print("That room is not connected to the "
                              "current room!")

            else:
                current_room = travel(current_room, action["direction"])
                # PROBLEM: THE PLAYER IS NOT CURRENTLY MOVING TO THE NEW ROOM

        # current_room = take_action(current_room, action)

        # print("Current room is now: {}".format(current_room.get_name()))


if __name__ == "__main__":
    main()
