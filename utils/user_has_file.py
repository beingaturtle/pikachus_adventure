import os

def user_has_file(name: str) -> bool:
    """
    Determines if user has a saved file or not.

    :param name: string representing the username
    :precondition: name must be a string representing the username typed by the user
    :postcondition: looks into saved folder and determines if the relevant file exists or not
    :return: True if json file exists or False otherwise

    >>> user_has_file("user_exist")
    True

    >>> user_has_file("user_does_not_exist")
    False
    """
    file_path = os.path.join("../saved", f"{name}_info.json")
    return os.path.exists(file_path)
