class Room:
    """Room class representing primary game map that player navigates.

    Attributes:
        description (tuple(str)): Contains long and short description of room.
            Long description at tuple[0], short description at tuple[1].
        item_list (list(:obj:Item)): List of all Item objects in the room.
        monster_list (list(:obj:Monster)): List of all Monster objects in room.
        player (:obj:Player): Player object used to access player in the room.
            Is None if no player is present.
        adjacent_rooms (dictionary(str, str)): Contains map of directions
            connected to room names that are accessible from current room. For
            example: {'south': 'dungeon_entrance'}.
        door_map (dictionary(str, bool)): Map of doors in room. Takes a
            string ('north', 'east', 'south', 'west') and returns a bool
            representing if the door is locked (True if locked).
        features(dictionary(str, str)): Dictionary contains all of this rooms
            feature names mapped to the text description of that feature.

    """
    def __init__(self, name, description, item_list, monster_list,
                 player, adjacent_rooms, door_map, features):
        self.name = name
        self.description = description
        self.item_list = item_list
        self.monster_list = monster_list
        self.player = player
        self.adjacent_rooms = adjacent_rooms
        self.door_map = door_map
        self.features = features

    def get_description(self):  # need a short and long description based on if
        return self.description[0]  # a player has been in the room before

    def get_short_description(self):
        return self.description[1]

    def get_adjacent_room(self, direction):
        return self.adjacent_rooms[direction]

    def get_door_map(self):
        return self.door_map

    def get_monsters(self):
        return self.monster_list

    def get_items(self):
        return self.item_list

    def get_features(self):
        return self.features

    def remove_feature(self, feature):
        if feature in self.features:
            del self.features[feature]

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
    """Character class parent to Monster and Player classes.

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
    def __init__(self, name, health, magic, level, magic_defense, magic_power,
                 defense, attack_power):
        self.name = name
        self.health = health
        self.magic = magic
        self.level = level
        self.magic_defense = magic_defense
        self.magic_power = magic_power
        self.defense = defense
        self.attack_power = attack_power

    def get_name(self):
        return self.name

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
    """Player class tracks the state of the user conrolled Character.

    Attributes:
        experience (int): Tracks points until next level.
        memory (list(str)): Tracks both features and items that a character
            has inspected.
        backpack (list(:obj:Item)): Tracks items that the character is
            carrying.
        equipped_item (:obj:Item): Tracks item that the character is using.

    """
    def __init__(self, name, health, magic, level, magic_defense, magic_power,
                 defense, attack_power, num_lives, experience, memory,
                 backpack, equipped_item, rescue_evelyn=False):
        super().__init__(name, health, magic, level, magic_defense,
                         magic_power, defense, attack_power)
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
        if thing in self.memory:
            return True
        else:
            return False

    def add_memory(self, thing):
        if thing not in self.memory:
            self.memory.append(thing)

    def drop_item(self, item):
        if self.equipped_item is not None and self.equipped_item == item:
            self.unequip_item()

        if item in self.backpack:
            self.backpack.remove(item)

    def add_item(self, item):
        self.backpack.append(item)

    def unequip_item(self):
        item = self.equipped_item

        if item is not None:
            stat_list = item.get_stats()

            for stat in stat_list:
                if stat == 'health':
                    self.set_health(self.get_health() - stat_list['health'])
                if stat == 'magic':
                    self.set_magic(self.get_magic() - stat_list['magic'])
                if stat == 'level':
                    self.set_level(self.get_level() - stat_list['level'])
                if stat == 'magic_defense':
                    self.set_magic_defense(self.get_magic_defense() -
                                           stat_list['magic_defense'])
                if stat == 'magic_power':
                    self.set_magic_power(self.get_magic_power() -
                                         stat_list['magic_power'])
                if stat == 'defense':
                    self.set_defense(self.get_defense() - stat_list['defense'])
                if stat == 'attack_power':
                    self.set_attack_power(self.get_attack_power() -
                                          stat_list['attack_power'])

            self.add_item(item)
            self.equipped_item = None

    def equip_item(self, item):
        if item in self.backpack:
            if self.equipped_item is not None:
                self.unequip_item()

            stat_list = item.get_stats()

            for stat in stat_list:
                if stat == 'health':
                    self.set_health(self.get_health() + stat_list['health'])
                if stat == 'magic':
                    self.set_magic(self.get_magic() + stat_list['magic'])
                if stat == 'level':
                    self.set_level(self.get_level() + stat_list['level'])
                if stat == 'magic_defense':
                    self.set_magic_defense(self.get_magic_defense() +
                                           stat_list['magic_defense'])
                if stat == 'magic_power':
                    self.set_magic_power(self.get_magic_power() +
                                         stat_list['magic_power'])
                if stat == 'defense':
                    self.set_defense(self.get_defense() + stat_list['defense'])
                if stat == 'attack_power':
                    self.set_attack_power(self.get_attack_power() +
                                          stat_list['attack_power'])

            self.equipped_item = item
            self.backpack.remove(item)

    def get_equipped_item(self):
        return self.equipped_item

    def use_item(self, item):
        if self.equipped_item is not None and self.equipped_item == item:

            if self.equipped_item.get_durability() is not None:
                self.equipped_item.decrement_durability()
                if self.equipped_item.get_durability() == 0:
                    self.equipped_item = None

            return self.equipped_item
        else:
            print("That item is not equipped.")

    def get_lives(self):
        return self.num_lives

    def lose_life(self):
        self.num_lives -= 1

    def inspect(self, thing):
        if not self.has_memory(thing):
            self.add_memory(thing)

    def get_inventory(self):
        return self.backpack

    def level_up(self):
        self.level += 1
        self.health += 10
        self.magic += 10
        self.magic_defense += 1
        self.magic_power += 1
        self.defense += 1
        self.attack_power += 1

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class Item():
    """Item class tracks the state of items used by the player.

    Attributes:
        name (str): Name that the item is called.
        description (str): Description of the characteristics of the item.
        stats (dictionary(str, int)): Stats that item boosts.

    """
    def __init__(self, name, description, durability, stats):
        self.name = name
        self.description = description
        self.durability = durability
        self.stats = stats

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_durability(self):
        return self.durability

    def decrement_durability(self):
        if self.durability is not None:
            self.durability -= 1

    def get_stats(self):
        return self.stats

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
