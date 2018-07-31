from file_manager import *


def room_1_feature_handler(current_room, verb, feature):
    """Handles verb commands related to room 1 features.

    Args:
        current_room (:obj:Room): The current room the player is in.
        verb (str): The action the user would like to take.
        feature (str): The feature in this room the user would like to act on.

    """

    # Dictionary of feature name mapped to a description of that feature.
    feature_dict = current_room.get_features()

    # Handle feature interaction for each of the 10 main verbs.
    if verb == "take":
        if feature == "body":
            print("This body is too heavy to carry.")

        if feature == "cloak":
            print("The cloak is in tatters, better to leave it I think.")

        if feature == "bag":
            print("This bag has holes in it. Better to leave it I think.")

        if feature == "door":
            print("Hmm let's see, if I unbolt the doors and go get about "
                  "10 other villagers to help me carry them...on second "
                  "thought maybe I should leave the doors where they are.")

    elif verb == "use":
        print("I can't use that. Better move on or find something I can "
              "use.")

    elif verb == "drop":
        print("Drop what? I'm not carrying that.")

    elif verb == "look at":
        print("You take a close look at the {}".format(feature))

        print(feature_dict[feature])

    elif verb == "eat":
        if feature == "body":
            print("Eat this? I don't think so. I'm not a zombie.")

        if feature == "door":
            print("You naw on the oak doors a bit. Yup that's oak all "
                  "right...")

        if feature == "cloak":
            print("You chew on the old cloak a bit and think to yourself "
                  "I better start coming up with some reasonable things "
                  "to do or I'll never rescue Evelyn.")

        if feature == "bag":
            print("You chew on the old bag a bit and think to yourself "
                  "I better start coming up with some reasonable things "
                  "to do or I'll never rescue Evelyn.")

    elif verb == "drink":
        print("I can't drink that.")

    elif verb == "smell":
        if feature == "door":
            print("Smells like oak.")

        else:
            print("The smell is foul. This has been here a while.")

    elif verb == "listen to":
        print("You hear the sounds of the wind rustling the leaves of the "
              "nearby trees.")

    elif verb == "climb":
        print("There's nothing to climb.")

    elif verb == "duck":
        print("You duck quickly and then stand back up.")

    save_object_state(current_room)


def room_2_feature_handler(current_room, verb, feature):
    """Handle room 2 player and feature interaction.

    Args:
        current_room (:obj:Room): The current room the player is in.
        verb (str): The action the user would like to take.
        feature (str): The feature in this room the user would like to act on.

    """
    # A dictionary that maps feature name to a description of that feature.
    feature_dict = current_room.get_features()

    # Handle custom feature interaction for each of the 10 core verbs.
    if verb == "take":
        if feature == "rubble":
            print("The pieces of rubble are to heavy to carry.")

        if feature == "door":
            print("Hmm let's see, if I unbolt the doors and go get about "
                  "10 other villagers to help me carry them...on second "
                  "thought maybe I should leave the doors where they are.")

        else:
            print("I can't take that.")

    elif verb == "use":
        print("I can't use that. Better move on or find something I can "
              "use.")

    elif verb == "drop":
        print("Drop what? I'm not carrying that.")

    elif verb == "look at":
        # Trigger to add rope to feature list. The command use sword will
        # eliminate the rope trap after the feature is discovered.
        if feature == "rubble":
            print("You take a close look at the {}".format(feature))

            print(feature_dict[feature])

            # Add the rope feature so that it can be acted upon by the user.
            if current_room.get_puzzle_status("rope"):
                rope_feature = ("The rope is taut, and looks as though it is "
                                "meant to trip someone walking toward the "
                                "inner door.")

                current_room.add_feature("rope", rope_feature)

                # The rope puzzle has been triggered and should now be set to
                # false. This tracks puzzle status.
                current_room.set_puzzle_status("rope", False)

        if feature == "rope":
            print("You take a close look at the {}".format(feature))

            print(feature_dict[feature])

        # If the user has not entered: use sword after the rope feature has
        # been added to the room, then going to inspect the writing triggers
        # a trap that will damage them.
        if feature == "writing":
            if (current_room.get_puzzle_status("rope") or
               "rope" in current_room.get_features()):

                print("You walk toward the door to inspect the writing.")

                rope_trap(current_room)

            # If the trap has already been triggered then the player can
            # inspect the writing as normal.
            else:
                print("You take a close look at the {}".format(feature))

                print(feature_dict[feature])

    elif verb == "eat":
        if feature == "rubble":
            print("You take a bite of some rubble and break a tooth. Ouch!")

        if feature == "door":
            print("You naw on the oak doors a bit. Yup that's oak all "
                  "right...")

        if feature == "writing":
            print("You can't eat writing, that's silly.")

    elif verb == "drink":
        print("I can't drink that.")

    elif verb == "smell":
        if feature == "door":
            print("Smells like oak.")

        if feature == "writing":
            print("The writing smells foul.")

        if feature == "rubble":
            print("Ahh nothing like the smell of some good rubble.")

    elif verb == "listen to":
        print("All quite...too quite.")

    elif verb == "climb":
        if feature == "rubble":
            print("You climb on top of a pile of rubble. Congrats you're king "
                  "of rubble mountain.")

    elif verb == "duck":
        print("You duck quickly and then stand back up.")

    save_object_state(current_room)


def rope_trap(current_room):
    """Handles rope trap event for room 2.

    Args:
        current_room (:obj:Room): The room the player is currently in.

    """
    print("As you walk toward the door, between the scattered rubble, "
          "your foot trips on a small hard to see rope. You here a "
          "click...\n")

    # Get user response for this mini event.
    print("What would you like to do?")

    response = input("Type some text: ")
    response.lower().strip()
    print("")

    # The only valid response to avoid damage is to duck.
    if "duck" in response:
        print("You duck just as a crossbow bolt passes over head. "
              "A narrow miss. I should probably inspect rooms more "
              "closely in the future.")
    else:
        print("Before you can do anything a crossbow bolt flies "
              "across the room from a hidden opening and strikes "
              "you in the shoulder. Ouch should have ducked.")

    # Set the puzzle status to false to indicate that the rope trap event is
    # complete.
    current_room.set_puzzle_status("rope", False)

    # The feature is removed from the room so that the event does not repeat.
    current_room.remove_feature("rope")

    save_object_state(current_room)


def room_3_feature_handler(current_room, verb, feature):
    """Handles verb commands related to room 3 features.

    Args:
        current_room (:obj:Room): The current room the player is in.
        verb (str): The action the user would like to take.
        feature (str): The feature in this room the user would like to act on.

    """
    # Dictionary of feature name mapped to a description of that feature.
    feature_dict = current_room.get_features()

    # Handle feature interaction for each of the 10 main verbs.
    if verb == "take":
        if feature == "engraving":
            print("You place both hands on the edge of the graving and pull "
                  "with all your might. It doesn't budge.")

        if feature == "armor":
            print("The armor is too heavy to take.")

    elif verb == "use":
        print("I can't use that. Better move on or find something I can "
              "use.")

    elif verb == "drop":
        print("Drop what? I'm not carrying that.")

    elif verb == "look at":
        print("You take a close look at the {}".format(feature))

        print(feature_dict[feature])

    elif verb == "eat":
        print("I can't eat that.")

    elif verb == "drink":
        print("I can't drink that.")

    elif verb == "smell":
        if feature == "engraving":
            print("The engaving doesn't smell like anything.")

        if feature == "armor":
            print("Smells dusty.")

    elif verb == "listen to":
        if feature == "armor":
            print("You put your ear up to one of the suits of armor. Inside "
                  "your hear a mouse scurrying.")

        if feature == "engraving":
            print("You put your ear up to the engraving. You hear nothing.")

    elif verb == "climb":
        if feature == "armor":
            print("You start climbing one of the armor statues. As climb "
                  "the armor tips and comes crashing to the floor. Good that "
                  "should wake up the entire fortress...")
        else:
            print("I can't climb that")

    elif verb == "duck":
        print("You duck quickly and then stand back up.")

    elif verb == "rotate":
        if (feature == "engraving" and
           current_room.get_puzzle_status("engraving")):
            print("You place both hands on the engraving edges and rotate "
                  "with all your might. It slowy turns until the markings "
                  "have been flipped. You hear a click and step back to take "
                  "a look."
                  " .")
            new_desc = ("The rotated engraving...\n"
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
                        "              \\ _______ /              \n")
            print(new_desc)
            print("\nThe door is now open...")
            current_room.unlock("north")
            current_room.set_puzzle_status("engraving", False)
            current_room.remove_feature("engraving")
            current_room.add_feature("engraving", new_desc)
        else:
            print("The engraving can no longer be rotated.")

    save_object_state(current_room)


def room_4_feature_handler(current_room, verb, feature):
    """Handle room 4 player and feature interaction.

    Args:
        current_room (:obj:Room): The current room the player is in.
        verb (str): The action the user would like to take.
        feature (str): The feature in this room the user would like to act on.

    """
    # A dictionary that maps feature name to a description of that feature.
    feature_dict = current_room.get_features()

    # Handle custom feature interaction for each of the 10 core verbs.
    if verb == "take":
        if feature == "broom":
            print("You try and grab the broom, but it evades your grasp. It "
                  "flies around the room a bit more and then settles in the "
                  "corner.")

        elif feature == "vines":
            print("You pull at the vines but they do not move.")

        elif feature == "carcass":
            print("I don't think so, this carcass is way to heavy.")

        elif feature == "lock box":
            print("I'm not sure that I need a box. I already have a bag.")

        else:
            print("I can't take that.")

    elif verb == "use":
        print("I can't use that. Better move on or find something I can "
              "use.")

    elif verb == "drop":
        print("Drop what? I'm not carrying that.")

    elif verb == "look at":
        if feature == "shelves" and current_room.get_puzzle_status("shelves"):
            current_room.set_puzzle_status("lock box", True)
            current_room.set_puzzle_status("shelves", False)

            print("You take a close look at the {}".format(feature))

            print(feature_dict[feature])
        else:
            print("You take a close look at the {}".format(feature))

            print(feature_dict[feature])

    elif verb == "eat":
        if feature == "broom":
            print("You try to take bite the broom. It flies behind you and "
                  "wacks you on the back of the head. Ouch!")

        elif feature == "vines":
            print("You naw on the vines to no effect. They won't budge, and "
                  "they taste disgusting!")

        elif feature == "shelves":
            print("What's with you and trying to eat furniture?")

        elif feature == "carcass":
            print("What are you a wild animal? This isn't cooked.")

        else:
            print("I can't eat that.")

    elif verb == "drink":
        print("I can't drink that.")

    elif verb == "smell":
        if feature == "vines":
            print("The vines smell like nothing.")

        if feature == "broom":
            print("You go to smell the broom. It flies up and hits you in "
                  "face. Ouch!")

        if feature == "shelves":
            print("They smell dusty.")

        if feature == "carcass":
            print("Smells like meat.")

    elif verb == "listen to":
        print("Not much to hear. Nothing happening really.")

    elif verb == "climb":
        if feature == "shelves":
            print("You start climbing the shelves, but before you get too "
                  "far up them the broom flies over and pokes you until you "
                  "stop.")

        else:
            print("I can't climb that.")

    elif verb == "duck":
        print("You duck quickly and then stand back up.")

    save_object_state(current_room)


def room_5_feature_handler(current_room, verb, feature):
    """Handle room 5 player and feature interaction.

    Args:
        current_room (:obj:Room): The current room the player is in.
        verb (str): The action the user would like to take.
        feature (str): The feature in this room the user would like to act on.

    """
    # A dictionary that maps feature name to a description of that feature.
    feature_dict = current_room.get_features()

    # Handle custom feature interaction for each of the 10 core verbs.
    if verb == "take":
        if feature == "fish":
            print("I wouldn't take that. Just touching that fish is probably "
                  "a health risk.")

        elif feature == "sink":
            print("You know when people say \"He took everything but the "
                  "kitchen sink!\" Well there's good reason. It's heavy and "
                  "attached to the wall. So unless you're gonna drop this "
                  "whole rescue mission and take up plumbing I would say no, "
                  "no you cannot take the kitchen sink.")

        else:
            print("I can't take that.")

    elif verb == "use":
        print("I can't use that. Better move on or find something I can "
              "use.")

    elif verb == "drop":
        print("Drop what? I'm not carrying that.")

    elif verb == "look at":
        print("You take a close look at the {}".format(feature))

        print(feature_dict[feature])

    elif verb == "eat":
        if feature == "fish":
            print("You take a bite of the fish and immediately regret it.")

        else:
            print("I can't eat that.")

    elif verb == "drink":
        print("I can't drink that.")

    elif verb == "smell":
        print("Smells rancid.")

    elif verb == "listen to":
        print("Not much to hear. Nothing happening really.")

    elif verb == "climb":
        print("I can't climb that.")

    elif verb == "duck":
        print("You duck quickly and then stand back up.")

    save_object_state(current_room)


def room_6_feature_handler(current_room, verb, feature):
    """Handle room 6 player and feature interaction.

    Args:
        current_room (:obj:Room): The current room the player is in.
        verb (str): The action the user would like to take.
        feature (str): The feature in this room the user would like to act on.

    """
    # A dictionary that maps feature name to a description of that feature.
    feature_dict = current_room.get_features()

    # Handle custom feature interaction for each of the 10 core verbs.
    if verb == "take":
        if feature == "tub":
            print("Do we have forklifts in this game? No, I don't think so."
                  "That's gonna be a hard no on taking this tub.")

        else:
            print("I can't take that.")

    elif verb == "use":
        print("I can't use that. Better move on or find something I can "
              "use.")

    elif verb == "drop":
        print("Drop what? I'm not carrying that.")

    elif verb == "look at":
        if feature == "tub":
            print("You take a close look at the {}".format(feature))

            print(feature_dict[feature])

            if current_room.get_puzzle_status("rubber duck"):
                print("You also notice, resting at the bottom of the "
                      "tub, is a little yellow rubber duck. On its side "
                      "written in black ink it says \"Quackers\"")

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
            print("You take a close look at the {}".format(feature))

            print(feature_dict[feature])

    elif verb == "eat":
        print("I can't eat that.")

    elif verb == "drink":
        if feature == "tub":
            print("No water left in the tub to drink.")

        if feature == "fountain":
            print("You go over to the fountain, lean over, and take a drink "
                  "of the purple liquid. Tastes like soap. You hiccup and "
                  "a soap bubble pops out of your mouth.")

    elif verb == "smell":
        print("Smells soapy.")

    elif verb == "listen to":
        if feature == "fountain":
            print("You listen to the tranquil sound of the fountain. How zen.")

        if feature == "tub":
            print("Water gurgles a bit in the drain.")

    elif verb == "climb":
        if feature == "fountain":
            print("You start climbing the fountain. Your foot slips and lands "
                  "in the purple liquid. You now have a soggy foot, congrats.")

        if feature == "tub":
            print("You climb over the edge and sit in the tub for a bit. "
                  "Nothing like sitting in an empty tub for a bit to "
                  "motivate you when you're on a rescue mission...")

    elif verb == "duck":
        print("You duck quickly and then stand back up.")

    save_object_state(current_room)


def room_7_feature_handler(current_room, verb, feature):
    """Handle room 7 player and feature interaction.

    Args:
        current_room (:obj:Room): The current room the player is in.
        verb (str): The action the user would like to take.
        feature (str): The feature in this room the user would like to act on.

    """
    # A dictionary that maps feature name to a description of that feature.
    feature_dict = current_room.get_features()

    # Handle custom feature interaction for each of the 10 core verbs.
    if verb == "take":
        if feature == "humidor":
            print("You attempt to take the humidor, however, it is bolted to "
                  "the wall.")

        elif feature == "ash tray":
            print("There are still some embers, I better not grab those or "
                  "I might get burned.")

        elif feature == "smoke":
            print("You tray and grab the smokey figure but your hand passes "
                  "through. The figure quickly reforms and continues looking "
                  "at you expectantly.")

    elif verb == "use":
        print("I can't use that. Better move on or find something I can "
              "use.")

    elif verb == "drop":
        print("Drop what? I'm not carrying that.")

    elif verb == "look at":
        if (feature == "humidor" and
           not current_room.get_puzzle_status("smoke")):

            current_room.set_puzzle_status("smoke", True)

            ash_feature = ("The heat from looking at the humidor has brought "
                           "some of the embers in the ash tray back to life. "
                           "Some peculiar smoke patterns start to appear.")

            smoke_feature = ("A wisp of smoke turns into a small humanoid "
                             "shape. You feel as though it is looking "
                             "expectantly at you.")

            current_room.remove_feature("ash tray")

            current_room.add_feature("ash tray", ash_feature)

            current_room.add_feature("smoke", smoke_feature)

            print("You take a close look at the {}".format(feature))

            print(feature_dict[feature])

        else:
            print("You take a close look at the {}".format(feature))

            print(feature_dict[feature])

    elif verb == "eat":
        print("I can't eat that.")

    elif verb == "drink":
        print("I can't drink that.")

    elif verb == "smell":
        print("Smells smokey.")

    elif verb == "listen to":
        print("All is quite.")

    elif verb == "climb":
        print("I can't climb that.")

    elif verb == "duck":
        print("You duck quickly and then stand back up.")

    save_object_state(current_room)


def room_8_feature_handler(current_room, verb, feature):
    """Handle room 8 player and feature interaction.

    Args:
        current_room (:obj:Room): The current room the player is in.
        verb (str): The action the user would like to take.
        feature (str): The feature in this room the user would like to act on.

    """
    # A dictionary that maps feature name to a description of that feature.
    feature_dict = current_room.get_features()

    # Handle custom feature interaction for each of the 10 core verbs.
    if verb == "take":
        if feature == "box":
            print("As you reach out to take the emerald box a small flash "
                  "of green lightning arcs from it and shocks you. I better "
                  "leave this box where it is.")
        else:
            print("I can't take that.")

    elif verb == "use":
        print("I can't use that. Better move on or find something I can "
              "use.")

    elif verb == "drop":
        print("Drop what? I'm not carrying that.")

    elif verb == "look at":
        print("You take a close look at the {}".format(feature))

        print(feature_dict[feature])

    elif verb == "eat":
        print("I can't eat that.")

    elif verb == "drink":
        print("I can't drink that.")

    elif verb == "smell":
        if feature == "bed":
            print("Smell the bed? No thanks, this is getting a little too "
                  "weird.")
        else:
            print("Doesn't smell like much.")

    elif verb == "listen to":
        print("I don't hear much.")

    elif verb == "climb":
        if feature == "bed":
            print("You climb on the bed and start jumping up and down. Wooo "
                  "what fun.")

        else:
            print("I can't climb that.")

    elif verb == "duck":
        print("You duck quickly and then stand back up.")

    save_object_state(current_room)


def room_9_feature_handler(current_room, verb, feature):
    """Handle room 9, supplies closet, player and feature interaction.

    Args:
        current_room (:obj:Room): The current room the player is in.
        verb (str): The action the user would like to take.
        feature (str): The feature in this room the user would like to act on.

    """
    # A dictionary that maps feature name to a description of that feature.
    feature_dict = current_room.get_features()

    # Handle custom feature interaction for each of the 10 core verbs.
    if verb == "take":
        if feature == "towel":
            print("You reach out to grab a towel. The towel quickly rises up "
                  "and raps around your face. As you try to remove it, two "
                  "other towels proceed to roll up and start whipping you. "
                  "Eventually the towels fly away leaving you feeling rather "
                  "embarrassed.")
        if feature == "shampoo":
            print(feature_dict[feature])

    elif verb == "use":
        print("I can't use that. Better move on or find something I can "
              "use.")

    elif verb == "drop":
        print("Drop what? I'm not carrying that.")

    elif verb == "look at":
        print("You take a close look at the {}".format(feature))

        print(feature_dict[feature])

    elif verb == "eat":
        if feature == "towel":
            print("You try and eat one of the towels, but it flies away, "
                  "avoiding your grasp. You get the sense that the objects "
                  "in the supplies closet are looking at you like you're a "
                  "maniac.")

        if feature == "shampoo":
            print("Does your mouth have hair in it? No? Then why are you "
                  "trying to put shampoo in it.")

    elif verb == "drink":
        if feature == "shampoo":
            print("Does your mouth have hair in it? No? Then why are you "
                  "trying to put shampoo in it.")

        else:
            print("I can't drink that.")

    elif verb == "smell":
        if feature == "towel":
            print("The towels have the unmistakable smell of goblin.")

        elif feature == "shampoo":
            print("Smells like lavender.")

    elif verb == "listen to":
        print("I don't hear much.")

    elif verb == "climb":
        if (feature == "shelves" and
           current_room.get_puzzle_status("shelves")):
            print("You climb the shelves to what is causing the blue glow. As "
                  "you reach the top you find that the blue glow is caused "
                  "by a long thin rapier.")

            rapier_name = "rapier"
            rapier_description = ("A thin and nimble long sword. The blade "
                                  "glows blue and it is razor sharp. ")
            rapier_durability = None
            rapier_stats = {"attack_power": 5}

            rapier = Item(rapier_name, rapier_description, rapier_durability,
                          rapier_stats)

            player.add_item(rapier)

            shelves_feature = ("They contain mostly towels. Nothing of note.")

            current_room.remove_feature("shelves")

            current_room.add_feature("shelves", shelves_description)

    elif verb == "duck":
        print("You duck quickly and then stand back up.")

    save_object_state(current_room)


def room_10_feature_handler(current_room, verb, feature):
    """Handle room 10 player and feature interaction.

    Args:
        current_room (:obj:Room): The current room the player is in.
        verb (str): The action the user would like to take.
        feature (str): The feature in this room the user would like to act on.

    """
    # A dictionary that maps feature name to a description of that feature.
    feature_dict = current_room.get_features()

    # Handle custom feature interaction for each of the 10 core verbs.
    if verb == "take":
        print("I can't take that.")

    elif verb == "use":
        print("I can't use that. Better move on or find something I can "
              "use.")

    elif verb == "drop":
        print("Drop what? I'm not carrying that.")

    elif verb == "look at":
        print("You take a close look at the {}".format(feature))

        print(feature_dict[feature])

    elif verb == "eat":
        print("I can't eat that.")

    elif verb == "drink":
        print("I can't drink that.")

    elif verb == "smell":
        print("Doesn't smell like much.")

    elif verb == "listen to":
        print("I don't hear much.")

    elif verb == "climb":
        print("I can't climb that.")

    elif verb == "duck":
        print("You duck quickly and then stand back up.")

    save_object_state(current_room)
