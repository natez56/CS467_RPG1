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
        print("Thank you for playing Nightfall. "
              "Have a fortuitous evening. ")
        exit()

    while not is_game_over(player):
        print("What would you like to do? ")

        user_input = get_input()

        action = parse_input(user_input)
        # add functionality to run game menu

        current_room = take_action(current_room, action)

        print("Current room is now: {}".format(current_room.get_name()))


if __name__ == "__main__":
    main()
