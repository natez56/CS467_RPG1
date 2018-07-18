import pytest
from pathlib import Path
import os
import shutil
from .context import file_manager as fm

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

        loaded_room = fm.load_game()

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
