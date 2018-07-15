from game_classes import *
from file_manager import *


def starting_menu():
    print("Welcome to Nightfall... The path that lies ahead is dark "
          "and full of terrors.")

    invalid_selection = True

    while invalid_selection:
        print("Starting Menu:")
        print("    Start New Game")
        print("    Load Game File")
        print("    Quit Game")
        print("Please select an option by entering:")
        print("Start, Load, or Quit")

        # should we use input() or raw_input()?
        menu_choice = raw_input().lower().strip()

        if menu_choice != "load" and menu_choice != "start" and
        menu_choice != "quit":
            print("You entered an invalid option!")

        else:
            invalid_selection = False

    return menu_choice


def choose_character():
    print("Before embarking on this tumultuous adventure, "
          "please would you like to play as a fear")


def game_menu():  # we need to add a command that brings up the game menu
    invalid_selection = True

    while invalid_selection:
        print("Game Menu: ")
        print("    Save Game File ")
        print("    Return to Game ")
        print("    Quit Game ")
        print("Please select an option by entering: ")
        print("Save, Return, or Quit ")

        # should we use input() or raw_input()?
        menu_choice = raw_input().lower().strip()

        if menu_choice != "save" and menu_choice != "return" and
        menu_choice != "quit":
            print("You entered an invalid option! ")

        else:
            invalid_selection = False

        if menu_choice == "save":
            print("Saving the current game... ")
            # save the game
            print("Game state successfully saved! ")

        elif menu_choice == "quit":
            print("Thank you for playing Nightfall. "
                  "Have a fortuitous evening... ")
            exit()

        else:
            print("Returning to the game!")


def travel(current_room, direction):
    """Move player from one room to another."""
    player = current_room.get_player()

    if direction in current_room.get_door_map():
        if current_room.is_locked(direction):
            print("That door is locked")
        else:
            print("OK")

            current_room.set_player(None)

            new_room_name = current_room.get_adjacent_room(direction)

            new_room = load_object(new_room_name)

            new_room.set_player(player)

            return new_room
    else:
        print('Not possible.')


def start_game():
    """Create game files, load initial room, and load player."""
    init_game_files()

    current_room = load_object("dungeon_entrance")

    player = load_object("player")

    current_room.set_player(player)

    return current_room


def take_action(current_room, action):
    """From action list call the right function."""
    if action[0] == 'travel':
        return travel(current_room, action[1])
    elif action[0] == 'inspect':
        player = current_room.get_player()

        player.inspect(action[1])


def is_game_over(player):
    """Checks to see if the player still has lives."""
    if player.get_lives() > 0:
        return False
    if player.rescue_evelyn is False:
        return False
    else:
        return True