from file_manager import *
from feature_handler import *


def general_item_handler(current_room, verb, item_name):
    """Handle any non-unique verb and item interactions.

    Args:
        current_room (:obj:Room): The current room that the player is in.
        verb (str): The action a user would like to take.
        item_name (str): The name of the item the user would like to use.

    """
    player = current_room.get_player()

    # For each verb handler player and item or room and item interaction.
    if verb == "take":
        if item_name not in player.get_item_names():
            item = current_room.get_item(item_name)

            player.add_item(item)

            # When item is added to player it must be removed from the room.
            current_room.remove_item(item)
        else:
            print("That item is already in your inventory.")

    # Player can look at an item whether it is in inventory on in the room.
    elif verb == "look at":
        if item_name in current_room.get_item_names():
            print(current_room.get_item(item_name).get_description())
        else:
            print(player.get_item(item_name).get_description())

    elif verb == "drop":
        if item_name in player.get_item_names():
            item = player.drop_item(item_name)

            # When an item is dropped by the player it must be added to the
            # current room.
            current_room.add_item(item)
        else:
            print("You're not carrying that item currently.")

    elif verb == "use":
        if item_name == "bread" and "bread" in player.get_item_names():
            player.use_item("bread")
            print("You scarf down the bread. It's delicious. You feel "
                  "healthier as a result")

        elif item_name not in player.get_item_names():
            print("You're not carrying that item currently.")

        else:
            print("You can't use that here")

    save_object_state(current_room)


def room_1_item_handler(current_room, verb, item_name):
    """Handle room 1 player and item and room and item interactions.

    Args:
        current_room (:obj:Room): The current room the player is in.
        verb (str): The action the user would like to take.
        item_name: The name of the item the user would like to use.

    """
    player = current_room.get_player()

    # Custom item handlers
    if (verb == "use" and item_name == "sword" and
       "sword" in player.get_item_names()):
            print("You start swinging your sword around like a lunatic. If "
                  "anyone was around to see you I'm sure they'd be terrified.")

    # These verbs do not need unique room interactions.
    else:
        general_item_handler(current_room, verb, item_name)

    save_object_state(current_room)


def room_2_item_handler(current_room, verb, item_name):
    """Handles room 2 player item or room item interactions.

    Args:
    current_room (:obj:Room): The current room that the player is in.
    verb (str): The action a user would like to take.
    item_name (str): The name of the item the user would like to use.

    """
    player = current_room.get_player()

    # Triggers rope trap if trap hasn't already been triggered.
    if (verb == "look at" and item_name == "key" and
            (current_room.get_puzzle_status("rope") or
             "rope" in current_room.get_features())):

            print("The golden key glitters on the floor among the rubble. "
                  "You walk forward to take a closer look.")

            rope_trap(current_room)

    # Triggers rope trap if trap hasn't already been triggered.
    elif (verb == "take" and item_name == "key" and
            (current_room.get_puzzle_status("rope") or
             "rope" in current_room.get_features())):

            print("The golden key glitters on the floor among the rubble. "
                  "You walk forward to pick up the key.")

            rope_trap(current_room)

    # Verb use uniquely interacts with this rooms features.
    # After a user inspects the rubble in the room, the rope feature is
    # added.  Then, if a player uses the sword, it will disable the rope
    # trap and remove it as a feature from the room.
    elif (verb == "use" and item_name == "sword" and
          "sword" in player.get_item_names()):
            if "rope" in current_room.get_features():
                print("You kneel down and cut the rope. As soon as the rope "
                      "is cut you here a click and a crossbow bolt zooms over "
                      "your head. Good thing I saw this trap ahead of time.")

                current_room.remove_feature("rope")

    # These verbs do not get unique handlers for this room.
    else:
        general_item_handler(current_room, verb, item_name)

    save_object_state(current_room)


def room_3_item_handler(current_room, verb, item_name):
    """Handle room 3 player and item and room and item interactions.

    Args:
        current_room (:obj:Room): The current room the player is in.
        verb (str): The action the user would like to take.
        item_name: The name of the item the user would like to use.

    """
    player = current_room.get_player()

    # These verbs do not need unique room interactions.
    general_item_handler(current_room, verb, item_name)

    save_object_state(current_room)


def room_4_item_handler(current_room, verb, item_name):
    """Handle room 4 player and item and room and item interactions.

    Args:
        current_room (:obj:Room): The current room the player is in.
        verb (str): The action the user would like to take.
        item_name: The name of the item the user would like to use.

    """
    player = current_room.get_player()

    # The verb use has custom interactions for each room.
    if (verb == "use" and item_name == "sword" and
        "sword" in player.get_item_names() and
       current_room.get_puzzle_status("vines")):

            print("You hack at the black vines covering the door. For each "
                  "vine you hack off another grows in its place. Better "
                  "find another way to remove them...")

    elif (verb == "use" and item_name == "key" and
          "key" in player.get_item_names() and
          current_room.get_puzzle_status("lock box")):

        print("You use the golden key on the small lock box on the shelf. "
              "Inside you find a letter.")

        letter_name = "letter"
        letter_description = ("The letter is neat and well written, it "
                              "reads: \n"
                              "This note is to remind you fool goblins to "
                              "not turn the newly placed engraved lock on "
                              "the kitchen door in the mess hall. The "
                              "creature inside must remain in the kitchen "
                              "until I can find the time to deal with it "
                              "myself. I will have food shipped from "
                              "elsewhere until the problem is resolved.")
        letter_durability = None
        letter_stats = None

        letter = Item(letter_name, letter_description, letter_durability,
                      letter_stats)
        player.add_item(letter)
        current_room.set_puzzle_status("lock box", False)

    # These verbs do not need unique room interactions.
    else:
        general_item_handler(current_room, verb, item_name)

    save_object_state(current_room)


def room_5_item_handler(current_room, verb, item_name):
    """Handle room 5 player and item and room and item interactions.

    Args:
        current_room (:obj:Room): The current room the player is in.
        verb (str): The action the user would like to take.
        item_name: The name of the item the user would like to use.

    """
    player = current_room.get_player()

    # These verbs do not need unique room interactions.
    general_item_handler(current_room, verb, item_name)

    save_object_state(current_room)
