class Room:
    def __init__(self):
        self.description = description
        self.item_list = []
        self.monster_list = []
        self.player_location = playerLocation
        self.adjacent_rooms = []
        self.door_list = {}
        self.feature_list = {}

    def get_description(self):
        return self.description

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

    def remove_monster(self, monster):
        if monster in self.monster_list:
            self.monster_list.remove(monster)