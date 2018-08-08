from game_classes import *
from scroll_print import *
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
    description = ("At the end of the path in a clearing, there is a large "
                   "stone fortress. Nothing grows near the fortress walls. "
                   "North of the fortress entrance, there's a pair of large "
                   "oak double doors leading to the entrance hall. Just "
                   "outside the entrance is a body on the ground. Could it "
                   "be your brother Evelyn?",
                   "You're at the fortress entrance. To the north, large oak "
                   "double doors lead to the entrance hall."
                   )

    # Init items
    # Item 1 - rusty_sword
    sword_name = "sword"
    sword_description = ("A rusty sword. It's long since lost its edge. "
                         "Who knows, you might be able to bludgeon monsters "
                         "with it. (Equip this item to gain stats)")
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

    body_feature = ("The body comes into view. you see that it is formed "
                    "of a heavy traveling cloak and bag. Bones peak out from "
                    "underneath. You recognize the clothes as the kind worn "
                    "by traveling traders in the mountains. This body has "
                    "been here a while."
                    )

    cloak_feature = "The cloak is old and torn. It will not be of use."

    bag_feature = ("The bag is empty and torn. Nothing of the trader's goods "
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
                   "side of the room, leading to the mess hall. Behind you "
                   "to the south are the large oak double doors leading back "
                   "to the fortress entrance. Above the painted door to the "
                   "east you can barely make out some writing....",
                   "You're in the entrance hall. There's goblin writing on "
                   "the wall. To the east, there is a painted door leading to "
                   "the mess hall. To the south, there are large oak double "
                   "doors leading to the fortress entrance."
                   )

    # Init items
    # Item 1 - chest_key
    chest_key_name = "golden key"
    chest_key_description = ("An elaborate golden key.")
    chest_key_durability = 1
    chest_key_stats = None

    chest_key = Item(chest_key_name, chest_key_description,
                     chest_key_durability, chest_key_stats)

    # Set item list
    item_list = []
    item_list.append(chest_key)

    # Set monster list
    goblin_name = "Skrag"
    goblin_description = ("There is a goblin with green skin and pointy ears "
                          "in the corner of the room. He is missing an eye "
                          "and carries a chipped machete. He notices you "
                          "when you enter the room. He screams and runs "
                          "towards you with his machete raised! ")
    goblin_loot = 5
    goblin_health = 8
    goblin_magic = 9
    goblin_level = 1
    goblin_magic_defense = 5
    goblin_magic_power = 2
    goblin_defense = 3
    goblin_attack_power = 3

    goblin = Monster(goblin_name, goblin_description, goblin_loot,
                     goblin_health, goblin_magic, goblin_level,
                     goblin_magic_defense, goblin_magic_power, goblin_defense,
                     goblin_attack_power)

    monster_list = []
    monster_list.append(goblin)

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
                               "clan's home."
                               )

    east_door_feature = ("An oak door with a large iron handle.")

    rubble_feature = ("It's mostly stone from the wall strewn across the "
                      "floor. As you look at the rubble on the ground, you "
                      "also notice a a thin rope secured across the path from "
                      "here to the door.")

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
    description = ("A long, dark room appears before you. It looks as though "
                   "this is where the people of the mansion eat. There are "
                   "two long tables that stretch the full length of the room "
                   "and there are suits of armor lining both walls. The "
                   "tables still have dirty plates scattered about. On the "
                   "north side of the room is an old steel door with a "
                   "strange engraving at its center. This door goes to the "
                   "kitchen. To the east, there is a large oak door. This "
                   "door goes to the store room. To the west, the painted "
                   "door leads back to the entrance hall.",
                   "You're in the mess hall. To the north, there is an old "
                   "steel door leading to the kitchen. To the east, a large "
                   "oak door leads to the store room. To the west, a painted "
                   "door leads back to the entrance hall."
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
    skeleton_name = "Renethe"
    skeleton_description = ("There is a pile of bones on the ground "
                            "near an elaborate suit of armor. As you walk "
                            "further into the hall, the bones begin to "
                            "reassemble and fill the armor. The armored "
                            "skeleton unsheathes its broadsword. ")
    skeleton_loot = 5
    skeleton_health = 15
    skeleton_magic = 15
    skeleton_level = 2
    skeleton_magic_defense = 5
    skeleton_magic_power = 6
    skeleton_defense = 4
    skeleton_attack_power = 7

    skeleton = Monster(skeleton_name, skeleton_description, skeleton_loot,
                       skeleton_health, skeleton_magic, skeleton_level,
                       skeleton_magic_defense, skeleton_magic_power,
                       skeleton_defense, skeleton_attack_power)

    monster_list = []
    monster_list.append(skeleton)

    # Set player to None
    player = None

    # Set room navigation traits.
    adjacent_rooms = {'north': 'kitchen', 'east': 'store room', 'south': None,
                      'west': 'entrance hall'}
    door_map = {'north': True, 'east': False, 'west': False}

    # Set features in room.

    armor_feature = ("The suits of armor are old and dusty.")

    engraving_feature = ("                _______                 \n"
                         "              /         \\              \n"
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
                         "            ________________           \n"
                         )

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
                   "to ceiling. There is a stone area for refrigeration where "
                   "animal carcasses hang from the ceiling. Nearby, a broom "
                   "leans against the wall. You appear to be in the store "
                   "room. To the west, a large oak door leads to the mess "
                   "hall. To the north dark black vines have entirely "
                   "blocked the entrance to a stairwell, which leads to the "
                   "washroom.",
                   "You're in the store room. To the west, a large oak door "
                   "leads to the mess hall. To the north, dark black vines "
                   "block a stairwell leading to the washroom."
                   )

    # Init items
    # Item 1 - empty_jar
    empty_jar_name = "jar"
    empty_jar_description = ("A clear, empty jar. Possibly used to hold "
                             "potions or other dangerous substances.")
    empty_jar_durability = 1
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

    feature_dict = {"box": lock_box_feature, "broom": broom_feature,
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
                   "cleaned the kitchen for a very long time. To the south, "
                   "a steel door leads to the mess hall.",
                   "You're in the kitchen. To the south, a steel door leads "
                   "to the mess hall."
                   )

    # Init items
    # Item 1 - magic_resistant_oven_mitt
    oven_mitt_name = "oven mitt"
    oven_mitt_description = ("The oven mitt glows with an orange magical hue. "
                             "The outside is warm to the touch. (Equip this "
                             "item to gain stats)")
    oven_mitt_durability = None
    oven_mitt_stats = {"magic_defense": 3}

    oven_mitt = Item(oven_mitt_name, oven_mitt_description,
                     oven_mitt_durability, oven_mitt_stats)

    ooze_name = "acidic ooze"
    ooze_description = ("This green ooze eats through anything it touches. "
                        "You'll need a special kind of container to hold "
                        "this.")
    ooze_durability = 1
    ooze_stats = None

    ooze = Item(ooze_name, ooze_description, ooze_durability, ooze_stats)
    # Set item list
    item_list = []
    item_list.extend((oven_mitt, ooze))

    # Set monster list
    sludge_name = "Grugg"
    sludge_description = ("You hear the sink start to make an odd gurgling "
                          "noise. A large slimy green sludge bursts from "
                          "the sink drain into the air. It settles on the "
                          "ground and forms into a giant blob over 7 feet "
                          "tall. ")
    sludge_loot = 10
    sludge_health = 25
    sludge_magic = 40
    sludge_level = 3
    sludge_magic_defense = 10
    sludge_magic_power = 12
    sludge_defense = 7
    sludge_attack_power = 10

    sludge = Monster(sludge_name, sludge_description, sludge_loot,
                     sludge_health, sludge_magic, sludge_level,
                     sludge_magic_defense, sludge_magic_power,
                     sludge_defense, sludge_attack_power)

    monster_list = []
    monster_list.append(sludge)

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

    puzzle_dict = {"ooze": True}

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
    description = ("The room before you is a pristine washroom. "
                   "There is a massive tub in the middle of the "
                   "room with a large window behind it. It is too "
                   "dark to see what is likely a gorgeous view of the "
                   "forest. You also see a fountain in the corner. To the "
                   "south, a stairwell leads back down to the store room. "
                   "To the west, an ornate door leads to the sleeping "
                   "chambers. To the north, a maple door takes you to the "
                   "smoking room.",
                   "You're in the washroom. To the south, a stairwell "
                   "leads back down to the store room. To the west, an ornate "
                   "door leads to the sleeping chambers. To the north, a "
                   "maple door leads to the smoking room."
                   )

    # Init items

    # Set item list
    item_list = []

    # Set monster list
    wraith_name = "Karthos"
    wraith_description = ("A screaming howling sound echoes through the "
                          "room. You see faint black wisps fly smoothly "
                          "through the air. The black smoke gathers and "
                          "a wraith with a silver dagger appears before "
                          "you! ")
    wraith_loot = 10
    wraith_health = 25
    wraith_magic = 40
    wraith_level = 3
    wraith_magic_defense = 10
    wraith_magic_power = 12
    wraith_defense = 7
    wraith_attack_power = 10

    wraith = Monster(wraith_name, wraith_description, wraith_loot,
                     wraith_health, wraith_magic, wraith_level,
                     wraith_magic_defense, wraith_magic_power,
                     wraith_defense, wraith_attack_power)

    monster_list = []
    monster_list.append(wraith)

    # Set player to None
    player = None

    # Set room navigation traits.
    adjacent_rooms = {'north': 'smoking room', 'east': None,
                      'south': 'store room', 'west': 'sleeping chambers'}
    door_map = {'north': False, 'south': False, 'west': False}

    # Set features in room.
    tub_feature = ("As you go near you hear the sound of rushing "
                   "water flowing far down the drain. You hear the sound "
                   "of wood cracking down the drain too... Could it be "
                   "beavers..?"
                   )

    fountain_feature = ("The fountain starts flowing translucent purple "
                        "water. It looks like it could be poisonous.")

    feature_dict = {"tub": tub_feature, "fountain": fountain_feature}

    puzzle_dict = {"rubber duck": True}

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
    description = ("The room before you has a luscious red carpet. There "
                   "is a large chair with gold stitching. By the chair there "
                   "is a table with a crystal ash tray on it. Little wisps of "
                   "smoke drift up from the leftover embers in the tray. On "
                   "one wall is a large humidor that stands out in the dimly "
                   "lit room. The room has a strong scent of smoke. To the "
                   "south, there is a maple door leading to the washroom. To "
                   "the west, there is a mahogany door to the supplies "
                   "closet.",
                   "You're in the smoking room. To the south, there is a "
                   "maple door to the washroom. To the west, there is a "
                   "mahogany door to the supplies closet."
                   )

    # Init items

    # Set item list
    item_list = []

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

    ash_feature = ("The ash embers have cooled. you walk towards the ash tray "
                   "and just when you are about to touch it, the ash from the "
                   "ash tray spreads out towards the edges of the tray. It "
                   "slowly regathers in the middle and spells out "
                   "\"LEAVE NOW\""
                   )

    feature_dict = {"humidor": humidor_feature, "ash tray": ash_feature}

    puzzle_dict = {"smoke": False}

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
                   "vaulted ceilings and a massive window along the "
                   "western wall. The bed has four large posts that "
                   "have drapes around it. The room is dimly lit "
                   "and it is immaculately clean. Near the bed is a "
                   "nightstand with a small emerald colored lock box on it. "
                   "There is an ornate door to the east that leads to a "
                   "washroom and a walnut door to the north that leads to "
                   "the supplies closet.",
                   "You're in the sleeping chambers. To the east, there is an "
                   "ornate door leading to the washroom. To the north, there "
                   "is a walnut door leading to the supplies closet. "
                   )

    # Init items
    book_name = ("book")
    book_description = ("The title reads: \"Magic Encryption for Dummies. Now "
                        "You Too Can Keep Your Magic Secret!\" There is a "
                        "bookmark midway through the book. You open the it "
                        "and read a passage. It says: \"Here we have an "
                        "example of a magical cypher. Simply set your magic "
                        "mirror to display the coded text of your choosing. "
                        "Then simply speak the decoded phrase allowed to "
                        "cast the automatic spell. Cipher:")
    book_durability = None
    book_stats = None

    book = Item(book_name, book_description, book_durability, book_stats)

    # Set item list
    item_list = []

    item_list.append(book)

    # Set monster list
    monster_list = []

    # Set player to None
    player = None

    # Set room navigation traits.
    adjacent_rooms = {'north': 'supplies closet', 'east': 'washroom',
                      'south': None, 'west': None}
    door_map = {'north': False, 'east': False}

    # Set features in room.
    emerald_box_feature = ("The lock box is emerald green and ornate. You "
                           "can see that you need a key to open the box.")

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

    feature_dict = {"bed": bed_feature, "window": window_feature,
                    "box": emerald_box_feature}

    puzzle_dict = {"nightstand": True}

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
                   "room should smell good, it reeks of goblin. There is "
                   "a mahogany door to the east that leads to the smoking "
                   "room and a walnut door to the south that leads to the "
                   "sleeping chambers. A birch door to the north leads to "
                   "the sauna room.",
                   "You're in the supplies closet. To the east, there is a "
                   "mahogany door that leads to the smoking room. To the "
                   "south, there is a walnut door that leads to the sleeping "
                   "chambers. To the north, there is a birch door that leads "
                   "to the sauna room."
                   )

    # Init items

    # Set item list
    item_list = []

    # Set monster list
    goblin_name = "Ulthu"
    goblin_description = ("There is what looks like a goblin foot sticking "
                          "out from under a towel. You hear snoring beneath "
                          "it. As you step into the room, the floor creaks "
                          "loudly. The goblin wakes up immediately and sits "
                          "up. The goblin has lots of dried dirt all over his "
                          "skin. He is carries a sickle and a sling for "
                          "throwing small rocks. ")
    goblin_loot = 8
    goblin_health = 13
    goblin_magic = 15
    goblin_level = 2
    goblin_magic_defense = 5
    goblin_magic_power = 5
    goblin_defense = 5
    goblin_attack_power = 6

    goblin = Monster(goblin_name, goblin_description, goblin_loot,
                     goblin_health, goblin_magic, goblin_level,
                     goblin_magic_defense, goblin_magic_power, goblin_defense,
                     goblin_attack_power)

    monster_list = []
    monster_list.append(goblin)

    # Set player to None
    player = None

    # Set room navigation traits.
    adjacent_rooms = {'north': 'sauna room', 'east': 'smoking room',
                      'south': 'sleeping chambers', 'west': None}
    door_map = {'north': False, 'east': False, 'south': False}

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

    shelves_feature = ("The contain mostly towels. You do notice a blue "
                       "light at the very top of one of the shelves. You "
                       "can't quite make out what it is from your vantage "
                       "point on the ground.")

    feature_dict = {"towel": towel_feature, "shampoo": shampoo_feature,
                    "shelves": shelves_feature}

    puzzle_dict = {"shelves": True}

    # Instantiate room object.
    supplies_closet = Room(name, description, item_list, monster_list,
                           player, adjacent_rooms, door_map, feature_dict,
                           puzzle_dict)

    return supplies_closet


def init_room_10():
    """Instantiates sauna room.

    Returns:
        :obj:Room: Room object.

    """
    name = "sauna room"
    description = ("A wave of steam and heat hits you. The steam is so thick "
                   "you can't see anything. You here the faint sound of "
                   "machinery. There is a birch door to the south, but the "
                   "way forward is not clear.",
                   "You're in the sauna room. There is a birch door to the "
                   "south. The way forward is not clear. "
                   )

    # Init items

    # Set item list
    item_list = []

    # Set monster list
    monster_list = []

    # Set player to None
    player = None

    # Set room navigation traits.
    adjacent_rooms = {'north': None, 'east': None,
                      'south': 'supplies closet', 'west': None}
    door_map = {'south': False}

    # Set features in room.
    machine_sound_feature = ("You follow the sound of the machinery through "
                             "the haze of steam. It leads you to a marble "
                             "wall. There is a mirror on the wall. Higher "
                             "up there is a vent which is exuding steam.")

    mirror_feature = ("Strangely it does not reflect "
                      "your image. Instead letters appear. On the mirror's "
                      "surface it reads: \"Speak the password: SDVVZRUG\"")

    feature_dict = {"machinery": machine_sound_feature,
                    "mirror": mirror_feature}

    puzzle_dict = {"steam": True, "sauna voice": True}

    # Instantiate room object.
    sauna_room = Room(name, description, item_list, monster_list,
                      player, adjacent_rooms, door_map, feature_dict,
                      puzzle_dict)

    return sauna_room


def init_room_11():
    """Instantiates tower hall.

    Returns:
        :obj:Room: Room object.

    """
    name = "tower hall"
    description = ("You enter a room that is gigantic with an ornate vaulted "
                   "ceiling. There is also a massive painting on the wall "
                   "that spans almost the entire length of the room. At the "
                   "center of the room there is a small table with what looks "
                   "to be some items on it. There is a marble staircase to "
                   "the south leading back to the sauna room and large walnut "
                   "double doors to the north leading to the archives.",
                   "You're in the tower hall. To the south, there is a marble "
                   "staircase leading back to the sauna room. To the north, "
                   "there are large walnut double doors leading to the "
                   "archives."
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
                      'south': 'sauna room', 'west': None}
    door_map = {'north': False, 'south': False}

    # Set features in room.
    ceiling_feature = ("Not only is the ceiling very high, you notice "
                       "that it appears to look like a star filled night sky. "
                       "It makes you wonder if a ceiling is truly there... "
                       )

    painting_feature = ("The painting on the wall depicts a large medieval "
                        "battle. There are two distinct armies engaged in "
                        "brutal combat. You notice that a piece of the "
                        "painting has been torn away. Right where the face of "
                        "one of the commanders should have been, there is a "
                        "rend. It's as if someone deliberately tore this part "
                        "of the painting away. I wonder if the owner of this "
                        "place was involved in the battle."
                        )

    table_feature = ("You approach the table. On it are three items lined up "
                     "in a perfect row. The items are a piece of charcoal, a "
                     "ruby, and a small dagger with a jet black onyx blade. "
                     "Engraved on the table, just in front of the items, is "
                     "the sentence: \"What is black when you buy it, red "
                     "when you use it, and gray when you throw it away?\"")

    ruby_feature = ("The ruby is a deep crimson. It is large and must be "
                    "worth a fortune.")

    charcoal_feature = ("This is charcoal like the type your village smithy "
                        "would use to fuel his furnace.")

    dagger_feature = ("The quality of the dagger is astounding. It is like "
                      "no weapon you have seen before.")

    feature_dict = {"ceiling": ceiling_feature, "painting": painting_feature,
                    "table": table_feature, "ruby": ruby_feature,
                    "charcoal": charcoal_feature, "dagger": dagger_feature}

    puzzle_dict = {"riddle": True}

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
    description = ("The room before you is very dark. There are cobwebs "
                   "scattered around the room and it is quite dusty. "
                   "There is a fireplace roaring in the corner. Above you "
                   "is a very large chandelier that is made out of hundreds "
                   "of crystals. This appears to be the archives. Large "
                   "walnut doors to the south lead back to the tower hall. "
                   "An ash door to the east leads to the reading room, and a "
                   "pine door to the west leads to the room of last rites.",
                   "You're in the archives. To the south, large walnut doors"
                   "lead back to the tower hall. To the east, an ash door "
                   "leads to the reading room. To the west, a pine door leads "
                   "to the room of last rites."
                   )

    # Init items
    # Item 1 - Mythril Tongs
    tongs_name = "mythril tongs"
    tongs_description = ("Long pristine tongs with a lime green flame that "
                         "flows from the tips. They appear to be made out of "
                         "mythril. (Equip this item to gain stats)"
                         )
    tongs_durability = None
    tongs_stats = {"magic_power": 8}

    tongs = Item(tongs_name, tongs_description, tongs_durability,
                 tongs_stats)

    # Set item list
    item_list = []
    item_list.append(tongs)

    # Set monster list
    skeleton_name = "Exelior"
    skeleton_description = ("A skeleton walks out of the blazing fireplace. "
                            "It's bones are still engulfed in flames as it "
                            "lunges at you. ")
    skeleton_loot = 5
    skeleton_health = 20
    skeleton_magic = 20
    skeleton_level = 3
    skeleton_magic_defense = 8
    skeleton_magic_power = 10
    skeleton_defense = 7
    skeleton_attack_power = 8

    skeleton = Monster(skeleton_name, skeleton_description, skeleton_loot,
                       skeleton_health, skeleton_magic, skeleton_level,
                       skeleton_magic_defense, skeleton_magic_power,
                       skeleton_defense, skeleton_attack_power)

    monster_list = []
    monster_list.append(skeleton)

    # Set player to None
    player = None

    # Set room navigation traits.
    adjacent_rooms = {'north': None, 'east': 'reading room',
                      'south': 'tower hall', 'west': 'room of last rites'}
    door_map = {'east': False, 'south': False, 'west': False}

    # Set features in room.
    fireplace_feature = ("As you step toward the fireplace you hear it start "
                         "to crackle loudly. A face then appears in the "
                         "flames. It screams \"Run or you will face the same "
                         "fate as those you wish to save!\" Evelyn must be "
                         "near! "
                         )

    chandelier_feature = ("As you look at the chandelier it begins to rattle "
                          "loudly. Rain then begins to fall from the "
                          "and continues for about ten seconds before "
                          "stopping. A loud boom of thunder blasts through "
                          "the room and dust is kicked up into the air. "
                          )

    feature_dict = {"fireplace": fireplace_feature,
                    "chandelier": chandelier_feature}

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
    description = ("In the room before you, there is a long couch and "
                   "books all around the room, stacked to the ceiling. "
                   "In the middle of the room there is a table with a "
                   "large, old open tome on it. The pages are tattered "
                   "and it seems like it could be thousands of years "
                   "old. High on a perch and out of reach you notice a raven "
                   "looking down at you. This room looks like the reading "
                   "room. To your west, an ash door leads you back to the "
                   "archives.",
                   "You're in the reading room. To the west, an ash door "
                   "leads back to the archives."
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
    door_map = {'west': False}

    # Set features in room.
    tome_feature = ("As you approach the tome, the pages start flapping "
                    "quickly, going further along in the tome. All of a "
                    "sudden, it stops on a page. As you look at the page, "
                    "it is completely blank until text begins to appear. "
                    "It says, \"This tome holds spells only for the worthy.\" "
                    "The tome then returns to its original page. "
                    )

    couch_feature = ("As you step towards the couch, it begins to sink into "
                     "the ground. The closer you step to it, the further it "
                     "sinks, as you back away, it returns to its normal "
                     "position. "
                     )

    raven_feature = ("He has dark black feathers. Engraved at the base "
                     "of its perch is the name Artemis. The raven is carrying "
                     "a key in its beak currently. He is looking at "
                     "you with great interest.")

    feature_dict = {"tome": tome_feature, "couch": couch_feature,
                    "raven": raven_feature}

    puzzle_dict = {"raven": True}

    # Instantiate room object.
    reading_room = Room(name, description, item_list, monster_list,
                        player, adjacent_rooms, door_map, feature_dict,
                        puzzle_dict)

    return reading_room


def init_room_14():
    """Instantiates Room of Last Rites.

    Returns:
        :obj:Room: Room object.

    """
    name = "room of last rites"

    description = ("I feel like I'm close to Evelyn. Bones are scattered in "
                   "this room. A very daunting sight indeed! There is also a "
                   "bloody handscroll_print on the north wall of the room. "
                   "Near the center of the room a cage is hanging from a long "
                   "chain connected to the ceiling. There is a tungsten door "
                   "to the north leading to the final lair and a pine door to "
                   "the east, which leads back to the archives.",
                   "You're in the room of last rites. To the north, a "
                   "tungsten door leads to the final lair. To the east, a "
                   "pine door leads to the archives."
                   )

    # Init items

    # Set item list
    item_list = []

    # ADD CHEST/FAIRY??

    # Set monster list
    monster_list = []

    # Set player to None
    player = None

    # Set room navigation traits.
    adjacent_rooms = {'north': 'final lair', 'east': 'archives', 'south': None,
                      'west': None}
    door_map = {'north': True, 'east': False}

    # Set features in room.
    bones_feature = ("The bones look like they belong to animals, "
                     "perhaps some unlucky birds and squirrels. Phew, "
                     "thankfully none of them look like human remains."
                     )

    hand_print_feature = ("Wait a second, that hand print looks very "
                          "familiar. Could it be...? Yes, it looks like "
                          "Evelyn's hand print!")

    cage_feature = ("It is small and made of iron.")

    feature_dict = {"bones": bones_feature, "hand print": hand_print_feature,
                    "cage": cage_feature}

    puzzle_dict = {"cage": True}

    # Instantiate room object.
    room_of_last_rites = Room(name, description, item_list, monster_list,
                              player, adjacent_rooms, door_map, feature_dict,
                              puzzle_dict)

    return room_of_last_rites


def init_room_15():
    """Instantiates Final Lair.

    Returns:
        :obj:Room: Room object.

    """
    name = "final lair"
    description = ("Evelyn is curled up in the corner of this room. "
                   "There is also a mirror in the back of the "
                   "room. You're in the final lair. There is a tungsten "
                   "door to the south that leads to the room of last "
                   "rites.",
                   "You're in the final lair. There is a tungsten door "
                   "to the south that leads to the room of last rites."
                   )

    # Set item list
    item_list = []

    # Set monster list
    final_boss_name = "Zlor"
    final_boss_description = ("It is I, Zlor! I am afraid your journey "
                              "has come to an end! You are destined "
                              "to join the same fate as your brother! ")
    final_boss_loot = 30
    final_boss_health = 43
    final_boss_magic = 100
    final_boss_level = 5
    final_boss_magic_defense = 12
    final_boss_magic_power = 19
    final_boss_defense = 15
    final_boss_attack_power = 17

    final_boss = Monster(final_boss_name, final_boss_description,
                         final_boss_loot, final_boss_health, final_boss_magic,
                         final_boss_level, final_boss_magic_defense,
                         final_boss_magic_power, final_boss_defense,
                         final_boss_attack_power)

    monster_list = []
    monster_list.append(final_boss)

    # Set player to None
    player = None

    # Set room navigation traits.
    adjacent_rooms = {'north': None, 'east': None,
                      'south': 'room of last rites', 'west': None}
    door_map = {'south': False}

    # Set features in room.
    evelyn_feature = ("Other than a cut on his hand, Evelyn looks to "
                      "be in fairly good shape even though he's pretty "
                      "shaken up. 'Thanks for saving me', he says. 'I "
                      "think it's time we go home.'"
                      )

    mirror_feature = ("You see yourself in the mirror's reflection. Your face "
                      "is covered with cuts and bruises. Your eyes, too, "
                      "look different. Wiser and tougher, perhaps. Your hair "
                      "is matted with a mixture of blood and sweat."
                      )

    feature_dict = {"evelyn": evelyn_feature, "mirror": mirror_feature}

    puzzle_dict = None

    # Instantiate room object.
    final_lair = Room(name, description, item_list, monster_list,
                      player, adjacent_rooms, door_map, feature_dict,
                      puzzle_dict)

    return final_lair


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
    sauna_room = init_room_10()
    tower_hall = init_room_11()
    archives = init_room_12()
    reading_room = init_room_13()
    room_of_last_rites = init_room_14()
    final_lair = init_room_15()

    room_list.extend((fortress_entrance, entrance_hall, mess_hall, store_room,
                      kitchen, washroom, smoking_room, sleeping_chambers,
                      supplies_closet, sauna_room, tower_hall, archives,
                      reading_room, room_of_last_rites, final_lair))

    return room_list


def init_player_object(player_name, character_choice):
    """Instantiates the inital Player object.

    Returns:
        :obj:Player: Player object with attributes set.

    """
    name = player_name
    health = 50
    magic = 20
    level = 1
    magic_defense = 0
    magic_power = 3
    defense = 0
    # attack_power = 3
    # This AP for Testing Only ADLFKSLDFKSLDKFSLDKF#@$@$@#$@#$
    attack_power = 3000
    num_lives = 3
    experience = 0
    memory = []
    backpack = []
    equipped_item = None

    if character_choice == "Wizard":
        player = Wizard(name, health, magic, level, magic_defense, magic_power,
                        defense, attack_power, num_lives, experience, memory,
                        backpack, equipped_item)
    elif character_choice == "Ranger":
        player = Ranger(name, health, magic, level, magic_defense, magic_power,
                        defense, attack_power, num_lives, experience, memory,
                        backpack, equipped_item)

    return player


def init_game_files(player_name, character_choice):
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
    player = init_player_object(player_name, character_choice)

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
    scroll_print("\nSave Menu")

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
                    scroll_print("Invalid character: {}".format(file_name[i]))

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

        scroll_print("\nGame Saved.")

    # Overwrite saved game process.
    else:
        scroll_print("\nSaved files")

        file_path = Path("game_files/saved_games")
        game_files = os.listdir(str(file_path))

        scroll_print("Please type the number of the file you would like to "
                     "overwrite or type E to exit.")

        # scroll_print out a list of saved files. Names are the names of the
        # directories where the saved files are stored.
        num = 1
        file_list = []
        for file in game_files:
            scroll_print("({}) {}".format(num, file))

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

                scroll_print("\nGame Saved")

    scroll_print("\nSave Menu Exited.\n")


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
    scroll_print("\nLoad Menu")
    scroll_print("Please type the number of the file you would like to load "
                 "or press E to exit load menu.")

    file_path = Path("game_files/saved_games")
    game_files = os.listdir(str(file_path))

    # Display list of current saved games.
    num = 1
    file_list = []
    for file in game_files:
        scroll_print("({}) {}".format(num, file))

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

            scroll_print("\nGame {} loaded.\n".format(file_name))

    scroll_print("\nLoad Menu Exited\n")


def initial_load_game():
    """Load file from start menu.

    Returns:
        (:obj:Room): The loaded Room object.

    """
    scroll_print("\nLoad Menu")
    scroll_print("Please type the number of the file you would like to load.")

    file_path = Path("game_files/saved_games")
    game_files = os.listdir(str(file_path))

    # List possible files to load from stored files. Prepend numbers so that
    # user will enter a number to select the file they would like to load.
    num = 1
    file_list = []
    for file in game_files:
        scroll_print("({}) {}".format(num, file))
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

    scroll_print("\nGame {} loaded.\n".format(file_name))

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
