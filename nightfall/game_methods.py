from game_classes import *
from file_manager import *
from random import *


def starting_menu():
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
        load_game()

    elif menu_choice == "quit":
        print("\nThank you for playing Nightfall. "
              "Have a fortuitous evening... \n")
        exit()

    else:
        print("Returning to the game!")


def help_menu():
    print("\nHere is a list of available commands: ")
    print("    ")  # ADD A LIST OF VERBS THAT CAN BE USED FOR COMMANDS IN GAME


def room_1_feature_handler(current_room, verb, feature):
    feature_dict = current_room.get_features()

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
    if verb == "use":
        print("I can't use that. Better move on or find something I can "
              "use.")
    if verb == "drop":
        print("Drop what? I'm not carrying that.")
    if verb == "look at":
        print("You take a close look at the {}".format(feature))
        print(feature_dict[feature])
    if verb == "eat":
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
    if verb == "drink":
        print("I can't drink that.")
    if verb == "smell":
        if feature == "door":
            print("Smells like oak.")
        else:
            print("The smell is foul. This has been here a while.")
    if verb == "listen to":
        print("You hear the sounds of the wind rustling the leaves of the "
              "nearby trees.")
    if verb == "climb":
        print("There's nothing to climb.")
    if verb == "duck":
        print("You duck quickly and then stand back up.")

    save_object_state(current_room)


def room_1_item_handler(current_room, verb, item):
    player = current_room.get_player()

    if verb == "take":
        if item == "sword":
            player.add_item(current_room.get_item("sword"))
    if verb == "use":
        if item == "sword":
            print("You start swinging your sword around like a lunatic. If "
                  "anyone was around to see you I'm sure they'd be terrified.")

    save_object_state(current_room)


def room_2_feature_handler(current_room, verb, feature):
    feature_dict = current_room.get_features()

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
        if feature == "rubble":
            print("You take a close look at the {}".format(feature))
            print(feature_dict[feature])
            if current_room.get_puzzle_status("rope"):
                rope_feature = ("The rope is taut, and looks as though it is "
                                "meant to trip someone walking toward the "
                                "inner door.")
                current_room.add_feature("rope", rope_feature)
                current_room.set_puzzle_status("rope", False)
        if feature == "rope":
            print("You take a close look at the {}".format(feature))
            print(feature_dict[feature])
        if feature == "writing":
            if (current_room.get_puzzle_status("rope") or
               "rope" in current_room.get_features()):
                print("You walk toward the door to inspect the writing.")
                rope_trap(current_room)
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


def room_2_item_handler(current_room, verb, item):
    player = current_room.get_player()

    if verb == "take":
        if item == "sword":
            player.add_item(current_room.get_item("sword"))
    if verb == "use":
        if item == "sword":
            if "rope" in current_room.get_features():
                print("You kneel down and cut the rope. As soon as the rope "
                      "is cut you here a click and a crossbow bolt zooms over "
                      "your head. Good thing I saw this trap ahead of time.")
                current_room.remove_feature("rope")

    save_object_state(current_room)


def rope_trap(current_room):
    print("As you walk toward the door, between the scattered rubble, "
          "your foot trips on a small hard to see rope. You here a "
          "click...")

    response = input("Type some text: ")
    response.lower().strip()

    if response == "duck":
        print("You duck just as a crossbow bolt passes over head. "
              "A narrow miss. I should probably inspect rooms more "
              "closely in the future.")
    else:
        print("Before you can do anything a crossbow bolt flies "
              "across the room from a hidden opening and strikes "
              "you in the shoulder. Ouch should have ducked.")

    current_room.set_puzzle_status("rope", False)
    current_room.remove_feature("rope")

    save_object_state(current_room)


def take_action(current_room, action):
    """From action list call the right function."""
    player = current_room.get_player()

    # Handle any error output
    if action["error"] is not None:
        print(action["error"])

    # Handle the standard actions
    elif action["standard_action"] is not None:
        return handle_standard_action(current_room, player, action)

    # Handle the directions
    elif action["direction"] is not None:
        # Handle room names
        if (current_room.get_name() == "entrance_hall" and
            (action["direction"] == 'east' or
             action["direction"] == "mess hall") and
           (current_room.get_puzzle_status("rope") or
           "rope" in current_room.get_features())):
            rope_trap()

        elif action["direction"] != "north" and \
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
                    travel(current_room, direction)
                else:
                    print("That room is not connected to the "
                          "current room!")

        else:
            travel(current_room, action["direction"])

    elif (action["verb"] is not None and
          action["feature"] is not None and
          action["feature"] in current_room.get_features()):
        if current_room.get_name() == "dungeon entrance":
            room_1_feature_handler(current_room, action["verb"],
                                   action["feature"])
        elif current_room.get_name() == "entrance hall":
            room_2_feature_handler(current_room, action["verb"],
                                   action["feature"])

    elif (action["verb"] is not None and
          action["item"] is not None and
          action["item"] in player.get_item_names()):
        if current_room.get_name() == "dungeon entrance":
            room_1_item_handler(current_room, action["verb"],
                                action["item"])
        elif current_room.get_name() == "entrance hall":
            room_2_item_handler(current_room, action["verb"],
                                action["item"])

    save_object_state(current_room)


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

            for item in player.get_inventory():
                print(item.get_name())

            # equipped_item = player.get_equipped_item()
            # # if equipped_item is not None:
            # #     print("Equipped item: {}".format(equipped_item.get_name()))
            # # else:
            # #     print("Equipped item: None")
    elif action["standard_action"] == "savegame":
        save_game(current_room)
    elif action["standard_action"] == "loadgame":
        load_game()


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

            save_object_state(current_room)

            new_room_name = current_room.get_adjacent_room(direction)

            new_room = load_object(new_room_name)

            new_room.set_player(player)

            save_object_state(new_room)

            # Print out room description.
            if player.has_memory(new_room_name):
                print(new_room.get_short_description())
            else:
                player.add_memory(new_room_name)

                print(new_room.get_description())

        else:
            print("The door is locked!")
            print("You can use a key to unlock the door.")

    else:
        print("\nThere is no room in that direction!")


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


def is_game_over(player):
    """Checks to see if the player still has lives."""
    if player.get_lives() > 0:
        return False
    if player.rescue_evelyn is False:
        return False
    else:
        return True
