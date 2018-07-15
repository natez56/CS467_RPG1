class Room:
    """
    Room class representing primary game map that player navigates.

    Attributes:
        description (string): Message printed to player.
        item_list (list(Item)): List of all Item objects in the room.
        monster_list (list(Monster)): List of all Monster objects in room.
        player (Player): Player object used to access player in the room. Is
            None if no player is present.
        adjacent_rooms (dictionary(string, string)): Contains map of directions
            connected to room names that are accessible from current room. For
            example: <'south', 'dungeon_entrance'>
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

    def get_adjacent_room(self, direction):
        return self.adjacent_rooms[direction]

    def get_door_map(self):
        return self.door_map

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

    def set_player(self, player):
        self.player = player

    def is_locked(self, door):
        return self.door_map[door]

    def unlock(self, door):
        self.door_map[door] = False

    def get_name(self):
        return self.name


class Character:
    """
    Character class parent to Monster and Player classes.

    Attributes:
        health (int): Character dies when this reaches zero.
        magic (int): Using spells drains this attribute.
        level (int): Relative measure of toughness (the combination of all
            offensive and defensive stats and abilities).
        magic_defense (int): Reduces magic damage.
        magic_power (int): Increases magic damage.
        defense (int): Reduces physical damage.
        attack_power (int): Increases physical damage.
    """
    def __init__(self, health, magic, level, magic_defense, magic_power,
                 defense, attack_power):
        self.health = health
        self.magic = magic
        self.level = level
        self.magic_defense = magic_defense
        self.magic_power = magic_power
        self.defense = defense
        self.attack_power = attack_power

    def get_health(self):
        return self.health

    def set_health(self, health):
        self.health = health

    def get_magic(self):
        return self.magic

    def set_magic(self, magic):
        self.magic = magic

    def get_level(self):
        return self.level

    def set_level(self, level):
        self.level = level

    def get_magic_defense(self):
        return self.magic_defense

    def set_magic_defense(self, magic_defense):
        self.magic_defense = magic_defense

    def get_magic_power(self):
        return self.magic_power

    def set_magic_power(self, magic_power):
        self.magic_power = magic_power

    def get_defense(self):
        return self.defense

    def set_defense(self, defense):
        self.defense = defense

    def get_attack_power(self):
        return self.attack_power

    def set_attack_power(self, attack_power):
        self.attack_power = attack_power


class Player(Character):
    """
    Player class tracks the state of the user conrolled Character.

    Attributes:
        experience (int): Tracks points until next level.
        memory (list(string)): Tracks both features and items that a character
            has inspected.
        backpack (list(item)): Tracks items that the character is carrying.
        equipped_item (item): Tracks item that the character is using.
    """
    def __init__(self, health, magic, level, magic_defense, magic_power,
                 defense, attack_power, num_lives, experience, memory,
                 backpack, equipped_item, rescue_evelyn=False):
        super().__init__(health, magic, level, magic_defense, magic_power,
                         defense, attack_power)
        self.num_lives = num_lives
        self.experience = experience
        self.memory = memory
        self.backpack = backpack
        self.equipped_item = equipped_item
        self.rescue_evelyn = False

    def get_experience(self):
        return self.experience

    def set_experience(self, experience):
        self.experience = experience

    def has_memory(self, thing):
        if thing in memory:
            return True
        else:
            return False

    def add_memory(self, thing):
        if thing not in memory:
            memory.append(thing)

    def drop_item(self, item):
        if item in backpack:
            backpack.remove(item)

    def add_item(self, item):
        self.backpack.append(item)

    def equip_item(self, item):
        if item in self.backpack:
            self.equipped_item = item

    def get_equipped_item(self):
        return self.equipped_item

    def get_name(self):
        return "player"

    def get_lives(self):
        return self.num_lives

    def lose_life(self):
        self.num_lives -= 1

    def use_door(self, door):
        # TODO travel(door)
        pass

    def inspect(self, thing):
        if not self.has_memory(thing):
            self.add_memory(thing)

    def level_up(self):
        self.level += 1
        self.health += 10
        self.magic += 10
        self.magic_defense += 1
        self.magic_power += 1
        self.defense += 1
        self.attack_power += 1
        self.experience = 0
