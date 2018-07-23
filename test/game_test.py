import pytest
from pathlib import Path
import os
import shutil
from .context import file_manager as fm
from .context import game_classes as gc


class TestGameClasses():
    """Tests all game classes."""
    def test_room_class(self):
        """Test room class."""
        name = "test_room"
        description = ("Testing this room", "shorter description")
        test_item = gc.Item("test item", "test item description", 100, None)
        item_list = []
        item_list.append(test_item)
        monster_list = []
        player = fm.init_player_object("test_player")
        adjacent_rooms = {'north': 'entrance_hall'}
        door_map = {'north': True}
        feature_dict = {"feature": "feature description"}

        room = gc.Room(name, description, item_list, monster_list, player,
                       adjacent_rooms, door_map, feature_dict)

        assert room.get_description() == description[0]
        assert room.get_short_description() == description[1]
        assert room.get_adjacent_room('north') == 'entrance_hall'
        assert room.get_door_map() == door_map
        assert room.get_monsters() == monster_list
        assert room.get_items() == item_list
        assert room.get_features() == feature_dict

        room.remove_feature("feature")

        assert len(room.get_features()) == 0

        new_item = gc.Item("Item 2", "Test Item 2", 50, None)
        room.add_item(new_item)

        assert len(room.get_items()) == 2

        room.remove_item(new_item)

        assert new_item not in room.get_items()
        assert room.get_player() == player

        room.set_player(None)

        assert room.get_player() is None
        assert room.is_locked('north')

        room.unlock('north')

        assert not room.is_locked('north')
        assert room.get_name() == "test_room"

    def test_player_class(self):
        """Test Player class."""
        name = "Test player"
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

        player = gc.Player(name, health, magic, level, magic_defense,
                           magic_power, defense, attack_power, num_lives,
                           experience, memory, backpack, equipped_item)

        stat_dictionary = {"health": 10, "magic": 10}
        test_item = gc.Item("test item", "test item description", 100,
                            stat_dictionary)

        assert player.get_name() == name
        assert player.get_health() == health

        new_health = 50
        player.set_health(new_health)

        assert player.get_health() == new_health
        assert player.get_magic() == magic

        new_magic = 50
        player.set_magic(new_magic)

        assert player.get_magic() == new_magic
        assert player.get_level() == 1

        player.set_level(2)

        assert player.get_level() == 2
        assert player.get_magic_defense() == magic_defense

        player.set_magic_defense(10)

        assert player.get_magic_defense() == 10
        assert player.get_magic_power() == magic_power

        player.set_magic_power(10)

        assert player.get_magic_power() == 10
        assert player.get_defense() == defense

        player.set_defense(10)

        assert player.get_defense() == 10
        assert player.get_attack_power() == attack_power

        player.set_attack_power(10)

        assert player.get_attack_power() == 10
        assert player.get_experience() == 0

        player.set_experience(10)

        assert player.get_experience() == 10

        player.add_memory("feature")

        assert player.has_memory("feature")
        assert not player.has_memory("feature2")

        player.add_item(test_item)
        inventory = player.get_inventory()

        assert inventory[0] == test_item

        player.equip_item(test_item)

        assert player.get_equipped_item() == test_item
        assert player.get_health() == new_health + 10
        assert player.get_magic() == new_magic + 10

        player.use_item(test_item)

        assert player.get_equipped_item().get_durability() == 99

        player.unequip_item()

        assert player.get_equipped_item() is None
        assert player.get_health() == new_health
        assert player.get_magic() == new_magic

        inventory = player.get_inventory()

        assert inventory[0] == test_item

        player.drop_item(test_item)

        inventory = player.get_inventory()

        assert len(inventory) == 0
        assert player.get_equipped_item() is None
        assert player.get_lives() == num_lives

        player.lose_life()

        assert player.get_lives() == num_lives - 1

        player.inspect(test_item.get_name())

        assert player.has_memory(test_item.get_name())

        player.level_up()

        assert player.get_level() == level + 2

    def test_item_class(self):
        """Tests for Item class."""
        name = "test item"
        description = "test item description"
        durability = 100
        stat_dictionary = {"health": 10, "magic": 10}
        test_item = gc.Item(name, description, durability, stat_dictionary)

        assert test_item.get_name() == name
        assert test_item.get_description() == description
        assert test_item.get_durability() == durability

        test_item.decrement_durability()

        assert test_item.get_durability() == durability - 1

        test_dictionary = test_item.get_stats()

        assert test_dictionary == stat_dictionary


# Global objects used in tests.
room = fm.init_room_1()
test_player = fm.init_player_object('Fisky')
room.set_player(test_player)


class TestSaveGame():
    """Tests all file_manager save functions."""
    def test_room_saved(self):
        """Test save_object_state on room."""
        room_name = room.get_name()

        fm.save_object_state(room)

        loaded_room = fm.load_object(room_name)

        assert loaded_room.get_name() == room.get_name()
        assert loaded_room.get_description() == room.get_description()
        assert loaded_room.get_door_map() == room.get_door_map()
        assert loaded_room.get_monsters() == room.get_monsters()
        assert loaded_room.get_features() == room.get_features()

    def test_player_saved(self):
        """Test save_object_state on player."""
        fm.save_object_state(room)

        loaded_room = fm.load_object(room.get_name())

        loaded_player = loaded_room.get_player()

        assert loaded_player.get_name() == test_player.get_name()
        assert loaded_player.get_health() == test_player.get_health()
        assert loaded_player.get_magic() == test_player.get_magic()
        assert loaded_player.get_level() == test_player.get_level()
        assert (loaded_player.get_magic_defense() ==
                test_player.get_magic_defense())
        assert loaded_player.get_magic_power() == test_player.get_magic_power()
        assert loaded_player.get_defense() == test_player.get_defense()
        assert (loaded_player.get_attack_power() ==
                test_player.get_attack_power())

    def test_new_save(self):
        """Test new save file created from save_game call."""
        input_values = ['y', 'testFile', 'y', 'testFile']

        def mock_input(s):
            return input_values.pop(0)

        fm.input = mock_input

        test_player.set_health(1)

        fm.save_game(room)
        fm.save_game(room)
        loaded_room = fm.load_object(room.get_name())
        loaded_player = loaded_room.get_player()

        saved_game_path = str(Path("game_files/saved_games/testFile"))
        saved_game_path_2 = str(Path("game_files/saved_games/testFile(1)"))
        current_game_path = str(Path("game_files/current_game"))
        all_saved_game_path = str(Path("game_files/saved_games"))

        current_game_files = os.listdir(current_game_path)
        saved_game_files = os.listdir(saved_game_path)
        all_saved_dirs = os.listdir(all_saved_game_path)

        assert os.path.exists(saved_game_path)
        assert os.path.exists(saved_game_path_2)
        assert current_game_files == saved_game_files
        assert test_player.get_health() == loaded_player.get_health()

        for dir_name in all_saved_dirs:
            path = str(Path("game_files/saved_games/{}".format(dir_name)))
            shutil.rmtree(path)

    def test_load_save(self):
        input_values = ['y', 'testFile', '1', 'y']

        def mock_input(s):
            return input_values.pop(0)

        fm.input = mock_input

        fm.save_game(room)

        room.set_player(None)

        fm.save_object_state(room)

        fm.load_game()
        loaded_room = fm.get_current_room()

        assert loaded_room.get_player() is not None

        loaded_room_2 = fm.load_object(room.get_name())

        assert loaded_room_2 is not None

        all_saved_game_path = str(Path("game_files/saved_games"))

        all_saved_dirs = os.listdir(all_saved_game_path)

        for dir_name in all_saved_dirs:
            path = str(Path("game_files/saved_games/{}".format(dir_name)))
            shutil.rmtree(path)

    def test_overwrite_save(self):
        """Test overwriting a saved game with a new saved game."""
        input_values = ['y', 'testFile', 'n', 'z', '1', 'y']

        def mock_input(s):
            return input_values.pop(0)

        fm.input = mock_input

        saved_game_path = str(Path("game_files/saved_games/testFile"))
        current_game_path = str(Path("game_files/current_game"))
        all_saved_game_path = str(Path("game_files/saved_games"))

        fm.save_game(room)

        saved_game_files = os.listdir(saved_game_path)

        fm.save_game(room)

        new_files = os.listdir(saved_game_path)
        all_saved_dirs = os.listdir(all_saved_game_path)

        assert len(all_saved_dirs) == 1

        for dir_name in all_saved_dirs:
            path = str(Path("game_files/saved_games/{}".format(dir_name)))
            shutil.rmtree(path)

    def test_get_num_saved_games(self):
        assert fm.get_num_saved_games() == 0
