class Room:
    """
    Room class representing primary game map that player navigates.

    Attributes:
        description (string): Message printed to player.
        item_list (list(Item)): List of all Item objects in the room.
        monster_list (list(Monster)): List of all Monster objects in room.
        player (Player): Player object used to access player in the room. Is
            None if no player is present.
        adjacent_rooms (list[Room]): List of rooms that can be reached from
            this room.
        door_map (dictionary(string, bool)): Map of doors in room. Takes a
            string ('north', 'east', 'south', 'west') and returns a bool
            representing if the door is locked (True if locked)
        feature_list(list(string)): List contains all the text descriptions
            of the rooms features.
    """
    def __init__(self, name, description, item_list, monster_list,
                 player, adjacent_rooms, door_map, feature_list):
        self.name = name
        self.description = description
        self.item_list = item_list
        self.monster_list = monster_list
        self.player = player
        self.adjacent_rooms = adjacent_rooms
        self.door_map = door_map
        self.feature_list = feature_list

    def get_description(self):
        return self.description

    def set_adjacent_room(self, room):
        self.adjacent_rooms.append(room)

    def get_monsters(self):
        return self.monster_list

    def get_items(self):
        return self.item_list

    def get_features(self):
        return self.feature_list

    def add_item(self, item):
        self.item_list.append(item)

    def remove_item(self, item):
        if item in self.item_list:
            self.item_list.remove(item)

    def add_monster(self, monster):
        self.monster_list.append(monster)

    def remove_monster(self, monster):
        if monster in self.monster_list:
            self.monster_list.remove(monster)

    def get_player(self):
        return self.player

    def is_locked(self, door):
        return self.door_map[door]

    def unlock(self, door):
        self.door_map[door] = False

    def get_name(self):
        return self.name
