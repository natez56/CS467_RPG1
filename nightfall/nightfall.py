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

        # handle the user command
        print(action)
        current_room = get_current_room()

        if action["standard_action"] is not None:
            if action["standard_action"] == "gamemenu" or\
               action["standard_action"] == "game menu":
                game_menu(current_room)
            elif action["standard_action"] == "help":
                help_menu()
            elif action["standard_action"] == "look":
                print(current_room.get_description())
            elif action["standard_action"] == "inventory":
                if not player.get_inventory():
                    print("\nYour backpack is empty!")
                else:
                    print("\nYour backpack has: ")
                    print("\n".join(player.get_inventory()))

        # current_room = take_action(current_room, action)

        # print("Current room is now: {}".format(current_room.get_name()))


if __name__ == "__main__":
    main()
