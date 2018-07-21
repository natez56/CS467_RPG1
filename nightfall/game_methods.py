from game_classes import *
from file_manager import *
from random import *


def starting_menu():
    print("\nWelcome to Nightfall... The path that lies ahead is dark "
          "and full of terrors.")

    invalid_selection = True

    while invalid_selection:
        print("\nStarting Menu:")
        print("    Start New Game")
        print("    Load Game File")
        print("    Quit Game")
        print("Please select an option by entering:")
        print("Start, Load, or Quit")

        menu_choice = input().lower().strip()

        if menu_choice != "load" and menu_choice != "start" and \
           menu_choice != "quit":
            print("You entered an invalid option!")
        elif menu_choice == 'load' and get_num_saved_games() < 1:
            print("\nNo saved games to load. Select another option.\n")
        else:
            invalid_selection = False

    return menu_choice


def choose_character():
    invalid_selection = True

    print("\nBefore embarking on this tumultuous adventure, "
          "would you like to play as a fearless Ranger \n"
          "or a brilliant Wizard? ")

    while invalid_selection:
        character_choice = input().lower().strip()

        if character_choice != "ranger" and character_choice != "wizard":
            print("\nYou entered an invalid selection, please choose "
                  "between Ranger and Wizard: ")
        else:
            invalid_selection = False

    character_choice = character_choice.capitalize()

    return character_choice


def choose_name(character_choice):
    print("\nExcellent choice! I am sure your %s will make a fine adventurer."
          "\nWhat would you like to name your %s? " % (character_choice,
                                                       character_choice))

    player_name = input().strip()

    print("\nSalutations %s! It is now time to embark on the adventure... "
          % (player_name))

    return player_name


def game_menu(current_room):  # command needed to bring up this menu.
    invalid_selection = True

    while invalid_selection:
        print("\nGame Menu: ")
        print("    Save Game File ")
        print("    Load Game File ")
        print("    Return to Game ")
        print("    Quit Game ")
        print("Please select an option by entering: ")
        print("Save, Return, or Quit ")

        menu_choice = input().lower().strip()

        if menu_choice != "save" and menu_choice != "return" and \
           menu_choice != "quit" and menu_choice != "load":
            print("You entered an invalid option! ")
        elif menu_choice == "load" and get_num_saved_games() < 1:
            print("\nNo saved games to load. Select another option.")
        else:
            invalid_selection = False

    if menu_choice == "save":
        save_game(current_room)

    elif menu_choice == "load":
        current_room = load_game(current_room)

        return current_room
    elif menu_choice == "quit":
        print("\nThank you for playing Nightfall. "
              "Have a fortuitous evening... \n")
        exit()

    else:
        print("Returning to the game!")

    return current_room


def help_menu():
    print("\nHere is a list of available commands: ")
    print("    ")  # ADD A LIST OF VERBS THAT CAN BE USED FOR COMMANDS IN GAME


def handle_standard_action(current_room, player, action):
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


def travel(current_room, direction):  # This will also need to handle room name
    """Move player from one room to another."""
    if current_room.get_adjacent_room(direction) is not None:
        print("\nMoving " + direction + " to the " +
              current_room.get_adjacent_room(direction))

        # Check if the door is locked
        current_door_map = current_room.get_door_map()

        if current_door_map[direction] is False:
            print("The door is unlocked!")

            # Move the character into the new room
            player = current_room.get_player()

            current_room.set_player(None)

            new_room_name = current_room.get_adjacent_room(direction)

            new_room = load_object(new_room_name)

            new_room.set_player(player)

            return new_room

        else:
            print("The door is locked!")
            print("You can use a key to unlock the door.")

    else:
        print("\nThere is no room in that direction!")

    return current_room


def combat(player, monster):
    # Begin combat dialogue
    print("You have encountered %s! Let's begin combat..." %
          (monster.get_name()))

    combat_continues = True

    while combat_continues:
        # Allow the player to choose their move
        print("Please select which move you would like to use: ")
        # Output player combat options

        # Randomize the damage based on the move and applicable equipment

        # Adjust the player's remaining ability count and
        # stats like magic power or health

        # Deal the damage to the enemy

        # Check if the enemy is dead, if so, exit combat and gain experience
        if monster.get_health() <= 0:
            print("You have slain %s" % (monster.name))

            experience_gained = randint(1, 5)
            print("You have gained %d experience points!" %
                  (experience_gained))

            new_experience_total = experience_gained + player.get_experience()

            # Level up the player if they have enough experience
            if new_experience_total >= 10:  # we will need to do balancing!!!
                print("%s has leveled up! " % player.get_name())
                player.level_up()

                # Carry over the excess experience into the new level
                new_experience_total = new_experience_total - 10

            player.set_experience(new_experience_total)

            combat_continues = False

        else:
            # Randomly choose what ability the enemy will use

            # Calculate the damage

            # Check if the player is dead
            # How should we handle player deaths? end combat? reset
            # monster health?
            # should we stay in combat and reset the player's stats and remove
            # 1 life?

            # Check if the game is over or do that in the main game loop?
            pass


def start_game(player_name):
    """Create game files, load initial room, and load player."""
    init_game_files(player_name)

    current_room = load_object("dungeon_entrance")

    return current_room


def take_action(current_room, action):
    """From action list call the right function."""
    if action[0] == 'travel':
        return travel(current_room, action[1])
    elif action[0] == 'inspect':
        player = current_room.get_player()

        player.inspect(action[1])
    elif action[0] == 'menu':
        return game_menu(current_room)


def is_game_over(player):
    """Checks to see if the player still has lives."""
    if player.get_lives() > 0:
        return False
    if player.rescue_evelyn is False:
        return False
    else:
        return True
