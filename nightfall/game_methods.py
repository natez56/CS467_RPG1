from game_classes import *
from file_manager import *


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
    else:
        return True