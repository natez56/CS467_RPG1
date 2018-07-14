def get_input():
    """Get raw user input."""
    user_input = input("Type some text: ")

    return user_input


def parse_input(user_input):
    """Extract action and thing from user_input."""
    action = []

    action.append('travel')

    action.append('north')

    return action