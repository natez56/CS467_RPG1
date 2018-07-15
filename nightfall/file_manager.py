from game_classes import *
from pathlib import Path
import pickle


def init_room_1():
    """Instantiates fortress_entrance room."""
    name = "dungeon_entrance"
    description = ("At the end of the path in a clearing there is a large "
                   "stone fortress. Nothing grows near the fortress walls. "
                   "There is a large double door of dark oak. Just outside "
                   "the entrance is a huddled mass on the ground. Could it be "
                   "Evelyn?"
                   )

    item_list = []
    monster_list = []
    player = None
    adjacent_rooms = {'north': 'entrance_hall'}
    door_map = {'north': False}

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

    feature_list = [door_feature, body_feature, cloak_feature, bag_feature]

    dungeon_entrance = Room(name, description, item_list, monster_list, player,
                            adjacent_rooms, door_map, feature_list)

    return dungeon_entrance


def init_room_2():
    """Instantiates entrance_hall room."""
    name = "entrance_hall"
    description = ("Inside it is dark. A hole in the far left corner of the "
                   "fortress wall casts some moonlight on the far side of the "
                   "room. On the far wall where the moonlight shines there "
                   "appears to be some writing."
                   )

    item_list = []
    monster_list = []
    player = None
    adjacent_rooms = {}
    door_map = {'east': False, 'south': False}

    goblin_graffitii_feature = ("You've seen this type of writing before at "
                                "the entrance to the high mountains near the "
                                "edge of your homeland. This is goblin "
                                "graffiti, used to mark a particular goblin "
                                "clans home."
                                )

    east_door_feature = ("An oak door with a large iron handle.")

    feature_list = [goblin_graffitii_feature, east_door_feature]

    entrance_hall = Room(name, description, item_list, monster_list, player,
                         adjacent_rooms, door_map, feature_list)

    return entrance_hall


def init_room_objects():
    """Creates the starting game objects"""
    room_list = []

    dungeon_entrance = init_room_1()
    entrance_hall = init_room_2()

    room_list.extend((dungeon_entrance, entrance_hall))

    return room_list


def init_player_object(player_name):
    """Instantiates the inital Player object."""
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
    """Serializes starting game state into game files."""
    room_list = []

    room_list = init_room_objects()

    for room in room_list:
        save_object_state(room)

    player = init_player_object(player_name)
    save_object_state(player)


def load_object(object_name):
    """Load room object from binary file."""
    file_path = Path("game_files/")

    file_name = object_name + '.bin'

    file = file_path / file_name

    binary_file = open(str(file), mode='rb')

    game_object = pickle.load(binary_file)

    return game_object


def save_object_state(game_object):
    """Serialize object into binary file"""
    file_path = Path("game_files/")

    file_name = game_object.get_name() + '.bin'

    file = file_path / file_name

    binary_file = open(str(file), mode='wb')

    pickle.dump(game_object, binary_file)

    binary_file.close()
