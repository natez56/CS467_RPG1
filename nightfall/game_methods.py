from game_classes import *
from file_manager import *
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


def room_1_feature_handler(current_room, verb, feature):
    """Handles verb commands related to room 1 features.

    Args:
        current_room (:obj:Room): The current room the player is in.
        verb (str): The action the user would like to take.
        feature (str): The feature in this room the user would like to act on.

    """

    # Dictionary of feature name mapped to a description of that feature.
    feature_dict = current_room.get_features()

    # Handle feature interaction for each of the 10 main verbs.
    if verb == "take":
        if feature == "body":
            print("This body is too heavy to carry.")

        if feature == "cloak":
            print("The cloak is in tatters, better to leave it I think.")

        if feature == "bag":
            print("This bag has holes in it. Better to leave it I think.")

        if feature == "door":
            print("Hmm let's see, if I unbolt the doors and go get about "
                  "10 other villagers to help me carry them...on second "
                  "thought maybe I should leave the doors where they are.")

    elif verb == "use":
        print("I can't use that. Better move on or find something I can "
              "use.")

    elif verb == "drop":
        print("Drop what? I'm not carrying that.")

    elif verb == "look at":
        print("You take a close look at the {}".format(feature))

        print(feature_dict[feature])

    elif verb == "eat":
        if feature == "body":
            print("Eat this? I don't think so. I'm not a zombie.")

        if feature == "door":
            print("You naw on the oak doors a bit. Yup that's oak all "
                  "right...")

        if feature == "cloak":
            print("You chew on the old cloak a bit and think to yourself "
                  "I better start coming up with some reasonable things "
                  "to do or I'll never rescue Evelyn.")

        if feature == "bag":
            print("You chew on the old bag a bit and think to yourself "
                  "I better start coming up with some reasonable things "
                  "to do or I'll never rescue Evelyn.")

    elif verb == "drink":
        print("I can't drink that.")

    elif verb == "smell":
        if feature == "door":
            print("Smells like oak.")

        else:
            print("The smell is foul. This has been here a while.")

    elif verb == "listen to":
        print("You hear the sounds of the wind rustling the leaves of the "
              "nearby trees.")

    elif verb == "climb":
        print("There's nothing to climb.")

    elif verb == "duck":
        print("You duck quickly and then stand back up.")

    save_object_state(current_room)


def general_item_handler(current_room, verb, item_name):
    """Handle any non-unique verb and item interactions.

    Args:
        current_room (:obj:Room): The current room that the player is in.
        verb (str): The action a user would like to take.
        item_name (str): The name of the item the user would like to use.

    """
    player = current_room.get_player()

    # For each verb handler player and item or room and item interaction.
    if verb == "take":
        if item_name not in player.get_item_names():
            item = current_room.get_item(item_name)

            player.add_item(item)

            # When item is added to player it must be removed from the room.
            current_room.remove_item(item)
        else:
            print("That item is already in your inventory.")

    # Player can look at an item whether it is in inventory on in the room.
    elif verb == "look at":
        if item_name in current_room.get_item_names():
            print(current_room.get_item(item_name).get_description())
        else:
            print(player.get_item(item_name).get_description())

    elif verb == "drop":
        if item_name in player.get_item_names():
            item = player.drop_item(item_name)

            # When an item is dropped by the player it must be added to the
            # current room.
            current_room.add_item(item)
        else:
            print("You're not carrying that item currently.")

    save_object_state(current_room)


def room_1_item_handler(current_room, verb, item_name):
    """Handle room 1 player and item and room and item interactions.

    Args:
        current_room (:obj:Room): The current room the player is in.
        verb (str): The action the user would like to take.
        item_name: The name of the item the user would like to use.

    """
    player = current_room.get_player()

    # These verbs do not need unique room interactions.
    if verb == "take" or verb == "look at" or verb == "drop":
        general_item_handler(current_room, verb, item_name)

    # The verb use has custom interactions for each room.
    elif verb == "use":
        if item_name == "sword" and "sword" in player.get_item_names():
            print("You start swinging your sword around like a lunatic. If "
                  "anyone was around to see you I'm sure they'd be terrified.")

        elif item_name not in player.get_item_names():
            print("You're not carrying that item currently.")

    save_object_state(current_room)


def room_2_feature_handler(current_room, verb, feature):
    """Handle room 2 player and feature interaction.

    Args:
        current_room (:obj:Room): The current room the player is in.
        verb (str): The action the user would like to take.
        feature (str): The feature in this room the user would like to act on.

    """
    # A dictionary that maps feature name to a description of that feature.
    feature_dict = current_room.get_features()

    # Handle custom feature interaction for each of the 10 core verbs.
    if verb == "take":
        if feature == "rubble":
            print("The pieces of rubble are to heavy to carry.")

        if feature == "door":
            print("Hmm let's see, if I unbolt the doors and go get about "
                  "10 other villagers to help me carry them...on second "
                  "thought maybe I should leave the doors where they are.")

        else:
            print("I can't take that.")

    if verb == "use":
        print("I can't use that. Better move on or find something I can "
              "use.")

    if verb == "drop":
        print("Drop what? I'm not carrying that.")

    if verb == "look at":
        # Trigger to add rope to feature list. The command use sword will
        # eliminate the rope trap after the feature is discovered.
        if feature == "rubble":
            print("You take a close look at the {}".format(feature))

            print(feature_dict[feature])

            # Add the rope feature so that it can be acted upon by the user.
            if current_room.get_puzzle_status("rope"):
                rope_feature = ("The rope is taut, and looks as though it is "
                                "meant to trip someone walking toward the "
                                "inner door.")

                current_room.add_feature("rope", rope_feature)

                # The rope puzzle has been triggered and should now be set to
                # false. This tracks puzzle status.
                current_room.set_puzzle_status("rope", False)

        if feature == "rope":
            print("You take a close look at the {}".format(feature))

            print(feature_dict[feature])

        # If the user has not entered: use sword after the rope feature has
        # been added to the room, then going to inspect the writing triggers
        # a trap that will damage them.
        if feature == "writing":
            if (current_room.get_puzzle_status("rope") or
               "rope" in current_room.get_features()):

                print("You walk toward the door to inspect the writing.")

                rope_trap(current_room)

            # If the trap has already been triggered then the player can
            # inspect the writing as normal.
            else:
                print("You take a close look at the {}".format(feature))

                print(feature_dict[feature])

    if verb == "eat":
        if feature == "rubble":
            print("You take a bite of some rubble and break a tooth. Ouch!")

        if feature == "door":
            print("You naw on the oak doors a bit. Yup that's oak all "
                  "right...")

        if feature == "writing":
            print("You can't eat writing, that's silly.")

    if verb == "drink":
        print("I can't drink that.")

    if verb == "smell":
        if feature == "door":
            print("Smells like oak.")

        if feature == "writing":
            print("The writing smells foul.")

        if feature == "rubble":
            print("Ahh nothing like the smell of some good rubble.")

    if verb == "listen to":
        print("All quite...too quite.")

    if verb == "climb":
        if feature == "rubble":
            print("You climb on top of a pile of rubble. Congrats you're king "
                  "of rubble mountain.")

    if verb == "duck":
        print("You duck quickly and then stand back up.")

    save_object_state(current_room)


def room_2_item_handler(current_room, verb, item_name):
    """Handles room 2 player item or room item interactions.

    Args:
    current_room (:obj:Room): The current room that the player is in.
    verb (str): The action a user would like to take.
    item_name (str): The name of the item the user would like to use.

    """
    player = current_room.get_player()

    # Triggers rope trap if trap hasn't already been triggered.
    if (verb == "look at" and item_name == "key" and
            (current_room.get_puzzle_status("rope") or
             "rope" in current_room.get_features())):

            print("The golden key glitters on the floor among the rubble. "
                  "You walk forward to take a closer look.")

            rope_trap(current_room)

    # Triggers rope trap if trap hasn't already been triggered.
    elif (verb == "take" and item_name == "key" and
            (current_room.get_puzzle_status("rope") or
             "rope" in current_room.get_features())):

            print("The golden key glitters on the floor among the rubble. "
                  "You walk forward to pick up the key.")

            rope_trap(current_room)

    # These verbs do not get unique handlers for this room.
    elif verb == "take" or verb == "look at" or verb == "drop":
        general_item_handler(current_room, verb, item_name)

    # Verb use uniquely interacts with this rooms features.
    elif verb == "use":
        # After a user inspects the rubble in the room, the rope feature is
        # added.  Then, if a player uses the sword, it will disable the rope
        # trap and remove it as a feature from the room.
        if item_name == "sword" and "sword" in player.get_item_names():
            if "rope" in current_room.get_features():
                print("You kneel down and cut the rope. As soon as the rope "
                      "is cut you here a click and a crossbow bolt zooms over "
                      "your head. Good thing I saw this trap ahead of time.")

                current_room.remove_feature("rope")

        elif item_name not in player.get_item_names():
            print("You are not carrying that item currently.")

    save_object_state(current_room)


def rope_trap(current_room):
    """Handles rope trap event for room 2.

    Args:
        current_room (:obj:Room): The room the player is currently in.

    """
    print("As you walk toward the door, between the scattered rubble, "
          "your foot trips on a small hard to see rope. You here a "
          "click...\n")

    # Get user response for this mini event.
    print("What would you like to do?")

    response = input("Type some text: ")
    response.lower().strip()
    print("")

    # The only valid response to avoid damage is to duck.
    if "duck" in response:
        print("You duck just as a crossbow bolt passes over head. "
              "A narrow miss. I should probably inspect rooms more "
              "closely in the future.")
    else:
        print("Before you can do anything a crossbow bolt flies "
              "across the room from a hidden opening and strikes "
              "you in the shoulder. Ouch should have ducked.")

    # Set the puzzle status to false to indicate that the rope trap event is
    # complete.
    current_room.set_puzzle_status("rope", False)

    # The feature is removed from the room so that the event does not repeat.
    current_room.remove_feature("rope")

    save_object_state(current_room)


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
        if (current_room.get_name() == "entrance_hall" and
            (action["direction"] == 'east' or
             action["direction"] == "mess hall") and
           (current_room.get_puzzle_status("rope") or
           "rope" in current_room.get_features())):

            rope_trap()

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

        if current_room.get_name() == "dungeon entrance":
            room_1_feature_handler(current_room, action["verb"],
                                   action["feature"])

        elif current_room.get_name() == "entrance hall":
            room_2_feature_handler(current_room, action["verb"],
                                   action["feature"])

    # Handle player / item interaction for a given room.
    elif (action["verb"] is not None and action["item"] is not None
          and (action["item"] in player.get_item_names() or
          action["item"] in current_room.get_item_names())):

        if current_room.get_name() == "dungeon entrance":
            room_1_item_handler(current_room, action["verb"],
                                action["item"])

        elif current_room.get_name() == "entrance hall":
            room_2_item_handler(current_room, action["verb"],
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
        load_game()

        # Get information to print description of current room the player is
        # in.
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
    """Create game files, load initial room, and load player.

    Args:
        player_name (str): The user selected main character name.

    Returns:
        :obj:Room: The current room that the player is in.

    """
    init_game_files(player_name)

    current_room = load_object("dungeon_entrance")

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
