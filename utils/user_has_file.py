"""
Pikachu's Adventure
Edro Gonzales A01257468
Ian Chan A00910012
"""
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
    saved_directory_path = os.path.join(os.path.dirname(__file__), '..', 'saved')
    file_path = os.path.join(saved_directory_path, f"{name}_info.json")
    return os.path.exists(file_path)
