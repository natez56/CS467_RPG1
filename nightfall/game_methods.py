from game_classes import *
from file_manager import *
from feature_handler import *
from item_handler import *
from random import *


def starting_menu():
    """Creates menu viewed when game first starts.

    Returns:
        str: A string that is the menu option chosen by the user.

    """
    # Intro message printed for user at start of game.
    print("\nOh no! While wandering the woods of Tardatheon, your younger "
          "brother Evelyn was snatched by the evil warlock, Zlor. Following "
          "your brother’s screams, you race through the thick brambles and "
          "branches of the forest as they whip and slash against your skin. "
          "All of a sudden, you find yourself in front of the warlock’s "
          "looming tower. \n")

    print("Zlor is holding your brother hostage here. All you have is the "
          "knapsack on your back and a fearless spirit, but you must carry "
          "on and save your brother.\n ")

    print("Welcome to Nightfall. The path that lies ahead is dark and full of "
          "terrors.\n")

    # Check user input for valid menu option.
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
    """Function to select Wizard or Ranger as character.

    Returns:
        str: A string that is Wizard or Ranger.

    """
    print("\nBefore embarking on this tumultuous adventure, "
          "would you like to play as a fearless Ranger \n"
          "or a brilliant Wizard? ")

    invalid_selection = True

    # Validate user input to ensure it is either ranger or wizard.
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
    """Ask user to enter their character name.

    Args:
        character_choice (str): String that is either Wizard or Ranger.

    Returns:
        str: The name the player entered for themselves.

    """
    print("\nExcellent choice! I am sure your %s will make a fine adventurer."
          "\nWhat would you like to name your %s? " % (character_choice,
                                                       character_choice))

    player_name = input().strip()

    print("\nSalutations %s! It is now time to embark on the adventure...\n"
          % (player_name))

    return player_name


def game_menu(current_room):
    """Calls in game menu for use during play.

    Args:
        current_room (:obj:Room): The current room that the player is in.

    """
    invalid_selection = True

    # Validate user menu selection.
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
        load_game()

        room = get_current_room()
        player = room.get_player()

        # Print out room description.
        if player.has_memory(room.get_name()):
            print(room.get_short_description())

        else:
            # If this is the players first time in a room, store the room name
            # so that the short form description can be used next time.
            player.add_memory(room.get_name())

            print(room.get_description())

        print_item_descriptions(room)

    elif menu_choice == "quit":
        print("\nThank you for playing Nightfall. "
              "Have a fortuitous evening... \n")
        exit()

    else:
        print("Returning to the game!")


def help_menu():
    """Print a list of available commands for the user."""
    print("\nHere is a list of available commands: ")

    print("take <item>")
    print("use <item>")
    print("drop <item>")
    print("go <direction>")
    print("look at <feature>")
    print("look at <item>")
    print("eat <feature>")
    print("eat <item>")
    print("drink <feature>")
    print("drink <item>")
    print("smell <feature>")
    print("listen to <feature>")
    print("climb <feature>")
    print("duck")


def take_action(current_room, action):
    """Handles parsed input to perform actions in game.

    Args:
        current_room (:obj:Room): Current room that the player is in.
        action (dictionary(str, str)): A dictionary mapping possible actions
            to either features or items.

    """
    player = current_room.get_player()

    # Handle any error output.
    if action["error"] is not None:
        print(action["error"])

    # Handle the standard actions.
    elif action["standard_action"] is not None:
        return handle_standard_action(current_room, player, action)

    # Handle the directions to pass correct arguments to travel function.
    elif action["direction"] is not None:
        # Check for room 2 rope trap trigger.
        if (current_room.get_name() == "entrance hall" and
            (action["direction"] == 'east' or
             action["direction"] == "mess hall") and
           (current_room.get_puzzle_status("rope") or
           "rope" in current_room.get_features())):

            rope_trap(current_room)

        # Handle input indicating character wants to move rooms.
        elif action["direction"] != "north" and \
                action["direction"] != "east" and \
                action["direction"] != "south" and \
                action["direction"] != "west":

            desired_room = action["direction"]

            # Get list of rooms connected to the current room.
            adjacent_rooms = current_room.get_adjacent_rooms()

            direction = ""

            if desired_room in adjacent_rooms.values():
                # Get the key to get the direction.
                for key in adjacent_rooms.keys():
                    if adjacent_rooms[key] == desired_room:
                        direction = key

                if direction != "":
                    travel(current_room, direction)
                else:
                    print("That room is not connected to the "
                          "current room!")

        else:
            travel(current_room, action["direction"])

    # Handle player / feature interaction for a given room.
    elif (action["verb"] is not None and
          action["feature"] is not None and
          action["feature"] in current_room.get_features()):

        if current_room.get_name() == "fortress entrance":
            room_1_feature_handler(current_room, action["verb"],
                                   action["feature"])

        elif current_room.get_name() == "entrance hall":
            room_2_feature_handler(current_room, action["verb"],
                                   action["feature"])

        elif current_room.get_name() == "mess hall":
            room_3_feature_handler(current_room, action["verb"],
                                   action["feature"])

        elif current_room.get_name() == "store room":
            room_4_feature_handler(current_room, action["verb"],
                                   action["feature"])

        elif current_room.get_name() == "kitchen":
            room_5_feature_handler(current_room, action["verb"],
                                   action["feature"])

        elif current_room.get_name() == "washroom":
            room_6_feature_handler(current_room, action["verb"],
                                   action["feature"])

        elif current_room.get_name() == "smoking room":
            room_7_feature_handler(current_room, action["verb"],
                                   action["feature"])

        elif current_room.get_name() == "sleeping chambers":
            room_8_feature_handler(current_room, action["verb"],
                                   action["feature"])

        elif current_room.get_name() == "supplies closet":
            room_9_feature_handler(current_room, action["verb"],
                                   action["feature"])

        elif current_room.get_name() == "sauna room":
            room_10_feature_handler(current_room, action["verb"],
                                    action["feature"])

    # Handle player / item interaction for a given room.
    elif (action["verb"] is not None and action["item"] is not None
          and (action["item"] in player.get_item_names() or
          action["item"] in current_room.get_item_names())):

        if current_room.get_name() == "fortress entrance":
            room_1_item_handler(current_room, action["verb"],
                                action["item"])

        elif current_room.get_name() == "entrance hall":
            room_2_item_handler(current_room, action["verb"],
                                action["item"])

        elif current_room.get_name() == "mess hall":
            room_3_item_handler(current_room, action["verb"],
                                action["item"])

        elif current_room.get_name() == "store room":
            room_4_item_handler(current_room, action["verb"],
                                action["item"])

        elif current_room.get_name() == "kitchen":
            room_5_item_handler(current_room, action["verb"],
                                action["item"])

        elif current_room.get_name() == "washroom":
            room_6_item_handler(current_room, action["verb"],
                                action["item"])

        elif current_room.get_name() == "smoking room":
            room_7_item_handler(current_room, action["verb"],
                                action["item"])

        elif current_room.get_name() == "sleeping chambers":
            room_8_item_handler(current_room, action["verb"],
                                action["item"])

        elif current_room.get_name() == "supplies closet":
            room_9_item_handler(current_room, action["verb"],
                                action["item"])

        elif current_room.get_name() == "sauna room":
            room_10_item_handler(current_room, action["verb"],
                                 action["item"])

    elif action["verb"] == "duck":
        print("You duck quickly and then stand back up.")

    else:
        print("I can't do that.")

    save_object_state(current_room)


def print_item_descriptions(current_room):
    """Prints the descriptions of all of the items in a room.

    Args:
        current_room (:obj:Room): The current room that the player is in.

    """
    # Custom message if there is only one item in the room.
    if len(current_room.get_item_names()) == 1:
        item_list = current_room.get_item_names()

        print("\nAs you enter the area you also notice a {} on the "
              "ground.".format(item_list[0]))

    # Custom message if there is only two items in the room.
    if len(current_room.get_item_names()) == 2:
        item_list = current_room.get_item_names()

        print("\nAs you enter the area you also notice a {} and a {} on "
              "the ground.".format(item_list[0], item_list[1]))

    # Custom message if there is more than two items in the room.
    elif len(current_room.get_item_names()) > 2:
        print("\nAs you enter the area you also notice ")

        for i, item_name in enumerate(current_room.get_item_names()):
            if i == len(current_room.get_item_names()) - 1:
                print("and a {} on the ground.".format(item_name))

            else:
                print("a {},".format(item_name))


def handle_standard_action(current_room, player, action):
    """Handles standard one word game commands.

    Args:
        current_room (:obj:Room): The current room that the player is in.
        player (:obj:Player): The current player.
        action (str): The user entered command to be handled.

    """
    if action["standard_action"] == "gamemenu" or\
       action["standard_action"] == "game menu":
        game_menu(current_room)

    elif action["standard_action"] == "help":
        help_menu()

    # Look always prints the long form room description.
    elif action["standard_action"] == "look":
        print(current_room.get_description())

        print_item_descriptions(current_room)

    elif action["standard_action"] == "inventory":
        if not player.get_inventory():
            print("\nYour backpack is empty!")

        else:
            print("\nYour backpack has: ")

            for item in player.get_inventory():
                print(item.get_name())

            # == Additional feature to be implemented ==
            # equipped_item = player.get_equipped_item()
            # # if equipped_item is not None:
            # #     print("Equipped item: {}".format(equipped_item.get_name()))
            # # else:
            # #     print("Equipped item: None")

    elif action["standard_action"] == "savegame":
        save_game(current_room)

    elif action["standard_action"] == "loadgame":
        if get_num_saved_games() < 1:
            print("\nNo saved games to load.\n")

        else:
            load_game()

            # Get information to print description of current room the player
            # is in.
            room = get_current_room()
            player = room.get_player()

            # Print out room description.
            if player.has_memory(room.get_name()):
                print(room.get_short_description())

            else:
                player.add_memory(room.get_name())

                print(room.get_description())

            print_item_descriptions(room)

    save_object_state(current_room)


def travel(current_room, direction):
    """Move player from one room to another.

    Args:
        current_room (:obj:Room): The current room that the player is in.
        direction (str): Either north, east, south, west.

    """
    if current_room.get_adjacent_room(direction) is not None:
        print("Moving " + direction + " to the " +
              current_room.get_adjacent_room(direction))

        # Check if the door is locked.
        current_door_map = current_room.get_door_map()

        if current_door_map[direction] is False:
            print("\nThe door is unlocked!\n")

            # Move the character into the new room.
            player = current_room.get_player()

            current_room.set_player(None)

            # Save state to ensure that player is no longer in old room.
            save_object_state(current_room)

            new_room_name = current_room.get_adjacent_room(direction)

            new_room = load_object(new_room_name)

            new_room.set_player(player)

            # Warlock voice interaction number 1.
            if (new_room.get_name() == "store room" and
               new_room.get_puzzle_status("voice")):
                print("As you walk through the door your vision suddenly goes "
                      "black. A voice enters your mind. It speaks in a low "
                      "raspy growl: \"Ahh it appears I have an intruder. "
                      "Although you cannot see me, I assure you I can see "
                      "you. I am Zlor and this is my fortress. Your brother "
                      "will not be returned. You cannot save him, I will "
                      "make sure of that...\" The voice fades and your vision "
                      "returns. Just as it does, there is a flash of light "
                      "and the sound of the stone floor shifting. "
                      "Dark black vines suddenly shoot up out of the cracks "
                      "in the floor. The vines quickly grow to cover the door "
                      "leading north...Things quite down and you take a look "
                      "around\n")
                new_room.set_puzzle_status("voice", False)

            elif (new_room.get_name() == "sauna room" and
                  new_room.get_puzzle_status("sauna voice")):
                print("As you walk through the door your vision goes black. "
                      "A voice enters your mind. It is the same voice as "
                      "the one you encountered in the store room. It says, "
                      "\"So you've made it this far...I am tired of these "
                      "games. You will go no farther. I have prepared a "
                      "special potion that has been added to the sauna you "
                      "are now in. Do whatever you like, but while the steam "
                      "remains you will not find the way forward.\". The "
                      "voice fades and your vision returns.")
                new_room.set_puzzle_status("sauna voice", False)

            # Print out room description.
            if player.has_memory(new_room_name):
                print(new_room.get_short_description())

            else:
                player.add_memory(new_room_name)

                print(new_room.get_description())

            print_item_descriptions(new_room)

            # Save state so that room tracks player in game files.
            save_object_state(new_room)

        else:
            print("The door is locked!")
            print("You can use a key to unlock the door.")

    else:
        print("There is no room in that direction!")


def combat(player, monster):
    """Function to allow for player monster rpg combat.

    Args:
        player (:obj:Player): The user selected main character.
        monster (:obj:Monster): A character that the player fights.

    """
    # Begin combat dialogue
    print("You have encountered %s! Let's begin combat..." %
          (monster.get_name()))

    combat_continues = True

    while combat_continues:
        # Allow the player to choose their move
        # Output player combat options
        print("\nPlease select which move you want: ")
        player.get_attack_description(0)
        player.get_attack_description(1)
        player.get_attack_description(2)

        # Get the player's choice
        attack_choice = input().lower().strip()

        invalid_choice = True

        while(invalid_choice):
            if attack_choice != 'slash' and attack_choice != 'thunder' and \
               attack_choice != 'singe':
                print("\nYou entered an invalid choice! ")
                print("Please enter: slash, thunder, or sear: ")

                attack_choice = input().lower().strip()
            else:
                invalid_choice = False

        # Execute the player's attack
        total_damage = player.execute_attack(attack_choice)

        if total_damage == 0:
            print("You missed! ")
        else:
            # Deal the damage to the enemy
            print("\nYou did %d damage! " % (total_damage))
            current_monster_health = monster.get_health()
            monster.set_health(current_monster_health-total_damage)

        # Check if the enemy is dead, if so, exit combat and gain experience
        if monster.get_health() <= 0:
            print("\nYou have slain %s" % (monster.get_name()))

            experience_gained = monster.get_loot()
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
            # return False

    return True


def start_game(player_name):
    """Create game files, load initial room, and load player.

    Args:
        player_name (str): The user selected main character name.

    Returns:
        :obj:Room: The current room that the player is in.

    """
    init_game_files(player_name)

    current_room = load_object("fortress_entrance")

    return current_room


def is_game_over(player):
    """Checks to see if the player still has lives.

    Args:
        player (:obj:Player): The main character of the game.

    Returns:
        bool: False if the character is dead or the game is complete.

    """
    if player.get_lives() > 0:
        return False

    if player.rescue_evelyn is False:
        return False

    else:
        return True
