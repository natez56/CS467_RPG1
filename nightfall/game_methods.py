from game_classes import *
from file_manager import *
from feature_handler import *
from item_handler import *
from random import *
from scroll_print import *
import time


def starting_menu():
    """Creates menu viewed when game first starts.

    Returns:
        str: A string that is the menu option chosen by the user.

    """
    # Intro message printed for user at start of game.
    scroll_print("\nOh no! While wandering the woods of Tardatheon, your "
                 "younger brother Evelyn was snatched by the evil warlock, "
                 "Zlor. Following your brother’s screams, you race through "
                 "the thick brambles and branches of the forest as they whip "
                 "and slash against your skin. All of a sudden, you find "
                 "yourself in front of the warlock’s looming tower. \n")

    scroll_print("Zlor is holding your brother hostage here. All you have is "
                 "the knapsack on your back and a fearless spirit, but you "
                 "must carry on and save your brother.\n ")

    scroll_print("Welcome to Nightfall. The path that lies ahead is dark and "
                 "full of terrors.\n")

    # Check user input for valid menu option.
    invalid_selection = True

    while invalid_selection:
        scroll_print("\nStarting Menu:")
        scroll_print("    Start New Game")
        scroll_print("    Load Game File")
        scroll_print("    Quit Game")
        scroll_print("Please select an option by entering:")
        scroll_print("Start, Load, or Quit")

        menu_choice = input().lower().strip()

        if menu_choice != "load" and menu_choice != "start" and \
           menu_choice != "quit":

            scroll_print("You entered an invalid option!")

        elif menu_choice == 'load' and get_num_saved_games() < 1:

            scroll_print("\nNo saved games to load. Select another option.\n")

        else:
            invalid_selection = False

    return menu_choice


def choose_character():
    """Function to select Wizard or Ranger as character.

    Returns:
        str: A string that is Wizard or Ranger.

    """
    scroll_print("\nBefore embarking on this tumultuous adventure, "
                 "would you like to play as a fearless Ranger "
                 "or a brilliant Wizard? ")

    invalid_selection = True

    # Validate user input to ensure it is either ranger or wizard.
    while invalid_selection:
        character_choice = input().lower().strip()

        if character_choice != "ranger" and character_choice != "wizard":
            scroll_print("\nYou entered an invalid selection, please choose "
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
    scroll_print("\nExcellent choice! I am sure your %s will make a fine "
                 "adventurer. What would you like to name your %s? " %
                 (character_choice, character_choice))

    player_name = input().strip()

    scroll_print("\nSalutations %s! It is now time to embark on the "
                 "adventure...\n" % (player_name))

    return player_name


def game_menu(current_room):
    """Calls in game menu for use during play.

    Args:
        current_room (:obj:Room): The current room that the player is in.

    """
    invalid_selection = True

    # Validate user menu selection.
    while invalid_selection:
        scroll_print("\nGame Menu: ")
        scroll_print("    Save Game File ")
        scroll_print("    Load Game File ")
        scroll_print("    Return to Game ")
        scroll_print("    Quit Game ")
        scroll_print("Please select an option by entering: ")
        scroll_print("Save, Return, or Quit ")

        menu_choice = input().lower().strip()

        if menu_choice != "save" and menu_choice != "return" and \
           menu_choice != "quit" and menu_choice != "load":

            scroll_print("You entered an invalid option! ")

        elif menu_choice == "load" and get_num_saved_games() < 1:

            scroll_print("\nNo saved games to load. Select another option.")

        else:
            invalid_selection = False

    if menu_choice == "save":
        save_game(current_room)

    elif menu_choice == "load":
        load_game()

        room = get_current_room()
        player = room.get_player()

        # scroll_print out room description.
        if player.has_memory(room.get_name()):
            scroll_print(room.get_short_description())

        else:
            # If this is the players first time in a room, store the room name
            # so that the short form description can be used next time.
            player.add_memory(room.get_name())

            scroll_print(room.get_description())

        print_item_descriptions(room)

    elif menu_choice == "quit":
        scroll_print("\nThank you for playing Nightfall. "
                     "Have a fortuitous evening... \n")
        exit()

    else:
        scroll_print("Returning to the game!")


def help_menu():
    """scroll_print a list of available commands for the user."""
    scroll_print("\nHere is a list of available commands: ")

    scroll_print("take <item>")
    scroll_print("use <item>")
    scroll_print("drop <item>")
    scroll_print("go <direction>")
    scroll_print("look at <feature>")
    scroll_print("look at <item>")
    scroll_print("eat <feature>")
    scroll_print("eat <item>")
    scroll_print("drink <feature>")
    scroll_print("drink <item>")
    scroll_print("smell <feature>")
    scroll_print("listen to <feature>")
    scroll_print("climb <feature>")
    scroll_print("duck")


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
        scroll_print(action["error"])

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
                    scroll_print("That room is not connected to the "
                                 "current room!")

        else:
            travel(current_room, action["direction"])

    # Handle player / item interaction for a given room.
    elif (action["verb"] is not None and action["item"] is not None
          and (action["item"] in player.get_item_names() or
          action["item"] in current_room.get_item_names())):

        if action["verb"] != "use" and action["feature"] is not None:
            scroll_print("You can't {} {} on {}".format(action["verb"],
                         action["item"],
                         action["feature"]))

        elif current_room.get_name() == "fortress entrance":
            room_1_item_handler(current_room, action["verb"],
                                action["item"], action["feature"])

        elif current_room.get_name() == "entrance hall":
            room_2_item_handler(current_room, action["verb"],
                                action["item"], action["feature"])

        elif current_room.get_name() == "mess hall":
            room_3_item_handler(current_room, action["verb"],
                                action["item"], action["feature"])

        elif current_room.get_name() == "store room":
            room_4_item_handler(current_room, action["verb"],
                                action["item"], action["feature"])

        elif current_room.get_name() == "kitchen":
            room_5_item_handler(current_room, action["verb"],
                                action["item"], action["feature"])

        elif current_room.get_name() == "washroom":
            room_6_item_handler(current_room, action["verb"],
                                action["item"], action["feature"])

        elif current_room.get_name() == "smoking room":
            room_7_item_handler(current_room, action["verb"],
                                action["item"], action["feature"])

        elif current_room.get_name() == "sleeping chambers":
            room_8_item_handler(current_room, action["verb"],
                                action["item"], action["feature"])

        elif current_room.get_name() == "supplies closet":
            room_9_item_handler(current_room, action["verb"],
                                action["item"], action["feature"])

        elif current_room.get_name() == "sauna room":
            room_10_item_handler(current_room, action["verb"],
                                 action["item"], action["feature"])

        elif current_room.get_name() == "tower hall":
            room_11_item_handler(current_room, action["verb"],
                                 action["item"], action["feature"])

        elif current_room.get_name() == "archives":
            room_12_item_handler(current_room, action["verb"],
                                 action["item"], action["feature"])

        elif current_room.get_name() == "reading room":
            room_13_item_handler(current_room, action["verb"],
                                 action["item"], action["feature"])

        elif current_room.get_name() == "room of last rites":
            room_14_item_handler(current_room, action["verb"],
                                 action["item"], action["feature"])

        elif current_room.get_name() == "final lair":
            room_15_item_handler(current_room, action["verb"],
                                 action["item"], action["feature"])

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

        elif current_room.get_name() == "tower hall":
            room_11_feature_handler(current_room, action["verb"],
                                    action["feature"])

        elif current_room.get_name() == "archives":
            room_12_feature_handler(current_room, action["verb"],
                                    action["feature"])

        elif current_room.get_name() == "reading room":
            room_13_feature_handler(current_room, action["verb"],
                                    action["feature"])

        elif current_room.get_name() == "room of last rites":
            room_14_feature_handler(current_room, action["verb"],
                                    action["feature"])

        elif current_room.get_name() == "final lair":
            room_15_feature_handler(current_room, action["verb"],
                                    action["feature"])

    elif action["verb"] == "duck":
        scroll_print("You duck quickly and then stand back up.")

    else:
        scroll_print("I can't do that.")

    save_object_state(current_room)


def print_item_descriptions(current_room):
    """Prints the descriptions of all of the items in a room.

    Args:
        current_room (:obj:Room): The current room that the player is in.

    """
    # Custom message if there is only one item in the room.
    if len(current_room.get_item_names()) == 1:
        item_list = current_room.get_item_names()

        scroll_print("\nAs you enter the area you also notice a {} on the "
                     "ground.".format(item_list[0]))

    # Custom message if there is only two items in the room.
    if len(current_room.get_item_names()) == 2:
        item_list = current_room.get_item_names()

        scroll_print("\nAs you enter the area you also notice a {} and a {} "
                     "on the ground.".format(item_list[0], item_list[1]))

    # Custom message if there is more than two items in the room.
    elif len(current_room.get_item_names()) > 2:
        scroll_print("\nAs you enter the area you also notice ")

        for i, item_name in enumerate(current_room.get_item_names()):
            if i == len(current_room.get_item_names()) - 1:
                scroll_print("and a {} on the ground.".format(item_name))

            else:
                scroll_print("a {},".format(item_name))


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
        scroll_print(current_room.get_description())

        print_item_descriptions(current_room)

    elif action["standard_action"] == "inventory":
        if not player.get_inventory():
            scroll_print("Your backpack is empty!")

        else:
            scroll_print("Your backpack has: ")

            for item in player.get_inventory():
                scroll_print(item.get_name())

            equipped_item = player.get_equipped_item()

            if equipped_item is not None:
                scroll_print("\nEquipped item: {}"
                             .format(equipped_item.get_name()))
            else:
                scroll_print("\nEquipped item: None")

    elif action["standard_action"] == "savegame":
        save_game(current_room)

    elif action["standard_action"] == "loadgame":
        if get_num_saved_games() < 1:
            scroll_print("\nNo saved games to load.\n")

        else:
            load_game()

            # Get information to scroll_print description of current room the
            # player is in.
            room = get_current_room()
            player = room.get_player()

            # scroll_print out room description.
            if player.has_memory(room.get_name()):
                scroll_print(room.get_short_description())

            else:
                player.add_memory(room.get_name())

                scroll_print(room.get_description())

            print_item_descriptions(room)

    elif action["standard_action"] == 'stats' or\
        action["standard_action"] == 'get stats' or\
        action["standard_action"] == 'my stats' or\
            action["standard_action"] == 'player stats':

        room = get_current_room()
        player = room.get_player()

        player.print_stats()

    save_object_state(current_room)


def travel(current_room, direction):
    """Move player from one room to another.

    Args:
        current_room (:obj:Room): The current room that the player is in.
        direction (str): Either north, east, south, west.

    """
    if current_room.get_adjacent_room(direction) is not None:
        scroll_print("Moving " + direction + " to the " +
                     current_room.get_adjacent_room(direction))

        # Check if the door is locked.
        current_door_map = current_room.get_door_map()

        if current_door_map[direction] is False:
            scroll_print("\nThe door is unlocked!\n")

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
                scroll_print("As you walk through the door your vision "
                             "suddenly goes black. A voice enters your mind. "
                             "It speaks in a low raspy growl: \"Ahh it "
                             "appears I have an intruder. Although you cannot "
                             "see me, I assure you I can see you. I am Zlor "
                             "and this is my fortress. Your brother will not "
                             "be returned. You cannot save him, I will make "
                             "sure of that...\" The voice fades and your "
                             "vision returns. Just as it does, there is a "
                             "flash of light and the sound of the stone floor "
                             "shifting. Dark black vines suddenly shoot up "
                             "out of the cracks in the floor. The vines "
                             "quickly grow to block the stairwell entrance to "
                             "the north...Things quiet down and you take a "
                             "look around\n")
                new_room.set_puzzle_status("voice", False)

            elif (new_room.get_name() == "sauna room" and
                  new_room.get_puzzle_status("sauna voice")):
                scroll_print("As you walk through the door your vision goes "
                             "black. A voice enters your mind. It is the same "
                             "voice as the one you encountered in the store "
                             "room. It says, \"So you've made it this far...I "
                             "am tired of these games. You will go no "
                             "farther. I have prepared a special potion that "
                             "has been added to the sauna you are now in. Do "
                             "whatever you like, but while the steam remains "
                             "you will not find the way forward.\". The voice "
                             "fades and your vision returns.\n")
                new_room.set_puzzle_status("sauna voice", False)

            # scroll_print out room description.
            if player.has_memory(new_room_name):
                scroll_print(new_room.get_short_description())

            else:
                player.add_memory(new_room_name)

                scroll_print(new_room.get_description())

            print_item_descriptions(new_room)

            # Save state so that room tracks player in game files.
            save_object_state(new_room)

        else:
            if (current_room.get_name() == "store room" and
               current_room.get_puzzle_status("vines")):
                scroll_print("\nYou can't enter the stairwell. The black "
                             "vines are blocking the way. You'll need to "
                             "find a way to remove them.")

            elif (current_room.get_name() == "room of last rites" and
                  current_room.get_puzzle_status("cage")):
                scroll_print("\nYou try and open the door but it is locked. "
                             "The fairy calls to you from the cage. \"Hey "
                             "if you let me out of here I might be able to "
                             "help you get the key to that door.\"")

            else:
                scroll_print("The door is locked!")

    else:
        scroll_print("There is no room in that direction!")


def combat(player, monster):
    """Function to allow for player monster rpg combat.

    Args:
        player (:obj:Player): The user selected main character.
        monster (:obj:Monster): A character that the player fights.

    """
    # Begin combat dialogue
    time.sleep(1)
    scroll_print("\nOh no! {}".format(monster.get_description()))
    time.sleep(1)
    scroll_print("\nYou have encountered %s! Let's begin combat..." %
                 (monster.get_name()))
    time.sleep(1)

    combat_continues = True

    while combat_continues:
        # Allow the player to choose their move
        # Output player combat options
        scroll_print("\nPlease select which move you want: ")
        player.get_attack_description(0)
        player.get_attack_description(1)
        player.get_attack_description(2)

        # Get the player's choice
        attack_choice = input().lower().strip()

        invalid_choice = True

        while(invalid_choice):
            if attack_choice != 'slash' and attack_choice != 'thunder' and \
               attack_choice != 'singe':
                scroll_print("\nYou entered an invalid choice! ")
                scroll_print("Please enter: Slash, Thunder, or Singe: ")

                attack_choice = input().lower().strip()
            else:
                invalid_choice = False

        # Execute the player's attack
        total_damage = player.execute_attack(attack_choice)

        # Idenfity the player's attack type
        attack_type = player.get_attack_type(attack_choice)

        # Get monster's defensive result, which is a random
        # number in the range of 0 and the monster's defense
        # or magic defense depending on the type of the attack
        if attack_type == 0:
            total_defense = randint(0, monster.get_defense())
        elif attack_type == 1:
            total_defense = randint(0, monster.get_magic_defense())
        else:
            total_defense = randint(0, (monster.get_defense() +
                                        monster.get_magic_defense()))

        total_damage -= total_defense

        if total_damage < 1:
            scroll_print("\nYou missed! ")
        else:
            # Deal the damage to the enemy
            scroll_print("\nYou did %d damage! " % (total_damage))
            current_monster_health = monster.get_health()
            monster.set_health(current_monster_health-total_damage)

        # Check if the enemy is dead, if so, exit combat and gain experience
        if monster.get_health() <= 0:
            time.sleep(1)
            scroll_print("\nYou have slain %s" % (monster.get_name()))

            experience_gained = monster.get_loot()
            scroll_print("You have gained %d experience points!" %
                         (experience_gained))

            new_experience_total = experience_gained + player.get_experience()

            # Level up the player if they have enough experience
            if new_experience_total >= 10:  # we will need to do balancing!!!
                time.sleep(1)
                scroll_print("\n%s has leveled up! " % player.get_name())
                player.level_up()

                # Carry over the excess experience into the new level
                new_experience_total = new_experience_total - 10

            player.set_experience(new_experience_total)

            combat_continues = False

        else:
            # Randomly choose what ability the enemy will use
            time.sleep(1)
            attack_type = randint(0, 1)
            total_damage = monster.npc_attack(attack_type)

            # Get player's defensive result, which is a random
            # number in the range of 0 and the player's defense
            # or magic defense depending on the type of the attack
            if attack_type == 0:
                total_defense = randint(0, player.get_defense())
            else:
                total_defense = randint(0, player.get_magic_defense())

            total_damage -= total_defense

            time.sleep(1)

            # Calculate the damage
            if total_damage < 1:
                scroll_print("%s missed! " % (monster.get_name()))
                time.sleep(1)
            else:
                # Deal the damage to the enemy
                scroll_print("\n%s did %d damage! " % (monster.get_name(),
                             total_damage))
                time.sleep(1)
                current_player_health = player.get_health()
                player.set_health(current_player_health-total_damage)

            # Check if the player is dead
            if player.get_health() <= 0:
                player.lose_life()
                scroll_print("\nYou blacked out! ")

                # Check if the player has any lives left
                if player.get_lives() <= 0:
                    return False

                else:
                    time.sleep(1)
                    scroll_print("\nA small pink fairy flies around your "
                                 "body... ")
                    scroll_print("You woke up! Your health has restored to "
                                 "50 HP. ")
                    # Reset the player's health and magic
                    # based on their level
                    player.revive(player.get_level())

    return True


def start_game(player_name, character_choice):
    """Create game files, load initial room, and load player.

    Args:
        player_name (str): The user selected main character name.

    Returns:
        :obj:Room: The current room that the player is in.

    """
    init_game_files(player_name, character_choice)

    current_room = load_object("fortress_entrance")

    return current_room


def is_game_over(player):
    """Checks to see if the player still has lives.

    Args:
        player (:obj:Player): The main character of the game.

    Returns:
        bool: False if the character is dead or the game is complete.

    """
    if player.get_lives() <= 0:
        return True

    if player.rescue_evelyn is True:
        scroll_print("\n The End \n")
        return True

    else:
        return False
