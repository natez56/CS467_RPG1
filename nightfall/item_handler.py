from file_manager import *
from feature_handler import *
from scroll_print import *


def general_item_handler(current_room, verb, item_name, feature):
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
            scroll_print("That item is already in your inventory.")

    # Player can look at an item whether it is in inventory on in the room.
    elif verb == "look at":
        if item_name in current_room.get_item_names():
            scroll_print(current_room.get_item(item_name).get_description())
        else:
            scroll_print(player.get_item(item_name).get_description())

    elif verb == "drop":
        if item_name in player.get_item_names():
            item = player.drop_item(item_name)

            # When an item is dropped by the player it must be added to the
            # current room.
            current_room.add_item(item)
        else:
            scroll_print("You're not carrying that item currently.")

    elif verb == "eat":
        if item_name == "bread" and "bread" in player.get_item_names():
            player.use_item("bread")
            scroll_print("You scarf down the bread. It's delicious. You feel "
                         "healthier as a result.")

        else:
            scroll_print("You can't eat that.")

    elif verb == "drink":
        if (item_name == "healing potion" and
           "healing potion" in player.get_item_names()):

            player.use_item("healing potion")

            scroll_print("5 health restored!")

            health = player.get_health()

            player.set_health(health + 5)

        else:
            scroll_print("You can't drink that.")

    elif verb == "smell":
        scroll_print("I can't smell that.")

    elif verb == "listen to":
        scroll_print("I can't listen to that.")

    elif verb == "use":
        if feature is not None:
            scroll_print("You can't use your {} on that.".format(item_name))

        elif item_name == "Quackers":
            scroll_print("You squeeze the rubber duck and it squeaks.")

        elif item_name == "bread" and "bread" in player.get_item_names():
            player.use_item("bread")
            scroll_print("You scarf down the bread. It's delicious. You feel "
                         "healthier as a result.")

        elif (item_name == "healing potion" and
              "healing potion" in player.get_item_names()):
            player.use_item("healing potion")

            scroll_print("5 health restored!")

            health = player.get_health()

            player.set_health(health + 5)

        elif item_name not in player.get_item_names():
            scroll_print("You're not carrying that item currently.")

        else:
            scroll_print("You can't use that here.")

    elif verb == "equip":
        item = player.get_item(item_name)

        player.equip_item(item)

    save_object_state(current_room)


def room_1_item_handler(current_room, verb, item_name, feature):
    """Handle room 1 player and item and room and item interactions.

    Args:
        current_room (:obj:Room): The current room the player is in.
        verb (str): The action the user would like to take.
        item_name: The name of the item the user would like to use.

    """
    player = current_room.get_player()

    if (verb == "use" and item_name == "sword" and
       "sword" in player.get_item_names() and feature is None):

        scroll_print("You start swinging your sword around like a "
                     "lunatic. If anyone was around to see you I'm sure "
                     "they'd be terrified.")

    # These verbs do not need unique room interactions.
    else:
        general_item_handler(current_room, verb, item_name, feature)

    save_object_state(current_room)


def room_2_item_handler(current_room, verb, item_name, feature):
    """Handles room 2 player item or room item interactions.

    Args:
    current_room (:obj:Room): The current room that the player is in.
    verb (str): The action a user would like to take.
    item_name (str): The name of the item the user would like to use.

    """
    player = current_room.get_player()

    # Triggers rope trap if trap hasn't already been triggered.
    if (verb == "look at" and item_name == "golden key" and
        (current_room.get_puzzle_status("rope") or
         "rope" in current_room.get_features())):

        scroll_print("The golden key glitters on the floor among the "
                     "rubble. You walk forward to take a closer look.")

        rope_trap(current_room)

    # Triggers rope trap if trap hasn't already been triggered.
    elif (verb == "take" and item_name == "golden key" and
          (current_room.get_puzzle_status("rope") or
            "rope" in current_room.get_features())):

        scroll_print("The golden key glitters on the floor among the "
                     "rubble. You walk forward to pick up the key.")

        rope_trap(current_room)

    # Verb use uniquely interacts with this rooms features.
    # After a user inspects the rubble in the room, the rope feature is
    # added.  Then, if a player uses the sword, it will disable the rope
    # trap and remove it as a feature from the room.
    elif (verb == "use" and item_name == "sword" and
          "sword" in player.get_item_names() and
          (feature is None or feature == "rope")):

        if "rope" in current_room.get_features():
            scroll_print("You kneel down and cut the rope. As soon as the "
                         "rope is cut you here a click and a crossbow "
                         "bolt zooms over your head. Good thing I saw "
                         "this trap ahead of time.")

            current_room.remove_feature("rope")

    # These verbs do not get unique handlers for this room.
    else:
        general_item_handler(current_room, verb, item_name, feature)

    save_object_state(current_room)


def room_3_item_handler(current_room, verb, item_name, feature):
    """Handle room 3 player and item and room and item interactions.

    Args:
        current_room (:obj:Room): The current room the player is in.
        verb (str): The action the user would like to take.
        item_name: The name of the item the user would like to use.

    """
    player = current_room.get_player()

    # These verbs do not need unique room interactions.
    general_item_handler(current_room, verb, item_name, feature)

    save_object_state(current_room)


def room_4_item_handler(current_room, verb, item_name, feature):
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

        scroll_print("You hack at the black vines covering the door. For "
                     "each vine you hack off another grows in its place. "
                     "Better find another way to remove them...")

    elif (verb == "use" and item_name == "golden key" and
          "golden key" in player.get_item_names() and
          current_room.get_puzzle_status("lock box")):

        scroll_print("You use the golden key on the small lock box on the "
                     "shelf. Inside you find a letter.")

        player.use_item("golden key")

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

    elif (verb == "use" and item_name == "acidic ooze" and
          "acidic ooze" in player.get_item_names() and
          current_room.get_puzzle_status("vines")):

        current_room.set_puzzle_status("vines", False)

        player.use_item("acidic ooze")

        scroll_print("You poor the jar of acidic ooze onto the vines covering "
                     "the door. The vines emit a shrieking sound and quickly "
                     "shrink away from the door. You should now be able to "
                     "pass through to the steel door going north.")

        description = ("The room you are in has large shelves that go from "
                       "floor ceiling. There is a stone area for "
                       "refrigeration where animal carcasses hang from the "
                       "ceiling. Nearby a broom leans against the wall. To "
                       "the west a large oak door leads to the mess hall. To "
                       "the north a steel door.",
                       "I'm in the store room. To the west a large oak door "
                       "leads to the mess hall and to the north a steel door."
                       )

        current_room.set_description(description)

        current_room.unlock('north')

    # These verbs do not need unique room interactions.
    else:
        general_item_handler(current_room, verb, item_name, feature)

    save_object_state(current_room)


def room_5_item_handler(current_room, verb, item_name, feature):
    """Handle room 5 player and item and room and item interactions.

    Args:
        current_room (:obj:Room): The current room the player is in.
        verb (str): The action the user would like to take.
        item_name: The name of the item the user would like to use.

    """
    player = current_room.get_player()

    if (verb == "use" and item_name == "jar" and
        "jar" in player.get_item_names() and
       "acidic ooze" in current_room.get_item_names()):
        scroll_print("You use the jar to grab some of the ooze.")
        player.use_item("jar")
        ooze = current_room.get_item("acidic ooze")
        current_room.remove_item(ooze)
        current_room.set_puzzle_status("ooze", False)

        jar_name = "acidic ooze"
        jar_description = ("The jar is doing a good job of holding the "
                           "ooze.")
        jar_durability = 1
        jar_stats = None

        jar = Item(jar_name, jar_description, jar_durability, jar_stats)

        player.add_item(jar)

    elif (verb == "take" and item_name == "acidic ooze" and
          current_room.get_puzzle_status("ooze")):
        scroll_print("You reach out to grab some of the ooze. When you touch "
                     "it you feel a sharp burning sensation. Ouch! You "
                     "quickly run to the sink to wash your hand off. I better "
                     "find a better way to carry this ooze.")

    # These verbs do not need unique room interactions.
    else:
        general_item_handler(current_room, verb, item_name, feature)

    save_object_state(current_room)


def room_6_item_handler(current_room, verb, item_name, feature):
    """Handle room 6 player and item and room and item interactions.

    Args:
        current_room (:obj:Room): The current room the player is in.
        verb (str): The action the user would like to take.
        item_name: The name of the item the user would like to use.

    """
    player = current_room.get_player()

    # These verbs do not need unique room interactions.
    general_item_handler(current_room, verb, item_name, feature)

    save_object_state(current_room)


def room_7_item_handler(current_room, verb, item_name, feature):
    """Handle room 7 player and item and room and item interactions.

    Args:
        current_room (:obj:Room): The current room the player is in.
        verb (str): The action the user would like to take.
        item_name: The name of the item the user would like to use.

    """
    player = current_room.get_player()

    if (verb == "use" and item_name == "Quackers" and
        "Quackers" in player.get_item_names() and
       current_room.get_puzzle_status("smoke")):
        scroll_print("You place the rubber duck on the table next to the "
                     "smoke figure. It dances around the duck happily. After "
                     "a few moments of frolicking around, the smoke figure "
                     "motions you to follow it toward the humador. The figure "
                     "floats up and points to a small gap betwen the back of "
                     "the humidor and the wall. You reach behind the humador "
                     "and find an emerald key hanging from a small hook. The "
                     "smoke figure waves and then promptly disappears.")

        ash_feature = ("The ash embers have cooled. You walk towards the ash "
                       "tray and just when you are about to touch it, the ash "
                       "from the ash tray spreads out towards the edges of "
                       "the tray. It slowly regathers in the middle and "
                       "spells out \"LEAVE NOW\""
                       )

        current_room.remove_feature("ash tray")
        current_room.remove_feature("smoke")

        current_room.add_feature("ash tray", ash_feature)

        key_name = "emerald key"
        key_description = ("A key with a large emerald embedded in it. ")
        key_durability = 1
        key_stats = None

        key = Item(key_name, key_description, key_durability, key_stats)

        player.add_item(key)

        duck = player.drop_item("Quackers")

        current_room.add_item(duck)

    # These verbs do not need unique room interactions.
    else:
        general_item_handler(current_room, verb, item_name, feature)

    save_object_state(current_room)


def room_8_item_handler(current_room, verb, item_name, feature):
    """Handle room 8 player and item and room and item interactions.

    Args:
        current_room (:obj:Room): The current room the player is in.
        verb (str): The action the user would like to take.
        item_name: The name of the item the user would like to use.

    """
    player = current_room.get_player()

    if (verb == "use" and item_name == "emerald key" and
        "emerald key" in player.get_item_names() and
       current_room.get_puzzle_status("nightstand")):

        current_room.set_puzzle_status("nightstand", False)

        scroll_print("You use the emerald key on the lock box and it opens. "
                     "Inside is a healing potion.")

        healing_potion_name = "healing potion"
        healing_potion_description = ("A glass vial of thick red liquid. ")
        healing_potion_durability = 1
        healing_potion_stats = {"health": 5}

        healing_potion = Item(healing_potion_name, healing_potion_description,
                              healing_potion_durability, healing_potion_stats)

        player.use_item("emerald key")
        player.add_item(healing_potion)

    # These verbs do not need unique room interactions.
    else:
        general_item_handler(current_room, verb, item_name, feature)

    save_object_state(current_room)


def room_9_item_handler(current_room, verb, item_name, feature):
    """Handle room 9 player and item and room and item interactions.

    Args:
        current_room (:obj:Room): The current room the player is in.
        verb (str): The action the user would like to take.
        item_name: The name of the item the user would like to use.

    """
    player = current_room.get_player()

    # These verbs do not need unique room interactions.
    general_item_handler(current_room, verb, item_name, feature)

    save_object_state(current_room)


def room_10_item_handler(current_room, verb, item_name, feature):
    """Handle room 10 player and item and room and item interactions.

    Args:
        current_room (:obj:Room): The current room the player is in.
        verb (str): The action the user would like to take.
        item_name: The name of the item the user would like to use.

    """
    player = current_room.get_player()

    # These verbs do not need unique room interactions.
    general_item_handler(current_room, verb, item_name, feature)

    save_object_state(current_room)


def room_11_item_handler(current_room, verb, item_name, feature):
    """Handle room 10 player and item and room and item interactions.

    Args:
        current_room (:obj:Room): The current room the player is in.
        verb (str): The action the user would like to take.
        item_name: The name of the item the user would like to use.

    """
    player = current_room.get_player()

    if (verb == "use" and item_name == "scrap" and
       "scrap" in player.get_item_names()):

        scroll_print("You place the painting scrap on the area of the "
                     "painting that was torn away. The scrap magically "
                     "stitches to the painting. You hear a ghostly voice "
                     "say, \"Thank you for restoring me to my rightful place, "
                     "in doing so you have freed the portion of my soul that "
                     "the warlock Zlor had trapped here many years ago. As "
                     "thanks take my blessing, it will aid you in your "
                     "fight.\" As the voice fades you feel your strength "
                     "increase. +1 has been added to you attack power.")

        attack_power = player.get_attack_power()

        player.set_attack_power(attack_power + 1)

    # These verbs do not need unique room interactions.
    else:
        general_item_handler(current_room, verb, item_name, feature)

    save_object_state(current_room)


def room_12_item_handler(current_room, verb, item_name, feture):
    """Handle room 10 player and item and room and item interactions.

    Args:
        current_room (:obj:Room): The current room the player is in.
        verb (str): The action the user would like to take.
        item_name: The name of the item the user would like to use.

    """
    player = current_room.get_player()

    if (verb == "use" and item_name == "charcoal" and
       "charcoal" in player.get_item_names()):
        player.use_item("charcoal")

        scroll_print("You throw the charcoal into the fire. There is a green "
                     "flash of light. Ash floats up from the fire and forms "
                     "into a small scrap of paper. You see that it is a "
                     "torn piece of a painting. A face is on the paper.")

        scrap_name = "scrap"
        scrap_description = ("A torn piece of a painting. You can make out a "
                             "face on the canvas scrap.")
        scrap_durability = 1
        scrap_stats = None

        scrap = Item(scrap_name, scrap_description, scrap_durability,
                     scrap_stats)
        player.add_item(scrap)

    # These verbs do not need unique room interactions.
    else:
        general_item_handler(current_room, verb, item_name, feature)

    save_object_state(current_room)


def room_13_item_handler(current_room, verb, item_name, feature):
    """Handle room 10 player and item and room and item interactions.

    Args:
        current_room (:obj:Room): The current room the player is in.
        verb (str): The action the user would like to take.
        item_name: The name of the item the user would like to use.

    """
    player = current_room.get_player()

    # These verbs do not need unique room interactions.
    general_item_handler(current_room, verb, item_name, feature)

    save_object_state(current_room)


def room_14_item_handler(current_room, verb, item_name, feature):
    """Handle room 10 player and item and room and item interactions.

    Args:
        current_room (:obj:Room): The current room the player is in.
        verb (str): The action the user would like to take.
        item_name: The name of the item the user would like to use.

    """
    player = current_room.get_player()

    if (verb == "use" and item_name == "skull key" and
       item_name in player.get_item_names()):

        player.use_item("skull key")
        scroll_print("The door to the final lair is now open")

        current_room.unlock("north")

    elif (verb == "use" and item_name == "iron key" and
          item_name in player.get_item_names() and
          current_room.get_puzzle_status("cage")):
        player.use_item("iron key")

        scroll_print("The cage door opens and the fairy flies out. \"Oh thank "
                     "you, thank you, thank you!!! You've saved me! Oh how "
                     "can I ever repay you. Oh yah! Almost forgot, let me see "
                     "if I can get the key to the final lair for you.\"")
        scroll_print("There is a flash of light and the fairy disappears. A "
                     "couple of seconds pass and there is another blinding "
                     "flash. The fairy has reappeared. \"Phew, that was "
                     "close. I was able to flash into the warlock's room and "
                     "take this without him noticing! Here take it, it is the "
                     "key to the final lair. Oh and one more thing before I "
                     "go, let me give you my blessing. It will aid in your "
                     "final fight.\" The fairy glows brighter for a second "
                     "and then disappears. You feel a warm glow about you. "
                     "Your health returns to full.")

        key_name = "skull key"
        key_description = ("The key has a skull on it. ")
        key_durability = 1
        key_stats = None

        skull_key = Item(key_name, key_description, key_durability, key_stats)
        player.add_item(skull_key)
        current_room.set_puzzle_status("cage", False)
        current_room.remove_feature("fairy")

    # These verbs do not need unique room interactions.
    else:
        general_item_handler(current_room, verb, item_name, feature)

    save_object_state(current_room)


def room_15_item_handler(current_room, verb, item_name, feature):
    """Handle room 10 player and item and room and item interactions.

    Args:
        current_room (:obj:Room): The current room the player is in.
        verb (str): The action the user would like to take.
        item_name: The name of the item the user would like to use.

    """
    player = current_room.get_player()

    # These verbs do not need unique room interactions.
    general_item_handler(current_room, verb, item_name, feature)

    save_object_state(current_room)
