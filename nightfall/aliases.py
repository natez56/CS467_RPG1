import itertools


def move_alias_check(current_room_name, user_input):
    """Movement alias check.

    Sources used: # https://stackoverflow.com/questions/14264163/search-for-any
    -word-or-combination-of-words-from-one-string-in-a-list-python
    # https://docs.python.org/2/library/itertools.html

    Args:
        current_room_name (str): Name of the room the player is currently in.
        user_input (str): raw user input.

    Returns:
        str: If movement command is valid it will return the name of the room
            that the player wants to travel to. Otherwise it will return the
            user_input just as it was received.

    """
    # Tracks possible destinations so that correct room name can be returned if
    # input is valid.
    possible_destinations = {}

    # Find out what room the player is in currently so that the correct word
    # list can be generated for the rooms connected to that room.
    if current_room_name == 'fortress entrance':
        # Contains both the words in the descriptions of doors and contains
        # variations of the names of rooms.
        dest_list = ([
                      ["large", "oak", "double", "door", "doors"],
                      ["entrance hall", "entrance", "door", "doors"],
                      ])

        # Match the room name to the description words matching that room.
        possible_destinations['entrance hall'] = dest_list

    elif current_room_name == 'entrance hall':
        # Two destination lists are created because two rooms are connected to
        # this room.
        dest_list_1 = ([
              ["large", "oak", "double", "door", "doors"],
              ["fortress entrance", "entrance", "door", "doors"],
              ])

        possible_destinations['fortress entrance'] = dest_list_1

        dest_list_2 = ([
              ["painted", "door", "doors"],
              ["mess hall", "door", "doors"],
              ])

        possible_destinations['mess hall'] = dest_list_2

    # The list of possible move words.
    move_lists = ([
                  ["move", "to"],
                  ["go", "to"],
                  ["travel", "to"],
                  ["leave", "to"],
                  ])

    for key in possible_destinations:
        # List to hold the combinations of both movement commands and 
        # destination variations.
        move_dest_list = []

        # Holds all valid combinations of input
        combination_lists = []

        # The specific destination list for a give room.
        dest_lists = possible_destinations[key]

        # Combine the movement list with each of the possible destination
        # lists.
        for list_obj_1 in move_lists:
            for list_obj_2 in dest_lists:
                move_dest_list.append(list_obj_1 + list_obj_2)

        # Generate all possible combinations of the words that make up the
        # move_dest_list.
        for i, word_list in enumerate(move_dest_list):
            _gen = (itertools.combinations(word_list, i + 1)
                    for i in range(len(word_list)))

            all_combinations_gen = itertools.chain(*_gen)

            combinations = list(all_combinations_gen)

            # Door descriptions require that the word door or doors be in
            # the command to travel to that door.
            if i % 2 == 0:
                # Must have word + door or word + doors
                _gen_valid = (word_tuple for word_tuple in combinations
                              if ((("door" in word_tuple and
                                   "doors" not in word_tuple) or
                                  ("doors" in word_tuple and
                                   "door" not in word_tuple)) and
                                  len(word_tuple) > 1))

            # Room name descriptions must have at least part of the room name
            # in the command. They do not need door to be in the command
            # however.
            else:
                # Must have room name or form of room name
                _gen_valid = (word_tuple for word_tuple in combinations
                              if key in word_tuple or "entrance" in word_tuple)

            # Join all possible combinations into a set of sentences
            # representing the user commands.
            valid_combination = set(' '.join(i) for i in _gen_valid)

            # Add the valid combination sentences to the final list that we
            # are checking against
            combination_lists.append(valid_combination)

        # Check for valid match
        for word_list in combination_lists:
            if user_input in word_list:
                return key

    return user_input


def verb_alias_check(command):
    """Check for aliases of 10 core verbs.

    Args:
        word_list (list(str)): Corresponds to clean_text in text_parser.py 
            file. Contains user input as a list of words.

    Returns:
        str: If an alias matches it returns one of the 10 core verbs the
            game uses. If an alias does not match it returns the unmodified
            word_list as taken from text_parser.py

    """
    alias_dictionary = {}

    # Filled out dictionary for each of the 10 core verbs
    alias_dictionary["take"] = ["grab", "pick up"]
    # alias_dictionary["smell"] = ....

    for key in alias_dictionary:
        for word in alias_dictionary[key]:
            command = command.replace(word, key)

    return command
