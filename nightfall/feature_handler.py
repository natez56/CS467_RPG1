from file_manager import *
from scroll_print import *


def room_1_feature_handler(current_room, verb, feature):
    """Handles verb commands related to room 1, fortress entrance, features.

    Puzzles:
        None

    Room Items:
        - sword: +1 attack power.

    Features:
        - door
        - body
        - cloak
        - bag

    Monsters:
        None

    Args:
        current_room (:obj:`Room`): The current room the player is in.
        verb (str): The action the user would like to take.
        feature (str): The feature in this room the user would like to act on.

    """

    # Dictionary of feature name mapped to a description of that feature.
    feature_dict = current_room.get_features()

    # Handle feature interaction for each of the 10 main verbs.
    if verb == "take":
        if feature == "body":
            scroll_print("This body is too heavy to carry.")

        elif feature == "cloak":
            scroll_print("The cloak is in tatters. Better to leave it.")

        elif feature == "bag":
            scroll_print("This bag has holes in it. Better to leave it.")

        elif feature == "door":
            scroll_print("Hmm let's see, if you unbolt the doors and go get "
                         "about 10 other villagers to help you carry them... "
                         "on second thought, maybe you should leave the doors "
                         "where they are.")

        else:
            scroll_print("You can't take that.")

    elif verb == "use":
        scroll_print("You can't use that. Better move on or find something "
                     "you can use.")

    elif verb == "drop":
        scroll_print("Drop what? You're not carrying that.")

    elif verb == "look at":
        scroll_print("You take a close look at the {}.".format(feature))

        scroll_print(feature_dict[feature])

    elif verb == "eat":
        if feature == "body":
            scroll_print("Eat this? I don't think so. You're not a zombie.")

        elif feature == "door":
            scroll_print("You gnaw on the oak doors a bit. Yup, that's oak "
                         "alright...")

        elif feature == "cloak":
            scroll_print("You chew on the old cloak a bit and think to "
                         "yourself, \"I better start coming up with some "
                         "reasonable things to do or I'll never rescue "
                         "Evelyn.\"")

        elif feature == "bag":
            scroll_print("You chew on the old bag a bit and think to "
                         "yourself, \"I better start coming up with some "
                         "reasonable things to do or I'll never rescue "
                         "Evelyn.\"")

        else:
            scroll_print("You can't eat that.")

    elif verb == "drink":
        scroll_print("You can't drink that.")

    elif verb == "smell":
        if feature == "door":
            scroll_print("Smells like oak.")

        else:
            scroll_print("The smell is foul. This has been here a while.")

    elif verb == "listen to":
        scroll_print("The only sound you can hear is the wind rustling the "
                     "leaves of the nearby trees.")

    elif verb == "climb":
        if feature == "body":
            scroll_print("Better to not disturb the dead by climbing on them.")

        else:
            scroll_print("You can't climb that.")

    elif verb == "duck":
        scroll_print("You duck quickly and then stand back up.")

    elif verb == "rotate":
        if feature == "body":
            scroll_print("You move the body so that it is facing the other "
                         "way.")

        elif feature == "cloak":
            scroll_print("You pick the cloak up, turn it around, and set it "
                         "back down.")

        elif feature == "bag":
            scroll_print("You pick the bag up, turn it around, and set it "
                         "back down.")

        else:
            scroll_print("You can't rotate that.")

    elif verb == "equip":
        scroll_print("You can't do that.")

    save_object_state(current_room)


def room_2_feature_handler(current_room, verb, feature):
    """Handle room 2, entrance hall, player and feature interaction.

    Puzzles:
        1. rope:
            Trigger: When a player looks at or trys to take the golden
            key in the room. Also triggers when the player tries to travel to
            the next room.

            Disable: Player must look at rubble before triggering the trap.
            Then they must type 'use sword' or 'use sword on rope' to disable
            the trap. If the trap is triggered before the sword is used, a
            player must type 'duck' to avoid the trap.

    Room Items:
        - golden key: Opens lock box in room 4 store room.

    Features:
        - rubble
        - door
        - writing
        - rope: Appears once the player looks at rubble or triggers the rope. \
        puzzle. Disappears once rope trap is disabled.

    Monsters:
        - Skrag, goblin.

    Args:
        current_room (:obj:`Room`): The current room the player is in.
        verb (str): The action the user would like to take.
        feature (str): The feature in this room the user would like to act on.

    """
    # A dictionary that maps feature name to a description of that feature.
    feature_dict = current_room.get_features()

    # Handle custom feature interaction for each of the 10 core verbs.
    if verb == "take":
        if feature == "rubble":
            scroll_print("The pieces of rubble are too heavy to carry.")

        elif feature == "door":
            scroll_print("Hmm let's see, if you unbolt the doors and go get "
                         "about 10 other villagers to help me carry them...on "
                         "second thought maybe you should leave the doors "
                         "where they are.")

        else:
            scroll_print("You can't take that.")

    elif verb == "use":
        scroll_print("You can't use that. Better move on or find something "
                     "you can use.")

    elif verb == "drop":
        scroll_print("Drop what? You're not carrying that.")

    elif verb == "look at":
        # Trigger to add rope to feature list. The command use sword will
        # eliminate the rope trap after the feature is discovered.
        if feature == "rubble":
            scroll_print("You take a close look at the {}.".format(feature))

            scroll_print(feature_dict[feature])

            # Add the rope feature so that it can be acted upon by the user.
            if current_room.get_puzzle_status("rope"):
                rope_feature = ("The rope is taut and looks as though it is "
                                "meant to trip someone walking toward the "
                                "inner door.")

                current_room.add_feature("rope", rope_feature)

                # The rope puzzle has been triggered and should now be set to
                # false. This tracks puzzle status.
                current_room.set_puzzle_status("rope", False)

        elif feature == "rope":
            scroll_print("You take a close look at the {}.".format(feature))

            scroll_print(feature_dict[feature])

        # If the user has not entered: use sword after the rope feature has
        # been added to the room, then going to inspect the writing triggers
        # a trap that will damage them.
        elif feature == "writing":
            if (current_room.get_puzzle_status("rope") or
               "rope" in current_room.get_features()):

                scroll_print("You walk toward the door to inspect the "
                             "writing.")

                rope_trap(current_room)

            # If the trap has already been triggered then the player can
            # inspect the writing as normal.
            else:
                scroll_print("You take a close look at the {}".format(feature))

                scroll_print(feature_dict[feature])

        else:
            scroll_print("You take a close look at the {}.".format(feature))

            scroll_print(feature_dict[feature])

    elif verb == "eat":
        if feature == "rubble":
            scroll_print("You take a bite of some rubble and break a tooth. "
                         "Ouch!")

        elif feature == "door":
            scroll_print("You gnaw on the oak doors a bit. Yup, that's oak "
                         "alright...")

        elif feature == "writing":
            scroll_print("You can't eat writing, that's silly.")

        elif feature == "rope":
            scroll_print("You gnaw on the rope a bit. Tastes like rope...")

        else:
            scroll_print("You can't eat that.")

    elif verb == "drink":
        scroll_print("You can't drink that.")

    elif verb == "smell":
        if feature == "door":
            scroll_print("Smells like oak.")

        elif feature == "writing":
            scroll_print("The writing smells foul.")

        elif feature == "rubble":
            scroll_print("Ahh nothing like the smell of some good rubble.")

        elif feature == "rope":
            scroll_print("Smells like rope...")

    elif verb == "listen to":
        scroll_print("You listen...everything is quiet.")

    elif verb == "climb":
        if feature == "rubble":
            scroll_print("You climb on top of a pile of rubble. Congrats! "
                         "You're king of rubble mountain.")

        else:
            scroll_print("You can't climb that.")

    elif verb == "duck":
        scroll_print("You duck quickly and then stand back up.")

    elif verb == "rotate":
        if feature == "rubble":
            scroll_print("You pick up some rubble and turn it around a bit.")

        else:
            scroll_print("I can't rotate that.")

    elif verb == "equip":
        scroll_print("You can't do that.")

    save_object_state(current_room)


def rope_trap(current_room):
    """Handles rope trap event for room 2.

    Args:
        current_room (:obj:`Room`): The room the player is currently in.

    """
    scroll_print("As you walk forward, between the scattered rubble, "
                 "your foot trips on a small hard to see rope. You hear a "
                 "click...\n")

    # Get user response for this mini event.
    scroll_print("What would you like to do?")

    response = input("Type some text: ")
    response.lower().strip()
    scroll_print("")

    # The only valid response to avoid damage is to duck.
    if "duck" in response:
        scroll_print("You duck just as a crossbow bolt passes overhead. "
                     "A narrow miss. You should probably inspect rooms more "
                     "closely in the future.")
    else:
        health_loss = 5

        scroll_print("Before you can do anything, a crossbow bolt flies "
                     "across the room from a hidden opening and strikes "
                     "you in the shoulder. You lose {} health. Ouch! Should "
                     "have ducked.".format(health_loss))

        player = current_room.get_player()

        player.set_health(player.get_health() - health_loss)

    # Set the puzzle status to false to indicate that the rope trap event is
    # complete.
    current_room.set_puzzle_status("rope", False)

    # The feature is removed from the room so that the event does not repeat.
    current_room.remove_feature("rope")

    new_rubble = ("It's mostly stone from the wall strewn across the floor. "
                  "Amongst the rubble is the rope trap that you triggered. "
                  "The rope is now loose and cannot be triggered again.")

    current_room.remove_feature("rubble")

    current_room.add_feature("rubble", new_rubble)

    save_object_state(current_room)


def room_3_feature_handler(current_room, verb, feature):
    """Handles verb commands related to room 3, mess hall, features.

    Puzzles:
        1. engraving:
            Trigger: Look at engraving.

            Disable: Player must enter the command 'rotate engraving'. The
            door to the kitchen will unlock as a result.

    Room Items:
        - bread: Player can eat to gain health.

    Features:
        - armor
        - engraving

    Monsters:
        - Renethe, skeleton.

    Args:
        current_room (:obj:`Room`): The current room the player is in.
        verb (str): The action the user would like to take.
        feature (str): The feature in this room the user would like to act on.

    """
    # Dictionary of feature name mapped to a description of that feature.
    feature_dict = current_room.get_features()

    # Handle feature interaction for each of the main verbs.
    if verb == "take":
        if feature == "engraving":
            scroll_print("You place both hands on the edge of the engraving "
                         "and pull with all your might. It doesn't budge.")

        elif feature == "armor":
            scroll_print("The armor is too heavy to take.")

        elif feature == "table":
            scroll_print("You place both your hands on the table and try to "
                         "move it. No luck, it won't budge.")

        elif feature == "plates":
            scroll_print("You consider taking the plates, but then think "
                         "better of it. You don't have much use for plates "
                         "right now.")

        else:
            scroll_print("I can't take that.")

    elif verb == "use":
        if feature == "armor":
            scroll_print("The armor looks to be to big and heavy for you "
                         "to use.")

        else:
            scroll_print("You can't use that. Better move on or find "
                         "something you can use.")

    elif verb == "drop":
        scroll_print("Drop what? You're not carrying that.")

    elif verb == "look at":
        if feature == "engraving":
            scroll_print("You take a close look at the {}.".format(feature))
            scroll_print("A closer inspection reveals that the engraving is "
                         "on a disc of silver that is attached to, but not "
                         "quite flush with, the surface of the door. Strange "
                         "markings cover the surface of the engraving and are "
                         "pictured below. \n\n")
            print(feature_dict[feature])

        else:
            scroll_print("You take a close look at the {}.".format(feature))

            scroll_print(feature_dict[feature])

    elif verb == "eat":
        scroll_print("You can't eat that.")

    elif verb == "drink":
        scroll_print("You can't drink that.")

    elif verb == "smell":
        if feature == "engraving":
            scroll_print("The engraving doesn't smell like anything.")

        elif feature == "armor":
            scroll_print("Smells dusty.")

        elif feature == "table":
            scroll_print("You smell the smell of rotting food.")

        elif feature == "plates":
            scroll_print("The plates smell terrible. Like rotting food.")

        else:
            scroll_print("Doesn't smell like much.")

    elif verb == "listen to":
        if feature == "armor":
            scroll_print("You put your ear up to one of the suits of armor. "
                         "Inside you hear a mouse scurrying.")

        elif feature == "engraving":
            scroll_print("You put your ear up to the engraving. You hear "
                         "nothing.")

        else:
            scroll_print("You don't hear anything.")

    elif verb == "climb":
        if feature == "armor":
            scroll_print("You start climbing one of the armor statues. As "
                         "you climb, the armor tips and comes crashing to the "
                         "floor. Good, that should wake up the entire "
                         "fortress...")

        elif feature == "table":
            scroll_print("You climb up onto the table and look around. Your "
                         "foot steps in some rotting meat. Gross. You climb "
                         "back down.")

        else:
            scroll_print("You can't climb that")

    elif verb == "duck":
        scroll_print("You duck quickly and then stand back up.")

    # Unlocks the door to the kitchen. Flips the ASCII art so that it is
    # right side up and displays a skull.
    elif verb == "rotate":
        if (feature == "engraving" and
           current_room.get_puzzle_status("engraving")):

            scroll_print("You place both hands on the engraving edges and "
                         "rotate with all your might. It slowly turns until "
                         "the markings have been flipped. You hear a click "
                         "and step back to take a look. The rotated "
                         "engraving...\n")

            new_desc = (
                        "            ________________           \n"
                        "          /-                -\\         \n"
                        "        /-                    -\\       \n"
                        "       |                       |       \n"
                        "      |.|                     |.|      \n"
                        "      | |     -         -     | |      \n"
                        "       \\ \\ ______     ______ / /       \n"
                        "       \\ |. -----\"   \"-----  | /       \n"
                        "        \\| |     \\   /    |  |/        \n"
                        "         |  \\__  /   \\ ___/   |        \n"
                        "         \\       /. .\\       /         \n"
                        "          \\__   .\\| |/ .   _/          \n"
                        "            .\\\\\\       ///.            \n"
                        "            | *\\___!___*  |            \n"
                        "            |  |IIIIIII|  |            \n"
                        "            |   \\IIIII/   |            \n"
                        "             \\           /             \n"
                        "              \\ _______ /              \n"
                        )

            # Do not use scroll_print. It will not print the newlines
            # correctly.
            print(new_desc)

            scroll_print("\nThe door is now open...")

            current_room.unlock("north")

            # Set puzzle status to false so that the engraving can no longer
            # be rotated.
            current_room.set_puzzle_status("engraving", False)

            current_room.remove_feature("engraving")

            current_room.add_feature("engraving", new_desc)

        elif feature == "engraving":
            scroll_print("The engraving can no longer be rotated.")

        elif feature == "plates":
            scroll_print("You pick up some plates and turn them around.")

        elif feature == "table":
            scroll_print("You go to turn one of the tables but it is too "
                         "heavy.")

        else:
            scroll_print("You can't rotate that.")

    elif verb == "equip":
        scroll_print("You can't do that.")

    save_object_state(current_room)


def room_4_feature_handler(current_room, verb, feature):
    """Handle room 4, store room, player and feature interaction.

    Puzzles:
        1. lock box:
            Trigger: Look at shelves.

            Disable: Use golden key to unlock box and get letter item.

        2. vines:
            Trigger: Enter the store room.

            Disable: Use acidic ooze item while in the store room.

        3. voice:
            Trigger: Enter the store room.

            Disable: Automatically disables.

        4. shelves:
            Trigger: Enter store room.

            Disable: Look at shelves.

    Room Items:
        - jar: Used to pick up acidic ooze in room 5.
        - letter: Explains how to get into room 5.

    Features:
        - broom
        - vines
        - shelves
        - carcass
        - box

    Monsters:
        None

    Args:
        current_room (:obj:`Room`): The current room the player is in.
        verb (str): The action the user would like to take.
        feature (str): The feature in this room the user would like to act on.

    """
    # A dictionary that maps feature name to a description of that feature.
    feature_dict = current_room.get_features()

    # Handle custom feature interaction for each of the 10 core verbs.
    if verb == "take":
        if feature == "broom":
            scroll_print("You try and grab the broom, but it evades your "
                         "grasp. It flies around the room a bit more and then "
                         "settles in the corner.")

        elif feature == "vines":
            scroll_print("You pull at the vines, but they do not move.")

        elif feature == "carcass":
            scroll_print("I don't think so, this carcass is way too heavy.")

        elif feature == "box":
            scroll_print("You think about taking the box but decide you "
                         "already have a bag to carry your things. You leave "
                         "the box where it is.")

        else:
            scroll_print("You can't take that.")

    elif verb == "use":
        scroll_print("You can't use that. Better move on or find something "
                     "you can use.")

    elif verb == "drop":
        scroll_print("Drop what? You're not carrying that.")

    elif verb == "look at":
        # Reveals the lockbox. User can now use the golden key to get the
        # letter item.
        if feature == "shelves" and current_room.get_puzzle_status("shelves"):
            current_room.set_puzzle_status("lock box", True)

            # Set shelves staus to false so that lock box can only be
            # opened once.
            current_room.set_puzzle_status("shelves", False)

            scroll_print("You take a close look at the {}.".format(feature))

            scroll_print(feature_dict[feature])

        else:
            scroll_print("You take a close look at the {}.".format(feature))

            scroll_print(feature_dict[feature])

    elif verb == "eat":
        if feature == "broom":
            scroll_print("You try to bite the broom. It flies behind you "
                         "and whacks you on the back of the head. Ouch!")

        elif feature == "vines":
            scroll_print("You gnaw on the vines to no effect. They won't "
                         "budge, and they taste disgusting!")

        elif feature == "shelves":
            scroll_print("What's with you and trying to eat furniture?")

        elif feature == "carcass":
            scroll_print("What are you, a wild animal? This isn't cooked.")

        else:
            scroll_print("You can't eat that.")

    elif verb == "drink":
        scroll_print("You can't drink that.")

    elif verb == "smell":
        if feature == "vines":
            scroll_print("The vines smell like nothing.")

        elif feature == "broom":
            scroll_print("You go to smell the broom. It flies up and hits "
                         "you in the face. Ouch!")

        elif feature == "shelves":
            scroll_print("They smell dusty.")

        elif feature == "carcass":
            scroll_print("Smells like meat.")

        else:
            scroll_print("Doesn't smell like anything.")

    elif verb == "listen to":
        scroll_print("Not much to hear. Nothing happening, really.")

    elif verb == "climb":
        if feature == "shelves":
            scroll_print("You start climbing the shelves, but before you get "
                         "too far up them, the broom flies over and pokes you "
                         "until you stop.")

        elif feature == "vines":
            scroll_print("You start climbing the vines covering the "
                         "stairwell entrance. As you do, the vines start "
                         "to grow thorns. Ouch, you let go of the vines.")

        else:
            scroll_print("You can't climb that.")

    elif verb == "duck":
        scroll_print("You duck quickly and then stand back up.")

    elif verb == "rotate":
        if feature == "carcass":
            scroll_print("You turn the hanging carcass around a bit.")

        elif feature == "broom":
            scroll_print("You go to grab the broom to rotate it. Before you "
                         "can grab it it flies up and hits you in the face. "
                         "Ouch!")

        else:
            scroll_print("I can't rotate that.")

    elif verb == "equip":
        scroll_print("You can't do that.")

    save_object_state(current_room)


def room_5_feature_handler(current_room, verb, feature):
    """Handle room 5, kitchen, player and feature interaction.

    Puzzles:
        1. ooze:
            Trigger: Enter kitchen room.

            Disable: Player must type 'use jar' with the jar item in their
            inventory.

    Room Items:
        - acidic ooze: Used to open room 4 store room door.
        - oven mitt: +3 magic defense.

    Features:
        - fish
        - sink

    Monsters:
        Grugg, sludge monster.

    Args:
        current_room (:obj:`Room`): The current room the player is in.
        verb (str): The action the user would like to take.
        feature (str): The feature in this room the user would like to act on.

    """
    # A dictionary that maps feature name to a description of that feature.
    feature_dict = current_room.get_features()

    # Handle custom feature interaction for each of the 10 core verbs.
    if verb == "take":
        if feature == "fish":
            scroll_print("I wouldn't take that. Just touching that fish is "
                         "probably a health risk.")

        elif feature == "sink":
            scroll_print("You know when people say, \"He took everything but "
                         "the kitchen sink!\" Well, there's good reason. It's "
                         "heavy and attached to the wall. So unless you're "
                         "gonna drop this whole rescue mission and take up "
                         "plumbing I would say no, no you cannot take the "
                         "kitchen sink.")

        else:
            scroll_print("You can't take that.")

    elif verb == "use":
        scroll_print("You can't use that. Better move on or find something "
                     "you can use.")

    elif verb == "drop":
        scroll_print("Drop what? You're not carrying that.")

    elif verb == "look at":
        scroll_print("You take a close look at the {}.".format(feature))

        scroll_print(feature_dict[feature])

    elif verb == "eat":
        if feature == "fish":
            scroll_print("You take a bite of the fish and immediately regret "
                         "it.")

        else:
            scroll_print("You can't eat that.")

    elif verb == "drink":
        scroll_print("You can't drink that.")

    elif verb == "smell":
        scroll_print("Smells rancid.")

    elif verb == "listen to":
        scroll_print("Not much to hear. Nothing happening, really.")

    elif verb == "climb":
        if feature == "sink":
            scroll_print("You climb on the sink. As you do, your foot slips "
                         "and lands in the rancid sink water. Gross! You "
                         "climb back down.")
        else:
            scroll_print("You can't climb that.")

    elif verb == "duck":
        scroll_print("You duck quickly and then stand back up.")

    elif verb == "rotate":
        if feature == "fish":
            scroll_print("You pick up the fish, rotate it, and set it back "
                         "down.")

        else:
            scroll_print("You can't rotate that.")

    elif verb == "equip":
        scroll_print("You can't do that.")

    save_object_state(current_room)


def room_6_feature_handler(current_room, verb, feature):
    """Handle room 6, washroom, player and feature interaction.

    Puzzles:
        1. rubber duck:
            Trigger: Look at tub.

            Disable: Look at tub.

    Room Items:
        - Quackers: Appears in room once tub is looked at. Used in room 7 \
        smoking room to find key. Reference room 7 puzzle information.

    Features:
        - tub
        - fountain

    Monsters:
        Karthos, wisp.

    Args:
        current_room (:obj:`Room`): The current room the player is in.
        verb (str): The action the user would like to take.
        feature (str): The feature in this room the user would like to act on.

    """
    # A dictionary that maps feature name to a description of that feature.
    feature_dict = current_room.get_features()

    # Handle custom feature interaction for each of the 10 core verbs.
    if verb == "take":
        if feature == "tub":
            scroll_print("Do we have forklifts in this game? No, I don't "
                         "think so. That's gonna be a hard no on taking this "
                         "tub.")

        else:
            scroll_print("You can't take that.")

    elif verb == "use":
        scroll_print("You can't use that. Better move on or find something"
                     "you can use.")

    elif verb == "drop":
        scroll_print("Drop what? You're not carrying that.")

    elif verb == "look at":
        # Adds the Quackers item to the room.
        if feature == "tub":
            scroll_print("You take a close look at the {}.".format(feature))

            scroll_print(feature_dict[feature])

            if current_room.get_puzzle_status("rubber duck"):
                scroll_print("You also notice, resting at the bottom of the "
                             "tub, is a little yellow rubber duck. On its "
                             "side written in black ink it says \"Quackers\"")

                # Disable puzzle status so that Quackers is only added to the
                # room once.
                current_room.set_puzzle_status("rubber duck", False)

                rubber_duck = "Quackers"
                rubber_duck_description = ("A little yellow rubber duck. It "
                                           "squeaks when you squeeze it.")
                rubber_duck_durability = None
                rubber_duck_stats = None

                rubber_duck = Item(rubber_duck, rubber_duck_description,
                                   rubber_duck_durability, rubber_duck_stats)

                current_room.add_item(rubber_duck)

        else:
            scroll_print("You take a close look at the {}.".format(feature))

            scroll_print(feature_dict[feature])

    elif verb == "eat":
        scroll_print("You can't eat that.")

    elif verb == "drink":
        if feature == "tub":
            scroll_print("No water left in the tub to drink.")

        elif feature == "fountain":
            scroll_print("You go over to the fountain, lean over, and take a "
                         "drink of the purple liquid. Tastes like soap. You "
                         "hiccup and a soap bubble pops out of your mouth.")

        else:
            scroll_print("You can't drink that.")

    elif verb == "smell":
        scroll_print("Smells soapy.")

    elif verb == "listen to":
        if feature == "fountain":
            scroll_print("You listen to the tranquil sound of the fountain. "
                         "How Zen.")

        elif feature == "tub":
            scroll_print("Water gurgles a bit in the drain.")

        else:
            scroll_print("You don't hear anything.")

    elif verb == "climb":
        if feature == "fountain":
            scroll_print("You start climbing the fountain. Your foot slips "
                         "and lands in the purple liquid. You now have a "
                         "soggy foot, congrats.")

        elif feature == "tub":
            scroll_print("You climb over the edge and sit in the tub for a "
                         "bit. Nothing like sitting in an empty tub for a "
                         "bit to motivate you when you're on a rescue "
                         "mission...")

        else:
            scroll_print("You can't climb that.")

    elif verb == "duck":
        scroll_print("You duck quickly and then stand back up.")

    elif verb == "rotate":
        scroll_print("You can't rotate that.")

    elif verb == "equip":
        scroll_print("You can't do that.")

    save_object_state(current_room)


def room_7_feature_handler(current_room, verb, feature):
    """Handle room 7, smoking room, player and feature interaction.

    Puzzles:
        1. smoke:
            Trigger: Look at the humidor. Then look at the ash tray.

            Disable: Use Quackers.

    Room Items:
        - emerald key: Get by triggering the puzzle and then using Quackers. \
        opens room 8 emerald lock box.

    Features:
        - humidor
        - ash tray

    Monsters:
        None

    Args:
        current_room (:obj:`Room`): The current room the player is in.
        verb (str): The action the user would like to take.
        feature (str): The feature in this room the user would like to act on.

    """
    # A dictionary that maps feature name to a description of that feature.
    feature_dict = current_room.get_features()

    # Handle custom feature interaction for each of the 10 core verbs.
    if verb == "take":
        if feature == "humidor":
            scroll_print("You attempt to take the humidor, however, it is "
                         "bolted to the wall.")

        elif feature == "ash tray":
            scroll_print("There are still some embers, you better not grab "
                         "those or you might get burned.")

        elif feature == "smoke":
            scroll_print("You try and grab the smoky figure but your hand "
                         "passes through. The figure quickly reforms and "
                         "continues looking at you expectantly.")

        else:
            scroll_print("You can't take that.")

    elif verb == "use":
        scroll_print("You can't use that. Better move on or find something "
                     "you can use.")

    elif verb == "drop":
        scroll_print("Drop what? You're not carrying that.")

    elif verb == "look at":
        # Looking at humidor enables the smoke puzzle. The player can now
        # look at the ash tray to reveal the presence of the smoke feature.
        if (feature == "humidor" and
           not current_room.get_puzzle_status("smoke")):

            current_room.set_puzzle_status("smoke", True)

            ash_feature = ("The heat from looking at the humidor has brought "
                           "some of the embers in the ash tray back to life. "
                           "Some peculiar smoke patterns start to appear.")

            smoke_feature = ("A wisp of smoke turns into a small humanoid "
                             "shape. You feel as though it is looking "
                             "expectantly at you.")

            # Update ash tray feature to add reference to smoke. This is
            # updated in the item_handler file once the puzzle is complete.
            current_room.remove_feature("ash tray")

            current_room.add_feature("ash tray", ash_feature)

            current_room.add_feature("smoke", smoke_feature)

            scroll_print("You take a close look at the {}.".format(feature))

            scroll_print(feature_dict[feature])

        else:
            scroll_print("You take a close look at the {}.".format(feature))

            scroll_print(feature_dict[feature])

    elif verb == "eat":
        if feature == "ash tray":
            scroll_print("Eating an whole ash tray, wouldn't that be an "
                         "interesting party trick. You decide to leave the "
                         "ash tray where it is.")
        else:
            scroll_print("You can't eat that.")

    elif verb == "drink":
        scroll_print("You can't drink that.")

    elif verb == "smell":
        scroll_print("Smells smoky.")

    elif verb == "listen to":
        scroll_print("All is quiet.")

    elif verb == "climb":
        if feature == "table":
            scroll_print("The table is too small to safely climb onto.")

        elif feature == "chair":
            scroll_print("You climb onto the chair and get your dirty "
                         "footprints all over the nice plush fabric. Nice!")

        else:
            scroll_print("You can't climb that.")

    elif verb == "duck":
        scroll_print("You duck quickly and then stand back up.")

    elif verb == "rotate":
        if feature == "ash tray":
            scroll_print("You pick up the ash tray and turn it around a bit.")

        elif feature == "chair":
            scroll_print("You pick the chair up and turn it around.")

        else:
            scroll_print("You can't rotate that.")

    elif verb == "equip":
        scroll_print("You can't do that.")

    save_object_state(current_room)


def room_8_feature_handler(current_room, verb, feature):
    """Handle room 8, sleeping chambers, player and feature interaction.

    Puzzles:
        1. nightstand:
            Trigger: Enter the sleeping chambers.

            Disable: Use the emerald key.

    Room Items:
        - book: Contains a cipher to solve the mirror puzzle in the sauna room.

    Features:
        - bed
        - window
        - box

    Monsters:
        None

    Args:
        current_room (:obj:`Room`): The current room the player is in.
        verb (str): The action the user would like to take.
        feature (str): The feature in this room the user would like to act on.

    """
    # A dictionary that maps feature name to a description of that feature.
    feature_dict = current_room.get_features()

    # Handle custom feature interaction for each of the 10 core verbs.
    if verb == "take":
        if feature == "box":
            scroll_print("As you reach out to take the emerald box, a small "
                         "flash of green lightning arcs from it and shocks "
                         "you. You better leave this box where it is.")

        else:
            scroll_print("You can't take that.")

    elif verb == "use":
        scroll_print("You can't use that. Better move on or find something "
                     "you can use.")

    elif verb == "drop":
        scroll_print("Drop what? You're not carrying that.")

    elif verb == "look at":
        scroll_print("You take a close look at the {}.".format(feature))

        scroll_print(feature_dict[feature])

    elif verb == "eat":
        scroll_print("You can't eat that.")

    elif verb == "drink":
        scroll_print("You can't drink that.")

    elif verb == "smell":
        if feature == "bed":
            scroll_print("Smell the bed? No thanks, this is getting a little "
                         "too weird.")

        elif feature == "window":
            scroll_print("Smells like a window I guess...")

        else:
            scroll_print("Doesn't smell like much.")

    elif verb == "listen to":
        scroll_print("You don't hear much.")

    elif verb == "climb":
        if feature == "bed":
            scroll_print("You climb on the bed and start jumping up and down. "
                         "Wooo what fun.")

        else:
            scroll_print("You can't climb that.")

    elif verb == "duck":
        scroll_print("You duck quickly and then stand back up.")

    elif verb == "rotate":
        scroll_print("You can't rotate that.")

    elif verb == "equip":
        scroll_print("You can't do that.")

    save_object_state(current_room)


def room_9_feature_handler(current_room, verb, feature):
    """Handle room 9, supplies closet, player and feature interaction.

    Puzzles:
        1. shelves:
            Trigger: Use the command 'climb shelves'.

            Disable: Use the command 'climb shelves'.

    Room Items:
        - rapier: Got by triggering the shelves puzzle. Simply use the \
        command climb shelves. Gives +5 attack power.

    Features:
        - towels
        - shampoo
        - shelves

    Monsters:
        Ulthu, goblin.

    Args:
        current_room (:obj:`Room`): The current room the player is in.
        verb (str): The action the user would like to take.
        feature (str): The feature in this room the user would like to act on.

    """
    # A dictionary that maps feature name to a description of that feature.
    feature_dict = current_room.get_features()

    # Handle custom feature interaction for each of the 10 core verbs.
    if verb == "take":
        if feature == "towels":
            scroll_print("You reach out to grab a towel. The towel quickly "
                         "rises up and wraps around your face. As you try to "
                         "remove it, two other towels proceed to roll up and "
                         "start whipping you. Eventually the towels fly away, "
                         "leaving you feeling rather embarrassed.")

        elif feature == "shampoo":
            scroll_print(feature_dict[feature])

        else:
            scroll_print("You can't take that.")

    elif verb == "use":
        scroll_print("You can't use that. Better move on or find something "
                     "you can use.")

    elif verb == "drop":
        scroll_print("Drop what? You're not carrying that.")

    elif verb == "look at":
        scroll_print("You take a close look at the {}.".format(feature))

        scroll_print(feature_dict[feature])

    elif verb == "eat":
        if feature == "towels":
            scroll_print("You try and eat one of the towels, but it flies "
                         "away, avoiding your grasp. You get the sense that "
                         "the objects in the supplies closet are looking at "
                         "you like you're a maniac.")

        elif feature == "shampoo":
            scroll_print("Does your mouth have hair in it? No? Then why are "
                         "you trying to put shampoo in it?")

        else:
            scroll_print("You can't eat that.")

    elif verb == "drink":
        if feature == "shampoo":
            scroll_print("Does your mouth have hair in it? No? Then why are "
                         "you trying to put shampoo in it?")

        else:
            scroll_print("You can't drink that.")

    elif verb == "smell":
        if feature == "towels":
            scroll_print("The towels have the unmistakable smell of goblin.")

        elif feature == "shampoo":
            scroll_print("Smells like lavender.")

        else:
            scroll_print("Smells like lavender...and goblin.")

    elif verb == "listen to":
        if feature == "towels":
            scroll_print("You hear the towels shift and rustle a bit.")

        else:
            scroll_print("You don't hear much.")

    elif verb == "climb":
        # Get the rapier by climbing the shelves in the room.
        if (feature == "shelves" and
           current_room.get_puzzle_status("shelves")):
            scroll_print("You climb the shelves to find what is causing the "
                         "blue glow. As you reach the top, you find that the "
                         "blue glow is caused by a long, thin rapier.")

            # Add rapier item to players inventory.
            rapier_name = "rapier"
            rapier_description = ("A thin and nimble long sword. The blade "
                                  "glows blue and it is razor sharp. "
                                  "(Equip this item to gain stats)")
            rapier_durability = None
            rapier_stats = {"attack_power": 5}

            rapier = Item(rapier_name, rapier_description, rapier_durability,
                          rapier_stats)

            player = current_room.get_player()

            player.add_item(rapier)

            # Set the puzzle status to false so that player cannot repeat
            # puzzle.
            current_room.set_puzzle_status("shelves", False)

            # Update shelves feature so that it does not mention glow.
            shelves_feature = ("They contain mostly towels. Nothing of note.")

            current_room.remove_feature("shelves")

            current_room.add_feature("shelves", shelves_feature)

        elif feature == "shelves":
            scroll_print("You climb the selves. There's nothing else to find.")

        else:
            scroll_print("You can't climb that.")

    elif verb == "duck":
        scroll_print("You duck quickly and then stand back up.")

    elif verb == rotate:
        if feature == "shampoo":
            scroll_print(feature_dict[feature])

        elif feature == "towels":
            scroll_print(feature_dict[feature])

        else:
            scroll_print("I can't rotate that.")

    elif verb == "equip":
        scroll_print("You can't do that.")

    save_object_state(current_room)


def room_10_feature_handler(current_room, verb, feature):
    """Handle room 10, sauna room, player and feature interaction.

    Puzzles:
        1. steam:
            Trigger: Enter the sauna and listen to machinery to locate the
            mirror. Then look at the mirror.

            Disable: Enter 'password' when prompted by the mirror. This is the
            answer that is given by decoding the phrase given by the mirror
            using the cipher found in the book from the sleeping chambers.

        2. sauna voice:
            Trigger: Enter the sauna room.

            Disable: Automatically disables on its own.

    Room Items:
        None

    Features:
        - machinery
        - mirror

    Monsters:
        None

    Args:
        current_room (:obj:`Room`): The current room the player is in.
        verb (str): The action the user would like to take.
        feature (str): The feature in this room the user would like to act on.

    """
    # A dictionary that maps feature name to a description of that feature.
    feature_dict = current_room.get_features()

    # Handle custom feature interaction for each of the 10 core verbs.
    if verb == "take":
        if feature == "mirror":
            scroll_print("You reach out to take the mirror. Before you can "
                         "grab it, a little storm cloud forms in front of "
                         "your face and emits a tiny lightning bolt that "
                         "shocks you. Ouch! You better leave this mirror "
                         "here.")
        else:
            scroll_print("You can't take that.")

    elif verb == "use":
        scroll_print("You can't use that. Better move on or find something "
                     "you can use.")

    elif verb == "drop":
        scroll_print("Drop what? You're not carrying that.")

    elif verb == "look at":
        # Mirror puzzle. Player must enter in a password to progress in the
        # game. The password is 'password'.
        if feature == "mirror" and current_room.get_puzzle_status("steam"):
            scroll_print("You take a close look at the {}".format(feature))

            scroll_print(feature_dict[feature])

            puzzle_result = mirror_puzzle()

            # When user enters correct password: 'password'.
            if puzzle_result:
                scroll_print("\nThe text in the mirror swirls and changes. It "
                             "reconfigures to say \"Password accepted.\". All "
                             "of a sudden you hear the machinery stop. The "
                             "magic steam stops exuding from the vent and the "
                             "room slowly becomes visible.\n")

                # Update room description so that there is no longer steam.
                description = ("The room is made of marble. Benches of marble "
                               "line the walls. The magic mirror hangs from "
                               "the left side of the room. To the south is a "
                               "birch door leading to the supplies closet. To "
                               "the north is a marble staircase leading to "
                               "the tower hall.",
                               "You're in the sauna room. To the south, there "
                               "is a birch door leading back to the supplies "
                               "closet. To the north, a marble staircase "
                               "leads to the tower hall.")

                current_room.set_description(description)

                # Update mirror feature.
                mirror_feature = ("The message \"Password accepted.\" is "
                                  "still displayed on the mirror surface.")

                current_room.remove_feature("mirror")

                current_room.add_feature("mirror", mirror_feature)

                # Update machinery feature.
                machinery_feature = ("The sound of machinery has disappeared.")

                current_room.remove_feature("machinery")

                current_room.add_feature("machinery", machinery_feature)

                # Add door from sauna room to tower hall.
                new_door_map = {'south': False, 'north': False}

                current_room.set_door_map(new_door_map)

                new_adjacent_rooms = {'north': 'tower hall', 'east': None,
                                      'south': 'supplies closet', 'west': None}

                current_room.set_adjacent_rooms(new_adjacent_rooms)

                # Set puzzle status to false so that mirror puzzle will not
                # repeat.
                current_room.set_puzzle_status("steam", False)

                scroll_print(current_room.get_description())

            # When user enters wrong password.
            else:
                scroll_print("The text on the mirror swirls and reconfigures "
                             "to say \"Password denied!\" A small storm cloud "
                             "forms in front of the mirror and emits a small "
                             "lightning bolt that shocks you. The cloud "
                             "quickly dissipates and the mirror goes blank.")

        else:
            scroll_print("You take a close look at the {}.".format(feature))

            scroll_print(feature_dict[feature])

    elif verb == "eat":
        if feature == "mirror":
            scroll_print("A thought pops into your head. \"You wouldn't eat a "
                         "couch would you? You wouldn't eat a chair would "
                         "you? Eating mirrors is a crime. This thought has "
                         "been paid for by the national mirror association "
                         "for the prevention of magic mirror related "
                         "crimes.\"")

        else:
            scroll_print("You can't eat that.")

    elif verb == "drink":
        scroll_print("You can't drink that.")

    elif verb == "smell":
        scroll_print("Doesn't smell like much.")

    elif verb == "listen to":
        if feature == "machinery":
            scroll_print(feature_dict[feature])

        else:
            scroll_print("You hear nothing.")

    elif verb == "climb":
        scroll_print("You can't climb that.")

    elif verb == "duck":
        scroll_print("You duck quickly and then stand back up.")

    elif verb == "rotate":
        if feature == "mirror":
            scroll_print("You reach out to take the mirror. Before you can "
                         "grab it, a little storm cloud forms in front of "
                         "your face and emits a tiny lightning bolt that "
                         "shocks you. Ouch! You better leave this mirror "
                         "here.")

        else:
            scroll_print("You can't rotate that.")

    elif verb == "equip":
        scroll_print("You can't do that.")

    save_object_state(current_room)


def mirror_puzzle():
    """Handles mirror puzzle for room 10, sauna room.

    Returns:
        bool: True if password: 'password' entered by user. False otherwise.

    """
    user_input = input("\nThe mirror wants you to say something. What do you "
                       "say? Enter some text: ")

    user_input.lower().strip()

    if user_input == "password":
        return True
    else:
        return False


def room_11_feature_handler(current_room, verb, feature):
    """Handle room 11, tower hall, player and feature interaction.

    Puzzles:
        None

    Room Items:
        - charcoal: got by using the command 'take charcoal'. Use in room 12, \
        archives, by typing the command 'use charcoal' to get the 'scrap' item.

    Features:
        - ceiling
        - painting: Once you get the scrap item from room 12, archives, type \
        'use scrap' in this room to get a blessing of +1 attack power.
        - table
        - ruby
        - charcoal: disappears after you use the command 'take charcoal'.
        - dagger

    Monsters:
        None

    Args:
        current_room (:obj:`Room`): The current room the player is in.
        verb (str): The action the user would like to take.
        feature (str): The feature in this room the user would like to act on.

    """
    # A dictionary that maps feature name to a description of that feature.
    feature_dict = current_room.get_features()

    # Handle custom feature interaction for each of the 10 core verbs.
    if verb == "take":
        if feature == "ruby":
            scroll_print("You reach out to take the ruby. As your hand closes "
                         "around it, you feel nothing. The ruby is an "
                         "illusion. Suddenly your hand bursts into flames. "
                         "You quickly use your bag to smother the flames, but "
                         "not before your hand is badly burned. You lose 5 "
                         "health.")

            player = current_room.get_player()
            player.set_health(player.get_health() - 5)

        elif feature == "dagger":
            scroll_print("You reach out to take the dagger. As your hand gets "
                         "close, the dagger morphs into a snake and strikes. "
                         "Your hand is bit. You pull away and the snake turns "
                         "back into a dagger. You feel weaker, the snake may "
                         "have been poisonous. You lose 5 health.")

            player = current_room.get_player()
            player.set_health(player.get_health() - 5)

        # Charcoal is the solution to the riddle. and the only valid choice.
        elif feature == "charcoal":

            # Remove charcoal feature and update table description.
            current_room.remove_feature('charcoal')
            current_room.remove_feature('table')

            table_feature = ("The charcoal is gone. Only the ruby and dagger "
                             "remain.")

            current_room.add_feature('table', table_feature)

            # Add charcoal item to player's inventory.
            charcoal_name = "charcoal"
            charcoal_description = ("This is charcoal like the type your "
                                    "village smithy would use to fuel his "
                                    "furnace.")
            charcoal_durability = 1
            charcoal_stats = None

            charcoal = Item(charcoal_name, charcoal_description,
                            charcoal_durability, charcoal_stats)

            player = current_room.get_player()

            player.add_item(charcoal)

        else:
            scroll_print("You can't take that.")

    elif verb == "use":
        scroll_print("You can't use that. Better move on or find something "
                     "you can use.")

    elif verb == "drop":
        scroll_print("Drop what? You're not carrying that.")

    elif verb == "look at":
        scroll_print("You take a close look at the {}.".format(feature))

        scroll_print(feature_dict[feature])

    elif verb == "eat":
        scroll_print("You can't eat that.")

    elif verb == "drink":
        scroll_print("You can't drink that.")

    elif verb == "smell":
        if feature == "charcoal":
            scroll_print("Smells like charcoal.")

        elif feature == "painting":
            scroll_print("The painting smells dusty.")

        else:
            scroll_print("Doesn't smell like much.")

    elif verb == "listen to":
        scroll_print("You don't hear anything.")

    elif verb == "climb":
        scroll_print("You can't climb that.")

    elif verb == "duck":
        scroll_print("You duck quickly and then stand back up.")

    elif feature == "rotate":
        scroll_print("You can't rotate that.")

    elif verb == "equip":
        scroll_print("You can't do that.")

    save_object_state(current_room)


def room_12_feature_handler(current_room, verb, feature):
    """Handle room 12, archives, player and feature interaction.

    Puzzles:
        None

    Room Items:
        - mythril tongs: +8 magic power.
        - scrap: Got by typing 'use charcoal' with charcoal in your \
        inventory. Charcoal got from room 11, tower hall. Use scrap in room \
        11, tower hall, to get a blessing.


    Features:
        - fireplace
        - chandelier

    Monsters:
        Exelior, skeleton.

    Args:
        current_room (:obj:`Room`): The current room the player is in.
        verb (str): The action the user would like to take.
        feature (str): The feature in this room the user would like to act on.

    """
    # A dictionary that maps feature name to a description of that feature.
    feature_dict = current_room.get_features()

    # Handle custom feature interaction for each of the 10 core verbs.
    if verb == "take":
        if feature == "chandelier":
            scroll_print("Maybe if you can find a ladder you can make an "
                         "attempt. Until then, better leave the chandelier "
                         "where it is.")

        elif feature == "cobwebs":
            scroll_print("You reach out to take some of the cobwebs. As you "
                         "do, a spider appears and scurries near your hand. "
                         "You quickly move your hand out of the way and the "
                         "spider returns to whatever dark corner it came "
                         "from.")

        else:
            scroll_print("You can't take that.")

    elif verb == "use":
        scroll_print("You can't use that. Better move on or find something "
                     "you can use.")

    elif verb == "drop":
        scroll_print("Drop what? You're not carrying that.")

    elif verb == "look at":
        scroll_print("You take a close look at the {}.".format(feature))

        scroll_print(feature_dict[feature])

    elif verb == "eat":
        if feature == "cobwebs":
            scroll_print("Eat cobwebs? No thanks, you think to yourself.")

        else:
            scroll_print("You can't eat that.")

    elif verb == "drink":
        scroll_print("You can't drink that.")

    elif verb == "smell":
        if feature == "chandelier":
            scroll_print("The air under the chandelier smells like rain.")

        elif feature == "fireplace":
            scroll_print("A smoky smell emits from the fireplace.")

        else:
            scroll_print("Doesn't smell like much.")

    elif verb == "listen to":
        if feature == "fireplace":
            scroll_print("You hear the crackle of the fireplace. It reminds "
                         "you of nights at home sitting in front of the "
                         "hearth. Your resolve to rescue Evelyn strengthens.")

        elif feature == "chandelier":
            scroll_print("No noise comes from the chandelier.")

        else:
            scroll_print("You hear the crackle of the fireplace in the "
                         "the room but nothing else.")

    elif verb == "climb":
        if feature == "chandelier":
            scroll_print("You start to sing, \"I'm gonna swing from the "
                         "chandelieeeer, from the chandelieeer. I'm gonna "
                         "live like tomorrow doesn't exiiiist...\"")

        elif feature == "cobwebs":
            scroll_print("What am I a spider? I don't think so.")

        else:
            scroll_print("You can't climb that.")

    elif verb == "duck":
        scroll_print("You duck quickly and then stand back up.")

    elif verb == "rotate":
        scroll_print("You can't rotate that.")

    elif verb == "equip":
        scroll_print("You can't do that.")

    save_object_state(current_room)


def room_13_feature_handler(current_room, verb, feature):
    """Handle room 13, reading room, player and feature interaction.

    Puzzles:
        1. raven:
            Trigger: Look at raven.

            Disable: Type 'knock knock' after having looked at raven. Then
            Type any two additional phrases when prompted.

    Room Items:
        - iron key: Got by completing the raven puzzle.

    Features:
        - tome
        - couch
        - raven

    Monsters:
        None

    Args:
        current_room (:obj:`Room`): The current room the player is in.
        verb (str): The action the user would like to take.
        feature (str): The feature in this room the user would like to act on.

    """
    # A dictionary that maps feature name to a description of that feature.
    feature_dict = current_room.get_features()

    # Handle custom feature interaction for each of the 10 core verbs.
    if verb == "take":
        if feature == "tome":
            scroll_print(feature_dict[feature])

        elif feature == "couch":
            scroll_print(feature_dict[feature])

        elif feature == "raven":
            scroll_print("The raven's perch is too high to reach.")

        else:
            scroll_print("You can't take that.")

    elif verb == "use":
        scroll_print("You can't use that. Better move on or find something "
                     "you can use.")

    elif verb == "drop":
        scroll_print("Drop what? You're not carrying that.")

    elif verb == "look at":
        # Raven puzzle. User needs to type 'knock knock' and then two
        # additional phrases (they can be anything) to solve the puzzle.
        if feature == "raven" and current_room.get_puzzle_status("raven"):
            scroll_print("You take a close look at the {}.".format(feature))

            scroll_print(feature_dict[feature])

            # On successful completion.
            if raven_joke():
                scroll_print("\nThe raven emits several hearty squawks that "
                             "almost sound like laughter. It drops the key, "
                             "which clatters to the floor. You pick it up. "
                             "For some reason you get the feeling the raven "
                             "doesn't speak English very well...\n")

                # Add iron key to player inventory. Used to unlock cage
                # in room of last rites.
                key_name = "iron key"
                key_description = ("A plain iron key.")
                key_durability = 1
                key_stats = None

                key = Item(key_name, key_description, key_durability,
                           key_stats)

                player = current_room.get_player()

                player.add_item(key)

                # Set puzzle status to false so that puzzle does not repeat.
                current_room.set_puzzle_status("raven", False)

                # Joke can only be done once. Raven feature updated.
                new_raven = ("He has dark black feathers. Engraved at the "
                             "base of its perch is the name Artemis. The "
                             "raven is carrying nothing currently. He "
                             "doesn't seem to be paying attention to you "
                             "anymore.")

                current_room.remove_feature("raven")

                current_room.add_feature("raven", new_raven)

            else:
                scroll_print("\nHmm well that didn't lead to anything.")

        else:
            scroll_print("You take a close look at the {}.".format(feature))

            scroll_print(feature_dict[feature])

    elif verb == "eat":
        if feature == "tome":
            scroll_print("You step closer to the tome with the intent to tear "
                         "a page off and eat it. As you near it, the book "
                         "suddenly becomes surrounded by a raging inferno of "
                         "flames. You can feel the heat. As you take a step "
                         "back the flames subside, leaving the book unharmed.")

        elif feature == "couch":
            scroll_print(feature_dict[feature])

        elif feature == "raven":
            scroll_print("In your mind, a picture of a nice cooked pheasant "
                         "replaces the image of the raven. You look at the "
                         "raven high up on its perch and start to drool.")

        else:
            scroll_print("You can't eat that.")

    elif verb == "drink":
        scroll_print("You can't drink that.")

    elif verb == "smell":
        if feature == "tome":
            scroll_print("You smell the air near the tome. It smells "
                         "strange, as do most highly magical items.")

        elif feature == "couch":
            scroll_print("Every time you get remotely close to the couch, it "
                         "starts sinking into the ground. Guess you'll have "
                         "to find something else to smell.")

        elif feature == "raven":
            scroll_print("You walk over to the area under where the bird's "
                         "perch is. You start sniffing the air. The bird "
                         "looks at you with a somewhat alarmed expression on "
                         "its face.")

        else:
            scroll_print("You can't smell that.")

    elif verb == "listen to":
        if feature == "tome":
            scroll_print("You step closer to the tome and listen. You hear "
                         "the faint sound of writing. As you look at the "
                         "current page, you see that words are appearing out "
                         "of nowhere. They are in a language you have never "
                         "seen before.")

        elif feature == "couch":
            scroll_print("Not much sound coming from the couch, even when "
                         "it's sinking into the ground...")

        elif feature == "raven":
            scroll_print("You listen for any sounds coming from the raven. It "
                         "stands on its perch and looks at you silently.")

        else:
            scroll_print("You don't hear a sound.")

    elif verb == "climb":
        if feature == "couch":
            scroll_print("You've had enough. You step back and take a "
                         "running leap to try and climb onto the couch before "
                         "it disappears. Just as you almost touch it, it "
                         "sinks the last couple inches into the ground and "
                         "you faceplant onto the hard stone floor. Ouch!")

        elif feature == "tome":
            scroll_print(feature_dict[feature])

        elif feature == "raven":
            scroll_print("The raven's perch hangs from the ceiling and is not "
                         "reachable from the ground.")

        else:
            scroll_print("You can't climb that")

    elif verb == "duck":
        scroll_print("You duck quickly and then stand back up.")

    elif verb == "rotate":
        if feature == "tome":
            scroll_print(feature_dict[feature])

        elif feature == "couch":
            scroll_print(feature_dict[feature])

        else:
            scroll_print("You can't rotate that.")

    elif verb == "equip":
        scroll_print("You can't do that.")

    save_object_state(current_room)


def raven_joke():
    """Handles raven puzzle for room 13, reading room.

    Returns:
        bool: True if knock knock entered and two additional phrases entered.
        False otherwise.

    """
    scroll_print("\nYou get the feeling that the raven is expecting you to say "
                 "something.")

    user_input = input("Words you would like to say to raven: ")

    user_input.lower().strip()

    # Only required input is to enter 'knock knock' when first prompted.
    # Other two inputs can be random.
    if user_input == "knock knock":
        scroll_print("\nThe raven looks intently at you. You suddenly hear a "
                     "voice in your mind say, \"Who's there?\"")

        user_input = input("Next words to the raven: ")

        scroll_print("\nYou hear a voice in you mind say, \"{} Who?\""
                     .format(user_input))

        user_input = input("\nNext words to the raven: ")

        return True

    # Return false if use fails to enter in knock knock.
    else:
        scroll_print("\nThe raven looks away from you. You suddenly hear a "
                     "voice in your mind say, \"That's not how the joke "
                     "starts.\"")

        return False


def room_14_feature_handler(current_room, verb, feature):
    """Handle room 14, room of last rites, player and feature interaction.

    Puzzles:
        1. cage:
            Trigger: Look at cage.

            Disable: Type command 'use iron key', with the iron key item in
            your inventory. Iron key item got by completing the raven puzzle
            in room 13, the reading room.

    Room Items:
        - skull key: Got by completing cage puzzle in this room.

    Features:
        - bones
        - hand print
        - cage

    Monsters:
        None

    Args:
        current_room (:obj:`Room`): The current room the player is in.
        verb (str): The action the user would like to take.
        feature (str): The feature in this room the user would like to act on.

    """
    # A dictionary that maps feature name to a description of that feature.
    feature_dict = current_room.get_features()

    # Handle custom feature interaction for each of the 10 core verbs.
    if verb == "take":
        if feature == "bones":
            scroll_print("Take the bones? Are you a troll? That's what "
                         "trolls do, they collect bones. Lets maybe stick to "
                         "picking up useful items...")

        elif feature == "hand print":
            scroll_print("You can't take a hand print...")

        elif feature == "cage":
            scroll_print("The cage is firmly attached to the ceiling by a "
                         "long chain. You can't take this.")

        elif feature == "fairy":
            scroll_print("The bars of the cage are too narrow for you to "
                         "reach through and grab the fairy.")

        else:
            scroll_print("You can't take that.")

    elif verb == "use":
        scroll_print("You can't use that. Better move on or find something "
                     "you can use.")

    elif verb == "drop":
        scroll_print("Drop what? You're not carrying that.")

    elif verb == "look at":
        # Cage puzzle. Unlocked by iron key got in the reading room by
        # completing the raven puzzle.
        if feature == "cage" and current_room.get_puzzle_status("cage"):
            scroll_print("You take a close look at the {}.".format(feature))

            scroll_print(feature_dict[feature])

            fairy_feature = ("She is small and emits a light so bright that "
                             "you can't make out what she looks like.")

            current_room.add_feature("fairy", fairy_feature)

            scroll_print("As you near you notice a small light glowing near "
                         "the cages' center. You hear a small voice. It "
                         "says, \"Hey you! You're not a Goblin! I can tell by "
                         "your magic aura. Oh thank goodness, you must "
                         "help me! I'm a fairy from the forest. I was "
                         "captured and put on display here. Normally I would "
                         "use my magic to escape, but this cage seems to be "
                         "preventing me from casting any spells. Please, you "
                         "must get the keys to unlock the cage. The warlock's "
                         "pet raven has them in the reading room. His name is "
                         "Artemis. To get the keys you must look directly at "
                         "him. After he notices you, you must make him laugh. "
                         "That is the only way to get him to drop the keys. "
                         "He likes knock knock jokes. Maybe try one of "
                         "those...")
        else:
            scroll_print("You take a close look at the {}.".format(feature))

            scroll_print(feature_dict[feature])

    elif verb == "eat":
        if feature == "bones":
            scroll_print("Um I don't think you should do that. Eating bones "
                         "is what the bad guys do...")

        elif feature == "hand print":
            scroll_print("You can't eat a hand print.")

        elif feature == "cage" and current_room.get_puzzle_status("cage"):
            scroll_print("You gnaw on the bars. The fairy looks at you and "
                         "says, \"Um I don't think that's going to work...\"")

        elif feature == "cage":
            scroll_print("You gnaw on the bars a bit. Nothing happens.")

        elif feature == "fairy":
            scroll_print("They say if you harm a fairy you will be cursed for "
                         "life. You should find a way to help her instead.")

        else:
            scroll_print("You can't eat that.")

    elif verb == "drink":
        scroll_print("You can't drink that.")

    elif verb == "smell":
        if feature == "bones":
            scroll_print("The bones smell like death and decay.")

        elif feature == "hand print":
            scroll_print("Hmm maybe if you were a bloodhound you could smell "
                         "something useful from this hand print. As it "
                         "stands, you smell nothing.")

        elif feature == "cage" and current_room.get_puzzle_status("cage"):
            scroll_print("You start sniffing around the cage. The fairy looks "
                         "at you and says, \"Um what are you doing? You're "
                         "scaring me a little...\"")

        elif feature == "fairy":
            scroll_print("You start sniffing around the cage. The fairy looks "
                         "at you and says, \"Um what are you doing? You're "
                         "scaring me a little...\"")

        else:
            scroll_print("You don't smell anything apart from the general "
                         "smell of death and decay present in the room.")

    elif verb == "listen to":
        if feature == "fairy":
            scroll_print("You hold your hand to your ear as you look toward "
                         "the fairy. \"What? I already told you what you need "
                         "to do to rescue me. What more do you want me to "
                         "say?\"")

        else:
            scroll_print("You don't hear anything of note.")

    elif verb == "climb":
        if feature == "bones":
            scroll_print("You climb up on a pile of bones. You get an "
                         "unsettling feeling and decide to climb down.")

        elif feature == "cage" and current_room.get_puzzle_status("cage"):
            scroll_print("You grab onto the cage and it starts to swing back "
                         "and forth. The fairy yells, \"Stop that! You can't "
                         "open this cage by climbing it, you know.\"")

        elif feature == "cage":
            scroll_print("You hop in the open cage and sit for a bit. Feels "
                         "kinda cramped. You better climb out before the "
                         "cage door accidentally closes and traps you in "
                         "here.")

        else:
            scroll_print("You can't climb that.")

    elif verb == "duck":
        scroll_print("You duck quickly and then stand back up.")

    elif verb == "rotate":
        scroll_print("You can't rotate that.")

    elif verb == "equip":
        scroll_print("You can't do that.")

    save_object_state(current_room)


def room_15_feature_handler(current_room, verb, feature):
    """Handle room 15, final lair, player and feature interaction.

    Puzzles:
        None

    Room Items:
        None

    Features:
        - evelyn
        - mirror

    Monsters:
        Zlor, warlock.

    Args:
        current_room (:obj:`Room`): The current room the player is in.
        verb (str): The action the user would like to take.
        feature (str): The feature in this room the user would like to act on.

    """
    # A dictionary that maps feature name to a description of that feature.
    feature_dict = current_room.get_features()

    # Handle custom feature interaction for each of the 10 core verbs.
    if verb == "take":

        # Triggers end of game.
        if feature == "evelyn":
            scroll_print(feature_dict[feature])

            player = current_room.get_player()

            player.rescue_evelyn = True

        else:
            scroll_print("You've come so far. You're too tired to think about "
                         "taking the mirror. All you can think about is "
                         "taking Evelyn and going home.")

    elif verb == "use":
        scroll_print("You can't use that. Better move on or find something "
                     "you can use.")

    elif verb == "drop":
        scroll_print("Drop what? You're not carrying that.")

    elif verb == "look at":

        # Triggers end of game.
        if feature == "evelyn":
            scroll_print(feature_dict[feature])

            player = current_room.get_player()

            player.rescue_evelyn = True

        elif feature == "mirror":
            scroll_print(feature_dict[feature])

    elif verb == "eat":
        scroll_print("I'm sure you meant to type something else. It's been a "
                     "long journey...")

    elif verb == "drink":
        scroll_print("I'm sure you meant to type something else. It's been a "
                     "long journey...")

    elif verb == "smell":
        scroll_print("The slight smell of goblin still lingers in the air. "
                     "You do not notice any other smells.")

    elif verb == "listen to":
        if feature == 'evelyn':
            scroll_print("Evelyn's breathing has started to calm down.")

        else:
            scroll_print("You don't hear anything. The room is quiet except "
                         "for Evelyn's breathing.")

    elif verb == "climb":
        scroll_print("You can't climb that.")

    elif verb == "duck":
        scroll_print("You duck quickly and then stand back up.")

    elif verb == "rotate":
        scroll_print("You can't rotate that.")

    elif verb == "equip":
        scroll_print("You can't do that.")

    save_object_state(current_room)
