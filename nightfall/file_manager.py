from game_classes import *
from pathlib import Path
import pickle
import os
import shutil


def init_room_1():
    """Instantiates dungeon_entrance room.

    Returns:
        :obj:Room: Room object.

    """
    name = "dungeon_entrance"
    description = ("At the end of the path in a clearing there is a large "
                   "stone fortress. Nothing grows near the fortress walls. "
                   "There is a large double door of dark oak. Just outside "
                   "the entrance is a huddled mass on the ground. Could it be "
                   "Evelyn?",
                   "I'm at the fortress entrance, the large oak double doors "
                   "are slightly ajar."
                   )

    # Init items
    # Item 1 - rusty_sword
    sword_name = "Rusty Sword"
    sword_description = ("A rusty sword. It's long since lost its edge. "
                         "Who knows, you might be able to bludgeon monsters "
                         "with it.")
    sword_durability = None
    sword_stats = {"attack_power": 1}

    rusty_sword = Item(sword_name, sword_description, sword_durability,
                       sword_stats)

    # Set item list
    item_list = []
    item_list.append(rusty_sword)

    # Set monster list
    monster_list = []

    # Set player to None
    player = None

    # Set room navigation traits.
    adjacent_rooms = {'north': 'entrance hall', 'east': None, 'south': None,
                      'west': None}
    door_map = {'north': False}

    # Set features in room.
    door_feature = ("The doors are thick and sturdy. One door appears to be "
                    "slightly ajar."
                    )

    body_feature = ("The dark mass comes into view. You see that it is formed "
                    "of a heavy traveling cloak and bag. Bones peak out from "
                    "underneath. You recognize the clothes as the kind worn "
                    "by traveling traders in the mountains. This body has "
                    "been here a while. Nearby on the ground is a rusty sword."
                    )

    cloak_feature = "The cloak is old an torn. It will not be of use."

    bag_feature = ("The bag is empty and torn. Nothing of the traders goods "
                   "remain."
                   )

    feature_dict = {"door": door_feature, "body": body_feature,
                    "cloak": cloak_feature, "bag": bag_feature}

    # Instantiate room object.
    dungeon_entrance = Room(name, description, item_list, monster_list, player,
                            adjacent_rooms, door_map, feature_dict)

    return dungeon_entrance


def init_room_2():
    """Instantiates entrance_hall room.

    Returns:
        :obj:Room: Room object.

    """
    name = "entrance_hall"
    description = ("Inside the fortress it is dark. A hole in the far left "
                   "corner of the fortress wall casts some moonlight on the "
                   "far side of the room. On the far wall where the moonlight "
                   "shines there appears to be some writing. Near the writing "
                   "is a door leading farther in the fortress.",
                   "I'm in the entrance hall, there's goblin writing on the "
                   "wall and a door leading father into the fortress."
                   )

    # Init items
    # Item 1 - chest_key
    chest_key_name = "Chest Key"
    chest_key_description = ("An elaborate golden key.")
    chest_key_durability = None
    chest_key_stats = None

    chest_key = Item(chest_key_name, chest_key_description,
                     chest_key_durability, chest_key_stats)

    # Set item list
    item_list = []
    item_list.append(chest_key)

    # Set monster list
    # ADD A GOBLIN TO THIS ROOM %^&*(^%&*(^%$*()^%$^&*(^&%^(^%^(^%)))))
    monster_list = []

    # Set player to None
    player = None

    # Tracks which rooms connect to this room. Pairs direction with room name.
    # Example: {'north': 'entrance_hall'}
    adjacent_rooms = {'north': None, 'east': 'mess hall',
                      'south': 'dungeon entrance', 'west': None}

    # Tracks which doors are locked.  False means unlocked.
    door_map = {'east': False, 'south': False}

    goblin_graffiti_feature = ("You've seen this type of writing before at "
                               "the entrance to the high mountains near the "
                               "edge of your homeland. This is goblin "
                               "graffiti, used to mark a particular goblin "
                               "clans home."
                               )

    east_door_feature = ("An oak door with a large iron handle.")

    feature_dict = {"graffiti": goblin_graffiti_feature,
                    "door": east_door_feature}

    entrance_hall = Room(name, description, item_list, monster_list, player,
                         adjacent_rooms, door_map, feature_dict)

    return entrance_hall


def init_room_3():
    """Instantiates mess_hall room.

    Returns:
        :obj:Room: Room object.

    """
    name = "mess_hall"
    description = ("A long dark room appears before you. It looks as though "
                   "this is where the people of the mansion eat. There are "
                   "two long tables that stretch the full length of the room "
                   "and there are suits of armor lining both walls. The "
                   "tables still have dirty plates scattered about ."
                   )

    # Init items
    # Item 1 - bread
    bread_name = "Bread"
    bread_description = ("A fresh chunk of French bread.")
    bread_durability = None
    bread_stats = None

    bread = Item(bread_name, bread_description, bread_durability,
                 bread_stats)

    # Set item list
    item_list = []
    item_list.append(bread)

    # Set monster list
    # ADD A SKELETON TO THIS ROOM %&^*()&^&%^()&(^*%&$&^&()&(^*%&^()^))
    monster_list = []

    # Set player to None
    player = None

    # Set room navigation traits.
    adjacent_rooms = {'north': 'kitchen', 'east': 'store room', 'south': None,
                      'west': 'entrance hall'}
    door_map = {'north': True, 'east': False, 'west': False}

    # Set features in room.
    chicken_feature = ("As you walk through the hall you see a torn piece of "
                       "chicken. It looks like it might still be fresh "
                       "enough to eat. ")

    armor_feature = ("Suddenly you hear armor rattle... A large suit "
                     "of armor crashes to the ground near you. ")

    feature_dict = {"chicken": chicken_feature, "armor": armor_feature}

    # Instantiate room object.
    mess_hall = Room(name, description, item_list, monster_list, player,
                     adjacent_rooms, door_map, feature_dict)

    return mess_hall


def init_room_4():
    """Instantiates store_room room.

    Returns:
        :obj:Room: Room object.

    """
    name = "store_room"
    description = ("The room has large shelves that go from the floor "
                   "all the way to the very high ceilings. There is a "
                   "stone area for refrigeration and hanging animal "
                   "carcasses from the ceiling. "
                   )

    # Init items
    # Item 1 - empty_jar
    empty_jar_name = "Empty Jar"
    sword_description = ("A clear, empty jar. It has some green slimy "
                         "residue in it. ")
    empty_jar_durability = None
    empty_jar_stats = None

    empty_jar = Item(empty_jar_name, empty_jar_description,
                     empty_jar_durability, empty_jar_stats)

    # Item 2 - letter
    letter_name = "Letter"
    letter_description = ("The letter has a scrawled ink lettering "
                          "that is hard to make out. It looks like "
                          "it might be written in distress... ")
    letter_durability = None
    letter_stats = None

    letter = Item(letter_name, letter_description, letter_durability,
                  letter_stats)

    # Set item list
    item_list = []
    item_list.append(empty_jar, letter)

    # Set monster list
    monster_list = []

    # Set player to None
    player = None

    # Set room navigation traits.
    adjacent_rooms = {'north': 'washroom', 'east': None, 'south': None,
                      'west': 'mess hall'}
    door_map = {'north': True, 'west': False}

    # Set features in room.
    broom_feature = ("A broom in the corner of the room looks like it "
                     "is moving. Suddenly, the boom shoots up and flies "
                     "around the room before retuning to the corner. "
                     )

    rice_feature = ("A bag of rice fell over on the top shelf and dumps "
                    "rice down onto the floor. "
                    )

    feature_dict = {"broom": broom_feature, "rice": rice_feature}

    # Instantiate room object.
    store_room = Room(name, description, item_list, monster_list, player,
                      adjacent_rooms, door_map, feature_dict)

    return store_room


def init_room_5():
    """Instantiates kitchen room.

    Returns:
        :obj:Room: Room object.

    """
    name = "kitchen"
    description = ("The room before you is clearly the kitchen of the "
                   "mansion. There are fish still on cutting boards. "
                   "The smell is rancid. It appears as though no one has "
                   "cleaned the kitchen for a very long time."
                   )

    # Init items
    # Item 1 - magic_resistant_oven_mitt
    oven_mitt_name = "Magic Resistant Oven Mitt"
    oven_mitt_description = ("The oven mitt glows with an orange hue. "
                             "The outside is warm to the touch. ")
    oven_mitt_durability = None
    oven_mitt_stats = {"magic_defense": 3}

    oven_mitt = Item(oven_mitt_name, oven_mitt_description,
                     oven_mitt_durability, oven_mitt_stats)

    # Set item list
    item_list = []
    item_list.append(oven_mitt)

    # Set monster list
    # ADD A CORROSIVE SLUDGE TO THIS ROOM &^T*Y(&^&%*()&^&*()^%&()^%&(^&))
    monster_list = []

    # Set player to None
    player = None

    # Set room navigation traits.
    adjacent_rooms = {'north': None, 'east': None, 'south': 'mess hall',
                      'west': None}
    door_map = {'south': False}

    # Set features in room.
    rat_feature = ("A dark mass can be seen in the corner of the room. "
                   "As you walk towards it, it scatters across the floor "
                   "into a nearby drain. ")

    sink_feature = ("The massive double basin sink is filled to the brim "
                    "with dishes covered in sludge. ")

    feature_dict = {"rat": rat_feature, "sink": sink_feature}

    # Instantiate room object.
    kitchen = Room(name, description, item_list, monster_list, player,
                   adjacent_rooms, door_map, feature_dict)

    return kitchen


def init_room_objects():
    """Creates the starting game objects.

    Returns:
        list(:obj:Room): List of all room objects in game.

    """
    room_list = []

    dungeon_entrance = init_room_1()
    entrance_hall = init_room_2()

    room_list.extend((dungeon_entrance, entrance_hall))

    return room_list


def init_player_object(player_name):
    """Instantiates the inital Player object.

    Returns:
        :obj:Player: Player object with attributes set.

    """
    name = player_name
    health = 100
    magic = 100
    level = 1
    magic_defense = 0
    magic_power = 1
    defense = 0
    attack_power = 1
    num_lives = 3
    experience = 0
    memory = []
    backpack = []
    equipped_item = None

    player = Player(name, health, magic, level, magic_defense, magic_power,
                    defense, attack_power, num_lives, experience, memory,
                    backpack, equipped_item)

    return player


def init_game_files(player_name):
    """Serializes starting game state into game files.

    Args:
        player_name (string): Name decided by user for the character they
            control.

    """
    # Clear current_game directory contents.
    current_game_path = str(Path("game_files/current_game"))

    shutil.rmtree(current_game_path)
    os.makedirs(current_game_path)

    room_list = []

    room_list = init_room_objects()
    player = init_player_object(player_name)

    room_list[0].set_player(player)

    # Create game file for each room.
    for room in room_list:
        save_object_state(room)


def load_object(object_name):
    """Load object from binary file.

    Args:
        object_name (string): Name of the object to be loaded from file. Object
            name should match the file name trying to be loaded.

    Returns:
        :obj:: Returns the object type that the file stores.

    """
    file_path = Path("game_files/current_game/")

    file_name = object_name + '.bin'

    file = file_path / file_name

    binary_file = open(str(file), mode='rb')

    game_object = pickle.load(binary_file)

    return game_object


def save_object_state(game_object):
    """Serialize object into binary file.

    Args:
        game_object (:obj:): Takes a class object for serialization. Object
            must have a get_name() method for this function to work.

    """
    file_path = Path("game_files/current_game/")

    file_name = game_object.get_name() + '.bin'

    file = file_path / file_name

    binary_file = open(str(file), mode='wb')

    pickle.dump(game_object, binary_file)

    binary_file.close()


def save_game(current_room):
    """Save entire game state to new file or overwrite current file.

    Args:
        current_room (:obj:Room): The current room that the player is located
            in.

    """
    print("\nSave Menu")

    user_input = input("New Save Game? (Y/N) ")
    user_input = user_input.lower()

    while user_input == 'n' and get_num_saved_games() < 1:
        user_input = input("I'm sorry you do not have any saved games to "
                           "overwrite. Please enter Y to create a new saved "
                           "game.\n")
        user_input = user_input.lower()

    while user_input != 'y' and user_input != 'n':
        user_input = input("Please enter the char Y or N: ")
        user_input = user_input.lower()

    if user_input == 'y':
        file_name = ""

        # Get title from user of new saved file.
        input_is_valid = False
        while not input_is_valid:
            file_name = input("\nPlease enter a title for your new saved game "
                              "(no special characters allowed)\n")

            i = 0
            chars_valid = True

            # Ensure that file name has only numbers and characters.
            while chars_valid and i < len(file_name):
                if not file_name[i].isalpha() and not file_name[i].isdigit():
                    print("Invalid character: {}".format(file_name[i]))

                    chars_valid = False

                i += 1

            if chars_valid:
                input_is_valid = True

        # Set path to include the new file name designated by user.
        file_path = str(Path("game_files/saved_games/{}".format(file_name)))

        # Check for duplicate file name. If it exists then append (num) to the
        # file path. Avoids duplicates by increasing num when a duplicate is
        # encountered.
        num = 1
        while os.path.exists(file_path):
            alt_name = file_name + "({})".format(num)
            file_path = str(Path("game_files/saved_games/{}".format(alt_name)))
            num += 1

        # Make the new directory to hold the game files.
        os.makedirs(file_path)

        # Save the current game state to the current_game folder and then
        # copy that folders contents into the newly created folder.
        save_game_state(current_room, file_path)

        print("\nGame Saved.")

    # Overwrite saved game process.
    else:
        print("\nSaved files")

        file_path = Path("game_files/saved_games")
        game_files = os.listdir(str(file_path))

        print("Please type the number of the file you would like to "
              "overwrite or type E to exit.")

        # Print out a list of saved files. Names are the names of the
        # directories where the saved files are stored.
        num = 1
        file_list = []
        for file in game_files:
            print("({}) {}".format(num, file))

            num += 1

            file_list.append(file)

        # Get user selection of the file they would like to load.
        user_input = input("")
        user_input = user_input.lower()

        # Check that input is a number within the correct range or 'e'.
        valid_input = False
        while not valid_input:
            if user_input.isalpha() and user_input != 'e':
                valid_input = False
            elif (user_input.isdigit() and
                  (int(user_input) < 1 or int(user_input) > num - 1)):
                valid_input = False
            else:
                valid_input = True

            # Get new input if user enters something incorrect.
            if not valid_input:
                user_input = input("\nInvalid input {}. Please enter an "
                                   "integer corresponding to a game file or "
                                   "press E to exit.\n".format(user_input))

                user_input = user_input.lower()

        # 'e' corresponds to exit menu.
        if user_input != 'e':
            # Get user selection of the file they want to overwrite.
            file = file_list[int(user_input) - 1]

            # Create file path using user selection.
            file_path = str(Path("game_files/saved_games/{}".format(file)))

            # Verify overwrite.
            response = input("\nAre you sure you would like to overwrite {}? "
                             "(Y/N): ".format(file))
            response = response.lower()

            # Verify most recent user input.
            while response != 'y' and response != 'n':
                response = input("Invalid input {}. Please enter Y or "
                                 "N: ".format(response))
                response = response.lower()

            if response == 'y':
                # Save current state in current_game directory and then copy
                # that directories contents into the file_path.
                save_game_state(current_room, file_path)

                print("\nGame Saved")

    print("\nSave Menu Exited.\n")


def save_game_state(current_room, destination_path):
    """Save game state to specified file.

    Args:
        current_room (:obj:Room): The current room that the player is in.
        destination_path (str): The file path to the new save location.

    """
    # Overwrite files in current_game folder to house most recent files.
    save_object_state(current_room)

    file_path = str(Path("game_files/current_game"))
    current_game_files = os.listdir(file_path)

    # Copy current_game files into destination path.
    for file in current_game_files:
        file_name = os.path.join(file_path, file)

        if os.path.isfile(file_name):
            shutil.copy(file_name, destination_path)


def load_game(current_room):
    """Enables user to load prior saved game.

    Returns:
        :obj:Room: Returns the loaded Room object.

    """
    print("\nLoad Menu")
    print("Please type the number of the file you would like to load or press "
          "E to exit load menu.")

    file_path = Path("game_files/saved_games")
    game_files = os.listdir(str(file_path))

    # Display list of current saved games.
    num = 1
    file_list = []
    for file in game_files:
        print("({}) {}".format(num, file))

        num += 1

        file_list.append(file)

    # Get user selection of file they would like to load.
    user_input = input("")
    user_input = user_input.lower()

    # Verify user input is 'e' or a number within the range of number of files.
    valid_input = False
    while not valid_input:
        if user_input.isalpha() and user_input != 'e':
            valid_input = False
        elif (user_input.isdigit() and
              (int(user_input) < 1 or int(user_input) > num - 1)):
            valid_input = False
        else:
            valid_input = True

        # Request new input if the user input is invalid.
        if not valid_input:
            user_input = input("\nInvalid input {}. Please enter an integer "
                               "corresponding to a game file or press E "
                               "to exit\n".format(user_input))
            user_input = user_input.lower()

    # Check if user requested to exit the load menu. 'e' means exit.
    if user_input != 'e':
        # Get the file selected by the user to load.
        file_name = file_list[int(user_input) - 1]

        # Append the file name to path.
        file_path = str(Path("game_files/saved_games/{}".format(file_name)))

        # Confirm that user would like to load.
        response = input("\nAre you sure you would like to load this game? "
                         "Your current game will be lost. (Y/N): ")
        response = response.lower()

        # Verify user input.
        while response != 'y' and response != 'n':
            response = input("Invalid input {}. Please enter Y or "
                             "N: ".format(response))
            response = response.lower()

        # Load game.
        if response == 'y':
            current_game_path = str(Path("game_files/current_game"))
            loaded_game_files = os.listdir(file_path)

            # Delete current_game folder and remake.
            shutil.rmtree(current_game_path)
            os.makedirs(current_game_path)

            # Copy file contents of file directory to load into current_game
            # directory.
            for file in loaded_game_files:
                full_path = os.path.join(file_path, file)

                if os.path.isfile(full_path):
                    shutil.copy(full_path, current_game_path)

            print("\nGame {} loaded.\n".format(file_name))

            # Return the room object of the room the player is in.
            return get_current_room()

    return current_room

    print("\nLoad Menu Exited\n")


def initial_load_game():
    """Load file from start menu.

    Returns:
        (:obj:Room): The loaded Room object.

    """
    print("\nLoad Menu")
    print("Please type the number of the file you would like to load.")

    file_path = Path("game_files/saved_games")
    game_files = os.listdir(str(file_path))

    # List possible files to load from stored files. Prepend numbers so that
    # user will enter a number to select the file they would like to load.
    num = 1
    file_list = []
    for file in game_files:
        print("({}) {}".format(num, file))
        num += 1
        file_list.append(file)

    # Get user selection for the file they want to load.
    user_input = input("")
    user_input = user_input.lower()

    # Verify that user has entered a valid integer within the range of 1
    # to the total number of files.
    valid_input = False
    while not valid_input:
        if user_input.isalpha():
            valid_input = False
        elif (user_input.isdigit() and
              (int(user_input) < 1 or int(user_input) > num - 1)):
            valid_input = False
        else:
            valid_input = True

        # Get user input again if they enter invalid input.
        if not valid_input:
            user_input = input("\nInvalid input {}. Please enter an integer "
                               "corresponding to a game "
                               "file.\n".format(user_input))
            user_input = user_input.lower()

    # Get the file name of the user selected file to load.
    file_name = file_list[int(user_input) - 1]

    # Add the user selected file name to the file path to access that
    # directory.
    file_path = str(Path("game_files/saved_games/{}".format(file_name)))

    current_game_path = str(Path("game_files/current_game"))
    loaded_game_files = os.listdir(file_path)

    # Delete and remake current_game folder so that its contents are
    # overwritten by the loaded files.
    shutil.rmtree(current_game_path)
    os.makedirs(current_game_path)

    # Copy files from directory that is to be loaded into current_game.
    for file in loaded_game_files:
        full_path = os.path.join(file_path, file)

        if os.path.isfile(full_path):
            shutil.copy(full_path, current_game_path)

    print("\nGame {} loaded.\n".format(file_name))

    return get_current_room()


def get_current_room():
    """Get Room object will player is located.

    Returns:
        :obj:Room: Room where player is located.

    """
    file_path = str(Path("game_files/current_game/"))

    current_game_files = os.listdir(file_path)

    # Load Room objects from current game files and check if one houses the
    # player.
    for file in current_game_files:
        file_name = os.path.join(file_path, file)

        binary_file = open(file_name, mode='rb')

        game_object = pickle.load(binary_file)

        if game_object.get_player() is not None:
            return game_object


def get_num_saved_games():
    """Get the total number of saved games.

    Returns:
        int: The number of player saved games.

    """
    file_path = str(Path("game_files/saved_games/"))

    saved_game_files = os.listdir(file_path)

    count = 0
    for file in saved_game_files:
        count += 1

    return count
