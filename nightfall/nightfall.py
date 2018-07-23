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

        # print("Initial location: {}".format(current_room.get_name()))
        # Print out room description.
        if player.has_memory(current_room.get_name()):
            print(current_room.get_short_description())

        else:
            player.add_memory(current_room.get_name())

            print(current_room.get_description())

        print_item_descriptions(current_room)

        save_object_state(current_room)

    elif starting_selection == "load":
        current_room = initial_load_game()

        player = current_room.get_player()

        if player.has_memory(current_room.get_name()):
            print(current_room.get_short_description())
        else:
            print(current_room.get_description())

        print_item_descriptions(current_room)
    else:
        print("\nThank you for playing Nightfall. "
              "Have a fortuitous evening. \n")
        exit()

    while not is_game_over(player):
        current_room = get_current_room()

        print("\nWhat would you like to do? ")

        # Grab the command from the user and execute the action if valid
        user_input = get_input()

        action = parse_input(user_input)

        take_action(current_room, action)

        # Handle the user command
        # print(action)  # DELETE THIS LINE AFTER TESTING 6879076890768968907689

        # print("Current room " + current_room.get_name())  # DELETE THIS LATER


if __name__ == "__main__":
    main()
