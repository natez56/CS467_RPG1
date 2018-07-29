from game_classes import *
from pathlib import Path
import pickle
import os
import shutil


def init_room_1():
    """Instantiates fortress_entrance room.

    Returns:
        :obj:Room: Room object.

    """
    name = "fortress entrance"
    description = ("At the end of the path in a clearing there is a large "
                   "stone fortress. Nothing grows near the fortress walls. "
                   "To the north the fortress entrance, a pair of large oak "
                   "double doors. Just outside the entrance is a body on the "
                   "ground. Could it be your brother Evelyn?",
                   "I'm at the fortress entrance. To the north large oak "
                   "double doors lead to the entrance hall."
                   )

    # Init items
    # Item 1 - rusty_sword
    sword_name = "sword"
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

    body_feature = ("The body comes into view. You see that it is formed "
                    "of a heavy traveling cloak and bag. Bones peak out from "
                    "underneath. You recognize the clothes as the kind worn "
                    "by traveling traders in the mountains. This body has "
                    "been here a while."
                    )

    cloak_feature = "The cloak is old an torn. It will not be of use."

    bag_feature = ("The bag is empty and torn. Nothing of the traders goods "
                   "remain."
                   )

    feature_dict = {"door": door_feature, "body": body_feature,
                    "cloak": cloak_feature, "bag": bag_feature}

    puzzle_dict = None

    # Instantiate room object.
    fortress_entrance = Room(name, description, item_list, monster_list,
                             player, adjacent_rooms, door_map, feature_dict,
                             puzzle_dict)

    return fortress_entrance


def init_room_2():
    """Instantiates entrance_hall room.

    Returns:
        :obj:Room: Room object.

    """
    name = "entrance hall"
    description = ("Inside the fortress it is dark. There is rubble on the "
                   "floor from a partially collapsed left wall. Moonlight "
                   "shines through a gap in part of the collapsed wall, "
                   "revealing what looks to be a painted door on the east "
                   "side of the room. Behind me to the south are the large "
                   "oak double doors. Above the painted door to the east you "
                   "can barely make out some writing...",
                   "I'm in the entrance hall, there's goblin writing on the "
                   "wall. A painted door to the east leads to the mess hall. "
                   "To the south are large oak double doors leading to the "
                   "fortress entrance."
                   )

    # Init items
    # Item 1 - chest_key
    chest_key_name = "key"
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
                      'south': 'fortress entrance', 'west': None}

    # Tracks which doors are locked.  False means unlocked.
    door_map = {'east': False, 'south': False}

    goblin_graffiti_feature = ("You've seen this type of writing before at "
                               "the entrance to the high mountains near the "
                               "edge of your homeland. This is goblin "
                               "graffiti, used to mark a particular goblin "
                               "clans home."
                               )

    east_door_feature = ("An oak door with a large iron handle.")

    rubble_feature = ("Mostly stone from the wall strewn across the floor. "
                      "As you look at the rubble on the ground you also "
                      "noticea a thin rope secured across the path from here "
                      "to the door.")

    feature_dict = {"writing": goblin_graffiti_feature,
                    "rubble": rubble_feature, "door": east_door_feature}

    puzzle_dict = {"rope": True}

    entrance_hall = Room(name, description, item_list, monster_list, player,
                         adjacent_rooms, door_map, feature_dict, puzzle_dict)

    return entrance_hall


def init_room_3():
    """Instantiates mess_hall room.

    Returns:
        :obj:Room: Room object.

    """
    name = "mess hall"
    description = ("A long dark room appears before you. It looks as though "
                   "this is where the people of the mansion eat. There are "
                   "two long tables that stretch the full length of the room "
                   "and there are suits of armor lining both walls. The "
                   "tables still have dirty plates scattered about. On the "
                   "north side of the room is an old steel door with a "
                   "strange engraving at its center. To the east "
                   "there is a large oak door. To the west, the painted door "
                   "leads back to the entrance hall.",
                   "I'm in the mess hall. To the north a steel door goes to "
                   "the kitchen. To the east a large oak door leads to the "
                   "store room. To the west a painted door leads to the "
                   "entrance hall."
                   )

    # Init items
    # Item 1 - bread
    bread_name = "bread"
    bread_description = ("A fresh chunk of French bread.")
    bread_durability = 1
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

    armor_feature = ("The suits of armor are old and dusty.")

    engraving_feature = ("A closer inspection reveals that the engraving is "
                         "on a disc of silver that is attached to, but not "
                         "quite flush with, the surface of the door. Strange "
                         "markings cover the surface of the engraving and are "
                         "pictured below. \n\n"
                         "              / _______ \\              \n"
                         "             /           \\             \n"
                         "            |   /IIIII\\   |            \n"
                         "            |  |IIIIIII|  |            \n"
                         "            | *\\___!___*  |            \n"
                         "            .///       \\\\\\.            \n"
                         "          /__   ./| |\\ .   _\\          \n"
                         "         /       \\. ./       \\         \n"
                         "         |  /__  \\   / ___\\   |        \n"
                         "        /| |     /   \\    |  |\\        \n"
                         "       / |. -----\"   \"-----  | \\       \n"
                         "       / / ______     ______ \\ \\       \n"
                         "      | |     -         -     | |      \n"
                         "      |.|                     |.|      \n"
                         "       |                       |       \n"
                         "        \\-                    -/       \n"
                         "          \\-                -/         \n"
                         "            ________________           \n")

    feature_dict = {"armor": armor_feature, "engraving": engraving_feature}

    puzzle_dict = {"engraving": True, "armor": True}

    # Instantiate room object.
    mess_hall = Room(name, description, item_list, monster_list, player,
                     adjacent_rooms, door_map, feature_dict, puzzle_dict)

    return mess_hall


def init_room_4():
    """Instantiates store_room room.

    Returns:
        :obj:Room: Room object.

    """
    name = "store room"
    description = ("The room you are in has large shelves that go from floor "
                   "ceiling. There is a stone area for refrigeration where "
                   "animal carcasses hang from the ceiling. Nearby a broom "
                   "leans against the wall. "
                   "To the west a large oak door leads to the mess hall. To "
                   "the north dark black vines have entirely covered a "
                   "steel door.",
                   "I'm in the store room. To the west a large oak door leads "
                   "to the mess hall and to the north a vine covered steel "
                   "door."
                   )

    # Init items
    # Item 1 - empty_jar
    empty_jar_name = "jar"
    empty_jar_description = ("A clear, empty jar. This might come in handy "
                             "later.")
    empty_jar_durability = None
    empty_jar_stats = None

    empty_jar = Item(empty_jar_name, empty_jar_description,
                     empty_jar_durability, empty_jar_stats)

    # Set item list
    item_list = []
    item_list.append(empty_jar)

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

    vines_feature = ("You've never seen a plant like this. The vines are "
                     "unnaturally dark and thick.")

    shelves_feature = ("The shelves are mostly empty. Looks like they haven't "
                       "stocked in a while. You do notice a small lock box on "
                       "one of the shelves though.")

    animal_carcass = ("Looks like a deer carcass.")

    lock_box_feature = ("The lock box is small but elaborate. It is made "
                        "of wood but has gold trim on its edges.")

    feature_dict = {"lock box": lock_box_feature, "broom": broom_feature,
                    "shelves": shelves_feature, "carcass": animal_carcass,
                    "vines": vines_feature}

    puzzle_dict = {"lock box": False, "vines": True, "voice": True,
                   "shelves": True}

    # Instantiate room object.
    store_room = Room(name, description, item_list, monster_list, player,
                      adjacent_rooms, door_map, feature_dict, puzzle_dict)

    return store_room


def init_room_5():
    """Instantiates kitchen room.

    Returns:
        :obj:Room: Room object.

    """
    name = "kitchen"
    description = ("The room before you is clearly the kitchen of the "
                   "fortress. There are fish still on cutting boards. "
                   "The smell is rancid. It appears as though no one has "
                   "cleaned the kitchen for a very long time. To the south "
                   "a steel door leads to the mess hall.",
                   "I'm in the kitchen. To the south a steel door leads to "
                   "the mess hall."
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
    fish_feature = ("Sushi anyone? On second thought maybe not...")

    sink_feature = ("The massive double basin sink is filled to the brim "
                    "with dishes covered in sludge. ")

    feature_dict = {"fish": fish_feature, "sink": sink_feature}

    puzzle_dict = None

    # Instantiate room object.
    kitchen = Room(name, description, item_list, monster_list, player,
                   adjacent_rooms, door_map, feature_dict, puzzle_dict)

    return kitchen


def init_room_6():
    """Instantiates washroom.

    Returns:
        :obj:Room: Room object.

    """
    name = "washroom"
    description = ("The room before you is a pristine washroom "
                   "there is a massive tub in the middle of the "
                   "room with a large window behind it. It is too "
                   "dark to see what is likely a gorgeous view of the "
                   "forest. You also see a fountain in the corner. "
                   "I'm in the washroom. There is a swinging door "
                   "leading to stairs back to the store room, an ornate "
                   "door to the west, and a maple door to the north. "
                   )

    # Init items

    # Set item list
    item_list = []

    # Set monster list
    # ADD A WRAITH TO THIS ROOM &^T*Y(&^&%*()&^&*()^%&()^%&(^&))
    monster_list = []

    # Set player to None
    player = None

    # Set room navigation traits.
    adjacent_rooms = {'north': 'smoking room', 'east': None,
                      'south': 'store room', 'west': 'sleeping chambers'}
    door_map = {'north': False, 'south': False, 'west': False}

    # Set features in room.
    tub_feature = ("As you go near the tub you hear the sound of rushing "
                   "water flowing far down the drain. You hear the sound "
                   "of wood cracking down the drain too... Could it be "
                   "beavers..? "
                   )

    fountain_feature = ("The fountain starts flowing translucent purple "
                        "water. It looks like it could be poisonous. ")

    feature_dict = {"tub": tub_feature, "fountain": fountain_feature}

    puzzle_dict = None

    # Instantiate room object.
    washroom = Room(name, description, item_list, monster_list, player,
                    adjacent_rooms, door_map, feature_dict, puzzle_dict)

    return washroom


def init_room_7():
    """Instantiates smoking room.

    Returns:
        :obj:Room: Room object.

    """
    name = "smoking room"
    description = ("The room before you has a lucious red carpet. There "
                   "is a large chair with gold stitching. On one wall is "
                   "a large humidor that stands out in the dimly lit room. "
                   "There is a table in the middle of the room with a crystal "
                   "ash tray. The room has a strong scent of smoke. "
                   "I'm in the smoking room. To the south there is a "
                   "maple door and to the west there is a mahogany door. "
                   )

    # Init items
    # Item 1 - Key
    key_name = "Key"
    key_description = ("A golden key that has an embedded emerald in it. ")
    key_durability = None
    key_stats = None

    key = Item(key_name, key_description, key_durability, key_stats)

    # Set item list
    item_list = []
    item_list.append(key)

    # Set monster list
    monster_list = []

    # Set player to None
    player = None

    # Set room navigation traits.
    adjacent_rooms = {'north': None, 'east': None, 'south': 'washroom',
                      'west': 'supplies closet'}
    door_map = {'south': False, 'west': False}

    # Set features in room.
    humidor_feature = ("The humidor on the wall has a warm glow to it. "
                       "As you stare at the massive glass case, you feel "
                       "the room start to heat up. As the temperature "
                       "becomes concerningly hot, you turn away and feel "
                       "the heat dissipate immediately. "
                       )

    ash_feature = ("You walk towards the ash tray and just when you are "
                   "about to touch it, the ash from the ash tray spreads "
                   "out towards the edges of the tray. It slowly regathers "
                   "in the middle and spells out \"LEAVE NOW\""
                   )

    feature_dict = {"humidor": humidor_feature, "ash": ash_feature}

    puzzle_dict = None

    # Instantiate room object.
    smoking_room = Room(name, description, item_list, monster_list, player,
                        adjacent_rooms, door_map, feature_dict, puzzle_dict)

    return smoking_room


def init_room_8():
    """Instantiates sleeping chambers.

    Returns:
        :obj:Room: Room object.

    """
    name = "sleeping chambers"
    description = ("The room in front of you is gigantic. There are "
                   "vaulted ceilings and massive windows along the "
                   "western wall. The bed has four large posts that "
                   "have drapes around it. The room is dimly lit "
                   "and it is immaculately clean. "
                   "I'm in the sleeping chambers. There is an ornate "
                   "door to the east and a walnut door to the north. "
                   )

    # Init items
    # Item 1 - Healing Potion
    healing_potion_name = "Healing Potion"
    healing_potion_description = ("A glass vial of thick red liquid. ")
    healing_potion_durability = None
    healing_potion_stats = {"health": 5}

    healing_potion = Item(healing_potion_name, healing_potion_description,
                          healing_potion_durability, healing_potion_stats)

    # Set item list
    item_list = []
    item_list.append(healing_potion)

    # Set monster list
    monster_list = []

    # Set player to None
    player = None

    # Set room navigation traits.
    adjacent_rooms = {'north': 'supplies closet', 'east': 'washroom',
                      'south': None, 'west': None}
    door_map = {'north': False, 'east': False}

    # Set features in room.
    bed_feature = ("The drapes of the bed begin to flutter and the covers "
                   "sink into the middle of the floor, only to fly back up "
                   "lifting the entire bed frame off the ground before it "
                   "slams back down to the floor. "
                   )

    window_feature = ("The large clear glass window panes begin to transform "
                      "into small pieces of colored glass. A gorgeous mural "
                      "appears before you. It depicts a fox being hunted in "
                      "a lush forest. The scene disappears after a few "
                      "seconds. "
                      )

    feature_dict = {"bed": bed_feature, "window": window_feature}

    puzzle_dict = None

    # Instantiate room object.
    sleeping_chambers = Room(name, description, item_list, monster_list,
                             player, adjacent_rooms, door_map, feature_dict,
                             puzzle_dict)

    return sleeping_chambers


def init_room_9():
    """Instantiates supplies closet.

    Returns:
        :obj:Room: Room object.

    """
    name = "supplies closet"
    description = ("There is a piercing cold light that illuminates the "
                   "room before you. The walls are lined with shelves "
                   "and the room is much smaller than the other rooms "
                   "you have been in. The shelves have a high stack of "
                   "towels, as well as shampoo and soap. Even though the "
                   "room should smell good, it wreaks of goblin. "
                   "I'm in the supplies closet. There is an mahogany "
                   "door to the east and a walnut door to the south, and "
                   "a birch door to the north. "
                   )

    # Init items
    # Item 1 - Rapier
    rapier_name = "Rapier"
    rapier_description = ("A thin and nimble long sword. The blade "
                          "glows blue and it is razor sharp. ")
    rapier_durability = None
    rapier_stats = {"attack_power": 5}

    rapier = Item(rapier_name, rapier_description, rapier_durability,
                  rapier_stats)

    # Set item list
    item_list = []
    item_list.append(rapier)

    # Set monster list
    # ADD A GOBLIN HERE &^*(^%&*(^%$*()&%$*(%$^&*(*%$^&*%$&%*^%$%&*^%$^%^%))))
    monster_list = []

    # Set player to None
    player = None

    # Set room navigation traits.
    adjacent_rooms = {'north': 'pool room', 'east': 'smoking room',
                      'south': 'sleeping chambers', 'west': None}
    door_map = {'north': True, 'east': False, 'south': False}

    # Set features in room.
    towel_feature = ("The towel at the top of the towels stacked on "
                     "top of each other slowly rises up and starts "
                     "to snap at you in your general direction. It "
                     "would be wise to avoid getting closer to it. "
                     )

    shampoo_feature = ("The container top flies off and a giant glob "
                       "of shampoo gets in your hair and starts bubbling "
                       "more and more. It then vanishes instantly and "
                       "your hair looks and feels amazing. "
                       )

    feature_dict = {"towel": towel_feature, "shampoo": shampoo_feature}

    puzzle_dict = None

    # Instantiate room object.
    supplies_closet = Room(name, description, item_list, monster_list,
                           player, adjacent_rooms, door_map, feature_dict,
                           puzzle_dict)

    return supplies_closet


def init_room_10():
    """Instantiates pool room.

    Returns:
        :obj:Room: Room object.

    """
    name = "pool room"
    description = (""
                   "I'm in the pool room. There is a birch door to the "
                   "south and a marble staircase to the north. "
                   )

    # Init items

    # Set item list
    item_list = []

    # Set monster list
    monster_list = []

    # Set player to None
    player = None

    # Set room navigation traits.
    adjacent_rooms = {'north': 'tower hall', 'east': None,
                      'south': 'supplies closet', 'west': None}
    door_map = {'north': False, 'south': False}

    # Set features in room.
    pool_feature = (""
                    )

    waterfall_feature = (""
                         )

    feature_dict = {"pool": pool_feature, "waterfall": waterfall_feature}

    puzzle_dict = None

    # Instantiate room object.
    pool_room = Room(name, description, item_list, monster_list,
                     player, adjacent_rooms, door_map, feature_dict,
                     puzzle_dict)

    return pool_room


def init_room_11():
    """Instantiates tower hall.

    Returns:
        :obj:Room: Room object.

    """
    name = "tower hall"
    description = (""
                   "I'm in the pool room. There is a birch door to the "
                   "south and a marble staircase to the north. "
                   )

    # Init items

    # Set item list
    item_list = []

    # Set monster list
    monster_list = []

    # Set player to None
    player = None

    # Set room navigation traits.
    adjacent_rooms = {'north': 'archives', 'east': None,
                      'south': 'pool room', 'west': None}
    door_map = {'north': True, 'south': False}

    # Set features in room.
    _feature = (""
                )

    _feature = (""
                )

    feature_dict = {"": _feature, "": _feature}

    puzzle_dict = None

    # Instantiate room object.
    tower_hall = Room(name, description, item_list, monster_list,
                      player, adjacent_rooms, door_map, feature_dict,
                      puzzle_dict)

    return tower_hall


def init_room_12():
    """Instantiates archives.

    Returns:
        :obj:Room: Room object.

    """
    name = "archives"
    description = (""
                   "I'm in the pool room. There is a birch door to the "
                   "south and a marble staircase to the north. "
                   )

    # Init items

    # Set item list
    item_list = []

    # Set monster list
    monster_list = []

    # Set player to None
    player = None

    # Set room navigation traits.
    adjacent_rooms = {'north': None, 'east': 'reading room',
                      'south': 'tower hall', 'west': 'room of last rights'}
    door_map = {'east': False, 'south': False, 'west': True}

    # Set features in room.
    _feature = (""
                )

    _feature = (""
                )

    feature_dict = {"": _feature, "": _feature}

    puzzle_dict = None

    # Instantiate room object.
    archives = Room(name, description, item_list, monster_list,
                    player, adjacent_rooms, door_map, feature_dict,
                    puzzle_dict)

    return archives


def init_room_13():
    """Instantiates reading room.

    Returns:
        :obj:Room: Room object.

    """
    name = "reading room"
    description = (""
                   "I'm in the pool room. There is a birch door to the "
                   "south and a marble staircase to the north. "
                   )

    # Init items

    # Set item list
    item_list = []

    # Set monster list
    monster_list = []

    # Set player to None
    player = None

    # Set room navigation traits.
    adjacent_rooms = {'north': None, 'east': None, 'south': None,
                      'west': 'archives'}
    door_map = {'north': False, 'south': False}

    # Set features in room.
    _feature = (""
                )

    _feature = (""
                )

    feature_dict = {"": _feature, "": _feature}

    puzzle_dict = None

    # Instantiate room object.
    reading_room = Room(name, description, item_list, monster_list,
                        player, adjacent_rooms, door_map, feature_dict,
                        puzzle_dict)

    return reading_room


def init_room_objects():
    """Creates the starting game objects.

    Returns:
        list(:obj:Room): List of all room objects in game.

    """
    room_list = []

    fortress_entrance = init_room_1()
    entrance_hall = init_room_2()
    mess_hall = init_room_3()
    store_room = init_room_4()
    kitchen = init_room_5()
    washroom = init_room_6()
    smoking_room = init_room_7()
    sleeping_chambers = init_room_8()
    supplies_closet = init_room_9()
    pool_room = init_room_10()
    tower_hall = init_room_11()
    archives = init_room_12()
    reading_room = init_room_13()
    # room_of_last_rights = init_room_14()
    # lair = init_room_15()

    room_list.extend((fortress_entrance, entrance_hall, mess_hall, store_room,
                      kitchen, washroom, smoking_room, sleeping_chambers,
                      supplies_closet, pool_room, tower_hall, archives,
                      reading_room))

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
    object_name = object_name.replace(" ", "_")

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
    object_name = game_object.get_name()

    object_name = object_name.replace(" ", "_")

    file_path = Path("game_files/current_game/")

    file_name = object_name + '.bin'

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
                              "(no special characters or spaces allowed)\n")

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


def load_game():
    """Enables user to load prior saved game."""
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
        if (user_input.isalpha() and user_input != 'e') or " " in user_input:
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
    user_input = user_input.lower().strip()

    # Verify that user has entered a valid integer within the range of 1
    # to the total number of files.
    valid_input = False
    while not valid_input:
        if user_input.isalpha() or " " in user_input:
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
