from game_methods import *
from text_parser import *


def main():
    # Run the starting menu of the game and start, load, or exit the game
    starting_selection = starting_menu()

    if starting_selection == "start":
        # need to add Ranger and Wizard class to intialize
        character_choice = choose_character()

        # need to add ability for the player name to be stored in the object
        player_name = choose_name(character_choice)

        current_room = start_game()

        player = current_room.get_player()

        print("Initial location: {}".format(current_room.get_name()))

    elif starting_selection == "load":
        print("Please select which game file to load:")
        # add load game functionality
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
