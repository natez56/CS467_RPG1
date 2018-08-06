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

        elif feature == "box":
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

            player = current_room.get_player()
            player.add_item(rapier)

            shelves_feature = ("They contain mostly towels. Nothing of note.")

            current_room.remove_feature("shelves")

            current_room.add_feature("shelves", shelves_feature)

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
        if feature == "mirror":
            print("You reach out to take the mirror. Before you can grab "
                  "it a little storm cloud forms in front of your face and "
                  "emits a tiny lightning bolt that shocks you. Ouch! I "
                  "better leave this mirror here.")
        else:
            print("I can't take that.")

    elif verb == "use":
        print("I can't use that. Better move on or find something I can "
              "use.")

    elif verb == "drop":
        print("Drop what? I'm not carrying that.")

    elif verb == "look at":
        if feature == "mirror" and current_room.get_puzzle_status("steam"):
            print("You take a close look at the {}".format(feature))

            print(feature_dict[feature])

            puzzle_result = mirror_puzzle()

            if puzzle_result:
                print("The text in the mirror swirls and changes. It "
                      "reconfigures to say \"Password accepted.\". All the "
                      "sudden you hear the machinery stop. The magic steam "
                      "stops exuding from the vent and the room slowly "
                      "becomes visible.")

                description = ("The room is made of marble. Benches of marble "
                               "line the walls. The magic mirror hangs from "
                               "the left side of the room. To the south is a "
                               "birch door and to the north is a marble "
                               "staircase.",
                               "I am in the sauna room. There is a birch door "
                               "to the south and a marble staircase to the "
                               "north.")

                current_room.set_description(description)

                mirror_feature = ("The message \"Password accepted.\" is "
                                  "still displayed on the mirror surface.")
                current_room.remove_feature("mirror")
                current_room.add_feature("mirror", mirror_feature)

                machinery_feature = ("The sound of machinery has disappeared.")
                current_room.remove_feature("machinery")
                current_room.add_feature("machinery", machinery_feature)

                new_door_map = {'south': False, 'north': False}
                current_room.set_door_map(new_door_map)

                new_adjacent_rooms = {'north': 'tower hall', 'east': None,
                                      'south': 'supplies closet', 'west': None}
                current_room.set_adjacent_rooms(new_adjacent_rooms)
                current_room.set_puzzle_status("steam", False)

                print(current_room.get_description())
            else:
                print("The text on the mirror swirls and reconfigures to say "
                      "\"Password denied!\" A small storm cloud forms in "
                      "front of the mirror and emits a small lightning bolt "
                      "that shocks you. The cloud quickly dissipates and the "
                      "mirror goes blank.")
        else:
            print("You take a close look at the {}".format(feature))

            print(feature_dict[feature])

    elif verb == "eat":
        if feature == "mirror":
            print("A thought pops into your head. \"You wouldn't eat a couch "
                  "would you? You wouldn't eat a chair would you? Eating "
                  "mirrors is a crime. This thought has been paid for by the "
                  "national mirror association for the prevention of magic "
                  "mirror related crimes.\"")
        else:
            print("I can't eat that.")

    elif verb == "drink":
        print("I can't drink that.")

    elif verb == "smell":
        print("Doesn't smell like much.")

    elif verb == "listen to":
        if feature == "machinery":
            print(feature_dict[feature])
        else:
            print("I hear nothing.")

    elif verb == "climb":
        print("I can't climb that.")

    elif verb == "duck":
        print("You duck quickly and then stand back up.")

    save_object_state(current_room)


def mirror_puzzle():
    user_input = input("The mirror wants you to say something. What do you "
                       "say? Enter some text: ")

    user_input.lower().strip()

    if user_input == "password":
        return True
    else:
        return False


def room_11_feature_handler(current_room, verb, feature):
    """Handle room 11 player and feature interaction.

    Args:
        current_room (:obj:Room): The current room the player is in.
        verb (str): The action the user would like to take.
        feature (str): The feature in this room the user would like to act on.

    """
    # A dictionary that maps feature name to a description of that feature.
    feature_dict = current_room.get_features()

    # Handle custom feature interaction for each of the 10 core verbs.
    if verb == "take":
        if feature == "ruby":
            print("You reach out to take the ruby. As your hand closes around "
                  "it you feel nothing. The ruby is an illusion. Suddenly "
                  "your hand bursts into flames. You quickly use your bag "
                  "to smother the flames, but not before your hand is badly "
                  "burned.")

        elif feature == "dagger":
            print("You reach out to take the dagger. As your hand gets close "
                  "the dagger morphs into a snake and strikes. Your hand is "
                  "bit. You pull away and the snake turns back into a dagger. "
                  "You feel weaker, the snake may have been poisonous.")

        elif feature == "charcoal":
            print("You take the charcoal. When you do both the ruby and the "
                  "dagger disappear from the table.")

            current_room.remove_feature('ruby')
            current_room.remove_feature('charcoal')
            current_room.remove_feature('dagger')
            current_room.remove_feature('table')

            table_feature = ("The table is now bare. The ruby and dagger "
                             "illusions have disappeared")

            current_room.add_feature('table', table_feature)

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


def room_12_feature_handler(current_room, verb, feature):
    """Handle room 12 player and feature interaction.

    Args:
        current_room (:obj:Room): The current room the player is in.
        verb (str): The action the user would like to take.
        feature (str): The feature in this room the user would like to act on.

    """
    # A dictionary that maps feature name to a description of that feature.
    feature_dict = current_room.get_features()

    # Handle custom feature interaction for each of the 10 core verbs.
    if verb == "take":
        if feature == "chandelier":
            print("Maybe if you can find a ladder you can make an attempt. "
                  "Until then better leave the chandelier where it is.")
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
        if feature == "chandelier":
            print("The air under the chandelier smells like rain.")

        elif feature == "fireplace":
            print("A smokey smell emits from the fireplace.")
        else:
            print("Doesn't smell like much.")

    elif verb == "listen to":
        if feature == "fireplace":
            print("You hear the crackle of the fireplace. It reminds you of "
                  "nights at home sitting in front of the hearth. Your "
                  "resolve to rescue Evelyn strengthens.")

        elif feature == "chandelier":
            print("No noise comes from the chandelier.")

    elif verb == "climb":
        if feature == "chandelier":
            print("You start to sing \"I'm gonna swing from the "
                  "chandelieeeer, from the chandelieeer. I'm gonna live like "
                  "tomorrow doesn't exiiiist...\"")
        else:
            print("I can't climb that.")

    elif verb == "duck":
        print("You duck quickly and then stand back up.")

    save_object_state(current_room)


def room_13_feature_handler(current_room, verb, feature):
    """Handle room 13 player and feature interaction.

    Args:
        current_room (:obj:Room): The current room the player is in.
        verb (str): The action the user would like to take.
        feature (str): The feature in this room the user would like to act on.

    """
    # A dictionary that maps feature name to a description of that feature.
    feature_dict = current_room.get_features()

    # Handle custom feature interaction for each of the 10 core verbs.
    if verb == "take":
        if feature == "tome":
            print(feature_dict[feature])

        elif feature == "couch":
            print(feature_dict[feature])

        elif feature == "raven":
            print("The raven's perch is too high to reach.")

    elif verb == "use":
        print("I can't use that. Better move on or find something I can "
              "use.")

    elif verb == "drop":
        print("Drop what? I'm not carrying that.")

    elif verb == "look at":
        if feature == "raven" and current_room.get_puzzle_status("raven"):
            print("You take a close look at the {}".format(feature))

            print(feature_dict[feature])

            if raven_joke():
                print("The raven emits several hearty squawkes that almost "
                      "sound like laughter. It drops the key which clatters "
                      "the floor. For some reason you get the feeling the "
                      "raven doesn't speak english very well...")

                key_name = "cage key"
                key_description = ("A plain iron key.")
                key_durability = 1
                key_stats = None
                key = Item(key_name, key_description, key_durability,
                           key_stats)

                current_room.add_item(key)
                current_room.set_puzzle_status("raven", False)

                new_raven = ("He has dark black feathers. Engraved at the "
                             "base of its perch is the name Artemis. The "
                             "raven is carrying nothing currently. He "
                             "doesn't seem to be paying attention to you "
                             "anymore.")

                current_room.remove_feature("raven")
                current_room.add_feature("raven", new_raven)
            else:
                print("Hmm well that didn't lead to anything.")

        else:
            print("You take a close look at the {}".format(feature))

            print(feature_dict[feature])

    elif verb == "eat":
        if feature == "tome":
            print("You step closer to the tome with the intent to tear a "
                  "page off and eat it. As you near The book suddenly becomes "
                  "surrounded by a raging inferno of flames. You can feel the "
                  "heat. As you take a step back the flames subside leaving "
                  "the book unharmed.")

        if feature == "couch":
            print(feature_dict[feature])

        if feature == "raven":
            print("In your mind a picture of a nice cooked pheasant replaces "
                  "the image of the raven. You look at the raven high up "
                  "on its perch and start to drool.")

    elif verb == "drink":
        print("I can't drink that.")

    elif verb == "smell":
        if feature == "tome":
            print("You smell the air near the tome. It smells strange, as do "
                  "most highly magical items.")

        elif feature == "couch":
            print("Every time you get remotely close to the couch it starts "
                  "sinking into the ground. Guess I'll have to find something "
                  "else to smell.")

        elif feature == "raven":
            print("You walk over to the area under where the birds perch is. "
                  "You start sniffing the air. The bird looks at you with a "
                  "somewhat alarmed expression on its face.")

    elif verb == "listen to":
        if feature == "tome":
            print("You step closer to the tome and listen. You hear the faint "
                  "sound of writing. As you look at the current page you see "
                  "that words are appearing out of nowhere. They are in a "
                  "language you have never seen before.")

        if feature == "couch":
            print("Not much sound coming from the couch, even when it's "
                  "sinking into the ground...")

        if feature == "raven":
            print("You listen for any sounds coming from the raven. It stands "
                  "on its perch and looks at you silently.")

    elif verb == "climb":
        if feature == "couch":
            print("You've had enough. You step back and take a running leap "
                  "try and climb onto the couch before it disappears. Just as "
                  "you almost touch it, it sinks the last couple inches into "
                  "the ground and you faceplant onto the hard stone floor. "
                  "Ouch!")

        elif feature == "tome":
            print(feature_dict[feature])

        elif feature == "raven":
            print("The raven's perch hangs from the ceiling and is not "
                  "reachable from the ground.")

    elif verb == "duck":
        print("You duck quickly and then stand back up.")

    save_object_state(current_room)


def raven_joke():
    print("You get the feeling that the raven is expecting you to say "
          "something.")

    user_input = input("Words you would like to say to raven: ")

    user_input.lower().strip()

    if user_input == "knock knock":
        print("The raven looks intently at you. You suddenly hear a voice in "
              "your mind say \"Who's there?\"")

        user_input = input("Next words to the raven: ")

        print("You hear a voice in you mind say \"{} who?\"")

        user_input = input("Next words to the raven: ")

        return True
    else:
        print("The raven looks away from you. You suddenly hear a voice in "
              "your mind say \"That's not how the joke starts.\"")

        return False


def room_14_feature_handler(current_room, verb, feature):
    """Handle room 14 player and feature interaction.

    Args:
        current_room (:obj:Room): The current room the player is in.
        verb (str): The action the user would like to take.
        feature (str): The feature in this room the user would like to act on.

    """
    # A dictionary that maps feature name to a description of that feature.
    feature_dict = current_room.get_features()

    # Handle custom feature interaction for each of the 10 core verbs.
    if verb == "take":
        if feature == "bones":
            print("Take the bones? Are you a troll? That's what trolls do, "
                  "they collect bones. Lets maybe stick to picking up useful "
                  "items...")

        elif feature == "handprint":
            print("You can't take a handprint...")

        elif feature == "cage":
            print("The cage is firmly attached to the ceiling by a long "
                  "chain. I can't take this.")

        elif feature == "fairy":
            print("The bars of the cage are too narrow for you to reach "
                  "through and grab the fairy.")

    elif verb == "use":
        print("I can't use that. Better move on or find something I can "
              "use.")

    elif verb == "drop":
        print("Drop what? I'm not carrying that.")

    elif verb == "look at":
        if feature == "cage" and current_room.get_puzzle_status("cage"):
            print("You take a close look at the {}".format(feature))

            print(feature_dict[feature])

            fairy_feature = ("She is small and emits a light so bright that "
                             "you can't make out what she looks like.")

            current_room.add_feature("fairy")

            print("As you near you notice a small light glowing near the "
                  "cages' center. You hear a small voice. It says, \"Hey "
                  "you! You're not a Goblin! I can tell by your magic aura. "
                  "Oh thank goodness, please you must help me! I'm a fairy "
                  "from the forest. I was captured and put on display here. "
                  "Please you must get the keys to open this cage. The "
                  "warlock's pet raven has them in the reading room. His name "
                  "is Artemis. To get the keys you must look directly at him. "
                  "After he notices you, you must make him laugh. That is the "
                  "only way to get him to drop the keys. He likes knock knock "
                  "jokes. Maybe try one of those...")
        else:
            print("You take a close look at the {}".format(feature))

            print(feature_dict[feature])

    elif verb == "eat":
        if feature == "bones":
            print("Um I don't think I should do that. Eating bones is what "
                  "the bad guys do...")

        elif feature == "handprint":
            print("You can't eat a handprint.")

        elif feature == "cage" and current_room.get_puzzle_status("cage"):
            print("You gnaw on the bars. The fairy looks at you and says "
                  "\"Um I don't think that's going to work...\"")

        elif feature == "cage":
            print("You gnaw on the bars a bit. Nothing happens.")

        elif feature == "fairy":
            print("They say if you harm a fairy you will be cursed for "
                  "life. I'd much rather look for a way to help her.")

    elif verb == "drink":
        print("I can't drink that.")

    elif verb == "smell":
        if feature == "bones":
            print("The bones smell like death and decay.")

        elif feature == "handprint":
            print("Hmm maybe if I was a bloodhound I could smell something "
                  "useful from this handprint. As it stands I smell nothing.")

        elif feature == "cage" and current_room.get_puzzle_status("cage"):
            print("You start sniffing around the cage. The fairy looks at "
                  "you and says \"Um what are you doing? You're scaring me "
                  "a little...\"")

        elif feature == "fairy":
            print("You start sniffing around the cage. The fairy looks at "
                  "you and says \"Um what are you doing? You're scaring me "
                  "a little...\"")

        else:
            print("You don't smell anything apart from the general smell of "
                  "death and decay present in the room.")

    elif verb == "listen to":
        if feature == "fairy":
            print("You hold your hand to your ear as you look toward the "
                  "fairy. \"What? I already told you what you need to do to "
                  "rescue me. What more do you want me to say?\"")

    elif verb == "climb":
        if feature == "bones":
            print("You climb up on a pile of bones. You get an unsettling "
                  "feeling and decide to climb down.")

        elif feature == "cage" and current_room.get_puzzle_status("cage"):
            print("You grab onto the cage and it starts to swing back and "
                  "forth. The fairy yells \"Stop that! You can't open this "
                  "cage by climbing it you know.\"")

        elif feature == "cage":
            print("You hop in the open cage and sit for a bit. Feels kinda "
                  "cramped. I better climb out before the cage door "
                  "accidentally closes and traps me in here.")

        else:
            print("I can't climb that.")

    elif verb == "duck":
        print("You duck quickly and then stand back up.")

    save_object_state(current_room)


def room_15_feature_handler(current_room, verb, feature):
    """Handle room 15 player and feature interaction.

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
