from game_classes import *
from file_manager import *


def main():
    init_game_files()
    current_room = load_room("dungeon_entrance")

    print(current_room.get_name())


if __name__ == "__main__":
    main()
