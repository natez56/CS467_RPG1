from game_methods import *
from text_parser import *


def main():
    current_room = start_game()

    player = current_room.get_player()

    print("Initial location: {}".format(current_room.get_name()))

    while not is_game_over(player):
        user_input = get_input()

        action = parse_input(user_input)

        current_room = take_action(current_room, action)

        print("Current room is now: {}".format(current_room.get_name()))


if __name__ == "__main__":
    main()
