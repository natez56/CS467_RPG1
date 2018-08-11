from random import randint
from scroll_print import *


class Room:
    """Room class representing primary game map that player navigates.

    Attributes:
        name (str): The room name. For example, fortress entrance.
        description (tuple(str, str)): Contains long and short description of
            room. Long description at tuple[0], short description at tuple[1].
        item_list (list(:obj:`Item`)): List of all Item objects in the room.
        monster_list (list(:obj:`Monster`)): List of all Monster objects in
            room.
        player (:obj:`Player`): Player object used to access player in the
            room. Is None if no player is present.
        adjacent_rooms (dictionary(str, str)): Contains map of directions
            connected to room names that are accessible from current room. For
            example: {'south': 'fortress entrance'}.
        door_map (dictionary(str, bool)): Map of doors in room. Takes a
            string ('north', 'east', 'south', 'west') and returns a bool
            representing if the door is locked (True if locked).
        features(dictionary(str, str)): Dictionary contains all of this rooms
            feature names mapped to the text description of that feature.
        puzzle_dict(dictionary(str, bool)): Dictionary used to track the state
            of puzzles in a room. True means the puzzle is not solved.

    """
    def __init__(self, name, description, item_list, monster_list,
                 player, adjacent_rooms, door_map, features, puzzle_dict):
        self.name = name
        self.description = description
        self.item_list = item_list
        self.monster_list = monster_list
        self.player = player
        self.adjacent_rooms = adjacent_rooms
        self.door_map = door_map
        self.features = features
        self.puzzle_dict = puzzle_dict

    def set_door_map(self, door_map):
        self.door_map = door_map

    def set_adjacent_rooms(self, adjacent_rooms):
        self.adjacent_rooms = adjacent_rooms

    def get_description(self):
        return self.description[0]

    def get_short_description(self):
        return self.description[1]

    def set_description(self, description):
        self.description = description

    def get_adjacent_room(self, direction):
        return self.adjacent_rooms[direction]

    def get_adjacent_rooms(self):
        return self.adjacent_rooms

    def get_door_map(self):
        return self.door_map

    def get_monsters(self):
        return self.monster_list

    def get_item_list(self):
        return self.item_list

    def get_item_names(self):
        name_list = []

        for item in self.item_list:
            name_list.append(item.get_name())

        return name_list

    def get_item(self, item_name):
        for item in self.item_list:
            if item.get_name() == item_name:
                return item

        return None

    def add_feature(self, feature, feature_description):
        self.features[feature] = feature_description

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

    def get_puzzle_dict(self):
        return self.puzzle_dict

    def get_puzzle_status(self, puzzle_name):
        return self.puzzle_dict[puzzle_name]

    def set_puzzle_status(self, puzzle_name, status):
        self.puzzle_dict[puzzle_name] = status

    def is_locked(self, door):
        return self.door_map[door]

    def unlock(self, door):
        self.door_map[door] = False

    def get_name(self):
        return self.name

    def monster_killed(self):
        self.monster_list = []


class Character:
    """Character class parent to Monster and Player classes.

    Attributes:
        name (str): The name of the character.
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
    """Player class tracks the state of the user controlled Character.

    Attributes:
        experience (int): Tracks points until next level.
        memory (list(str)): Tracks both features and items that a character
            has inspected.
        backpack (list(:obj:`Item`)): Tracks items that the character is
            carrying.
        equipped_item (:obj:`Item`): Tracks item that the character is using.
        rescue_evelyn (bool): Tracks if the game has ended.

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

    def has_memory(self, room_name):
        """Check if user has visited room.

        Args:
            room_name: Room name to check against

        Returns:
            bool: True if room has been visited before, False otherwise.

        """
        if room_name in self.memory:
            return True
        else:
            return False

    def add_memory(self, room_name):
        """Track which room user has visited.

        Args:
            room_name: Name of room being tracked.

        """
        if room_name not in self.memory:
            self.memory.append(room_name)

    def drop_item(self, item_name):
        """Removes item from inventory and returns it.

        Args:
            item_name: Name of item to be removed.

        Returns:
            :obj:`Item`: The item object removed from inventory.

        """
        # Check if item is equipped. Unequip it if it is.
        if (self.equipped_item is not None and
           self.equipped_item.get_name() == item_name):
            self.unequip_item()

        # Remove item and return it.
        for item in self.backpack:
            if item.get_name() == item_name:
                scroll_print("Removed item {} from inventory."
                             .format(item_name))

                self.backpack.remove(item)

                return item

    def add_item(self, item):
        """Add item from room to player inventory."""
        scroll_print("Added {} to your inventory.".format(item.get_name()))

        self.backpack.append(item)

    def unequip_item(self):
        """Unequip current equipped item."""
        item = self.equipped_item

        if item is not None:
            # Remove item stats that were added when item was first equipped.
            stat_list = item.get_stats()

            scroll_print("Unequipped {}".format(item.get_name()))

            # Check the specific item stat list for the presence of stats.
            # Remove stats from player if found.
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

            self.equipped_item = None

    def equip_item(self, item):
        """Equip item that is in player inventory to get stats.

        Args:
            item: The item object to be equipped

        """
        if item in self.backpack and item.get_stats() is not None:
            if self.equipped_item is not None:
                self.unequip_item()

            stat_list = item.get_stats()

            scroll_print("You equipped the {}.\n".format(item.get_name()))

            scroll_print("Stats gained:")

            # Check specific item stat list for stats. For each stat found,
            # add it to the player stats.
            for stat in stat_list:
                if stat == 'health':
                    scroll_print("+{} health".format(stat_list['health']))

                    self.set_health(self.get_health() + stat_list['health'])
                if stat == 'magic':
                    scroll_print("+{} magic".format(stat_list['magic']))

                    self.set_magic(self.get_magic() + stat_list['magic'])
                if stat == 'level':
                    scroll_print("+{} level".format(stat_list['level']))

                    self.set_level(self.get_level() + stat_list['level'])
                if stat == 'magic_defense':
                    scroll_print("+{} magic defense"
                                 .format(stat_list['magic_defense']))

                    self.set_magic_defense(self.get_magic_defense() +
                                           stat_list['magic_defense'])
                if stat == 'magic_power':
                    scroll_print("+{} magic power"
                                 .format(stat_list['magic_power']))

                    self.set_magic_power(self.get_magic_power() +
                                         stat_list['magic_power'])
                if stat == 'defense':
                    scroll_print("+{} defense".format(stat_list['defense']))

                    self.set_defense(self.get_defense() + stat_list['defense'])
                if stat == 'attack_power':
                    scroll_print("+{} attack power"
                                 .format(stat_list['attack_power']))

                    self.set_attack_power(self.get_attack_power() +
                                          stat_list['attack_power'])

            self.equipped_item = item

        else:
            scroll_print("You cannot equip that item.")

    def get_equipped_item(self):
        return self.equipped_item

    def use_item(self, item_name):
        """Simulate using item by removing item durability."""
        if item_name in self.get_item_names():
            item = self.get_item(item_name)

            item.decrement_durability()

            # Item destroyed if durability is 0.
            if item.get_durability() == 0:
                scroll_print("Item {} used and removed from inventory.\n"
                             .format(item_name))

                self.backpack.remove(item)

    def get_lives(self):
        return self.num_lives

    def lose_life(self):
        self.num_lives -= 1

    def inspect(self, thing):
        if not self.has_memory(thing):
            self.add_memory(thing)

    def get_inventory(self):
        return self.backpack

    def get_item(self, item_name):
        for item in self.backpack:
            if item.get_name() == item_name:
                return item

    def get_item_names(self):
        name_list = []

        for item in self.backpack:
            name_list.append(item.get_name())

        return name_list

    def print_stats(self):
        """Prints the players stats."""
        scroll_print("Current Stats")
        scroll_print("Player Name: {}".format(self.name))
        scroll_print("Level: {}".format(self.level))
        scroll_print("Experience: {}".format(self.experience))
        scroll_print("Remaining Lives: {}".format(self.num_lives))
        scroll_print("Health: {}".format(self.health))
        scroll_print("Magic: {}".format(self.magic))
        scroll_print("Attack Power: {}".format(self.attack_power))
        scroll_print("Defense: {}".format(self.defense))
        scroll_print("Magic Power: {}".format(self.magic_power))
        scroll_print("Magic Defense: {}".format(self.magic_defense))

    def revive(self, level):
        """Revive players that lose all their health.

        Args:
            level: The players current level.

        """
        if level == 1:
            self.health = 50
            self.magic = 20

        elif level == 2:
            self.health = 60
            self.magic = 25

        elif level == 3:
            self.health = 70
            self.magic = 30

        elif level == 4:
            self.health = 80
            self.magic = 35

        else:
            self.health = 90
            self.magic = 40

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class Wizard(Player):
    """Wizard class tracks the state of wizard characters.

    Modifies Character attributes.

    """
    def __init__(self, name, health, magic, level, magic_defense, magic_power,
                 defense, attack_power, num_lives, experience, memory,
                 backpack, equipped_item, rescue_evelyn=False):
        magic += 5
        magic_power += 1
        magic_defense += 1

        super().__init__(name, health, magic, level, magic_defense,
                         magic_power, defense, attack_power, num_lives,
                         experience, memory, backpack, equipped_item,
                         rescue_evelyn)

    def get_attack_description(self, level):
        """Prints the attack options the player has given their level.

        Args:
            level: The player's level.

        """
        scroll_print("   Bash: Swing your weapon at the enemy to bludgeon "
                     "them. ")
        scroll_print("   Thunder: Conjure the force of thunder and launch "
                     "it at the enemy. ")
        scroll_print("   Singe: Strike your opponent with a burning aura "
                     "on your primary weapon. ")
        if level > 2:
            scroll_print("   Level 3 attack placeholder. ")
        if level > 4:
            scroll_print("   Level 5 attack placeholder. ")

    def check_invalid_attack(self, attack_choice, level):
        """Checks if the player selected an invalid attack.

        Args:
            attack_choice: The user choice of attack.
            level: The player's level.

        """
        if level > 4:
            if attack_choice != 'bash' and attack_choice != 'thunder' and \
               attack_choice != 'singe' and attack_choice != '4' and \
               attack_choice != '5':

                scroll_print("\nYou entered an invalid choice! ")
                scroll_print("Please enter: Bash, Thunder, Singe, 4, or 5: ")

                return True

        elif level > 2:
            if attack_choice != 'bash' and attack_choice != 'thunder' and \
               attack_choice != 'singe' and attack_choice != '4':

                scroll_print("\nYou entered an invalid choice! ")
                scroll_print("Please enter: Bash, Thunder, Singe, or 4: ")

                return True

        else:
            if attack_choice != 'bash' and attack_choice != 'thunder' and \
               attack_choice != 'singe':

                scroll_print("\nYou entered an invalid choice! ")
                scroll_print("Please enter: Bash, Thunder, or Singe: ")

                return True

        return False

    def execute_attack(self, option):
        """Calculates attack damage for user chosen attack.

        Args:
            option: The user chosen attack.

        Returns:
            int: The player's attack damage that will be done.

        """
        if option == 'bash':
            # Randomize the damage based on the move and applicable equipment
            attack_damage = randint(0, self.attack_power)

            return attack_damage

        elif option == 'thunder':
            if self.magic < 2:
                scroll_print("You don't have enough magic! ")
                attack_damage = 0

            else:
                # Randomize the damage based on the move and
                # applicable equipment
                attack_damage = randint(0, self.magic_power)

                # Adjust the player's stats
                self.magic -= 2

            return attack_damage

        elif option == 'singe':
            if self.magic < 3:
                scroll_print("You don't have enough magic! ")
                attack_damage = 0

            else:
                # Randomize the damage based on the move and
                # applicable equipment
                attack_damage = randint(0, (self.magic_power +
                                        self.attack_power))

                # Adjust the player's stats
                self.magic -= 3

            return attack_damage

    def get_attack_type(self, attack_choice):
        if attack_choice == 'bash':
            return 0
        elif attack_choice == 'thunder':
            return 1
        else:
            return 2

    def level_up(self, new_level):
        """Increase character stats when certain experience reached."""
        self.level += 1
        self.health += 10
        self.magic += 5
        self.magic_defense += 1
        self.magic_power += 1
        self.defense += 1
        self.attack_power += 1

        if new_level == 3:
            scroll_print("%s has learned 4! " % (self.name))

        elif new_level == 5:
            scroll_print("%s has learned 5! " % (self.name))


class Ranger(Player):
    """Wizard class tracks the state of wizard characters.

    Modifies Character attributes.

    """
    def __init__(self, name, health, magic, level, magic_defense, magic_power,
                 defense, attack_power, num_lives, experience, memory,
                 backpack, equipped_item, rescue_evelyn=False):
        health += 5
        attack_power += 1
        defense += 1

        super().__init__(name, health, magic, level, magic_defense,
                         magic_power, defense, attack_power, num_lives,
                         experience, memory, backpack, equipped_item,
                         rescue_evelyn)

    def get_attack_description(self, level):
        """Prints the attack options the player has given their level.

        Args:
            level: The player's level.

        """
        scroll_print("   Slash: Make a large slash with your primary "
                     "weapon. ")
        scroll_print("   Snare: Cast a spell that causes thorny vines "
                     "to burst from the ground and slice the enemy. ")
        scroll_print("   Sharpshot: Conjour three magical arrows and "
                     "shoot them at the enemy. ")
        if level > 2:
            scroll_print("   Level 3 attack placeholder. ")
        if level > 4:
            scroll_print("   Level 5 attack placeholder. ")

    def check_invalid_attack(self, attack_choice, level):
        """Checks if the player selected an invalid attack.

        Args:
            attack_choice: The user choice of attack.
            level: The player's level.

        """
        if level > 4:
            if attack_choice != 'slash' and attack_choice != 'snare' and \
               attack_choice != 'sharpshot' and attack_choice != '4' and \
               attack_choice != '5':
                scroll_print("\nYou entered an invalid choice! ")
                scroll_print("Please enter: Slash, Snare, Sharpshot, "
                             "4 or 5: ")

                return True

        elif level > 2:
            if attack_choice != 'slash' and attack_choice != 'snare' and \
               attack_choice != 'sharpshot' and attack_choice != '4':

                scroll_print("\nYou entered an invalid choice! ")
                scroll_print("Please enter: Slash, Snare, Sharpshot, or "
                             "4: ")

                return True

        else:
            if attack_choice != 'slash' and attack_choice != 'snare' and \
               attack_choice != 'sharpshot':

                scroll_print("\nYou entered an invalid choice! ")
                scroll_print("Please enter: Slash, Snare, or Sharpshot: ")

                return True

        return False

    def execute_attack(self, option):
        """Calculates attack damage for user chosen attack.

        Args:
            option: The user chosen attack.

        Returns:
            int: The player's attack damage that will be done.

        """
        if option == 'slash':
            # Randomize the damage based on the move and applicable equipment
            attack_damage = randint(0, self.attack_power)

            return attack_damage

        elif option == 'snare':
            if self.magic < 2:
                scroll_print("You don't have enough magic! ")
                attack_damage = 0

            else:
                # Randomize the damage based on the move and
                # applicable equipment
                attack_damage = randint(0, self.magic_power)

                # Adjust the player's stats
                self.magic -= 2

            return attack_damage

        elif option == 'sharpshot':
            if self.magic < 3:
                scroll_print("You don't have enough magic! ")
                attack_damage = 0

            else:
                # Randomize the damage based on the move and
                # applicable equipment
                attack_damage = randint(0, (self.magic_power +
                                        self.attack_power))

                # Adjust the player's stats
                self.magic -= 3

            return attack_damage

    def get_attack_type(self, attack_choice):
        if attack_choice == 'slash':
            return 0
        elif attack_choice == 'snare':
            return 1
        else:
            return 2

    def level_up(self, new_level):
        """Increase character stats when certain experience reached."""
        self.level += 1
        self.health += 10
        self.magic += 5
        self.magic_defense += 1
        self.magic_power += 1
        self.defense += 1
        self.attack_power += 1

        if new_level == 3:
            scroll_print("%s has learned 4! " % (self.name))

        elif new_level == 5:
            scroll_print("%s has learned 5! " % (self.name))


class Monster(Character):
    """Monster class tracks the state of monster characters.

    Attributes:
        description (str): The description of the monster.
        loot (int): Integer loot.

    """
    def __init__(self, name, description, loot, health, magic, level,
                 magic_defense, magic_power, defense, attack_power):
        super().__init__(name, health, magic, level, magic_defense,
                         magic_power, defense, attack_power)
        self.name = name
        self.description = description
        self.loot = loot

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_loot(self):
        return self.loot

    def npc_attack(self, attack_type):
        """Calculate the monster attack damage.

        Args:
            attack_type: The monster chosen attack.

        Returns:
            int: The calculated monster attack damage.

        """
        # Randomly select a melee or magic attack.
        if attack_type == 0:
            scroll_print("\n%s swung their weapon at you! " % (self.name))

            # Randomize the damage based on the move and applicable equipment
            attack_damage = randint(0, self.attack_power)

            return attack_damage

        elif attack_type == 1:
            scroll_print("\n%s is casting a spell! " % (self.name))

            if self.magic < 3:
                scroll_print("%s doesn't have enough magic! " % (self.name))
                attack_damage = 0

            else:
                # Randomize the damage based on the move and
                # applicable equipment.
                attack_damage = randint(0, self.magic_power)

                # Adjust the player's stats.
                self.magic -= 3

            return attack_damage


class Item():
    """Item class tracks the state of items used by the player.

    Attributes:
        name (str): Name that the item is called.
        description (str): Description of the characteristics of the item.
        durability (int): The amount of times this item can be used.
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
        """Remove 1 point of item durability."""
        if self.durability is not None:
            self.durability -= 1

    def get_stats(self):
        return self.stats

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
