"""
Pikachu's Adventure
Edro Gonzales A01257468
Ian Chan A00910012
"""
import os
import sys
from game.game_gui import game_gui
from utils.get_name import get_name
from utils.user_has_file import user_has_file
from utils.generate_character_info import generate_character_info

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

def main():
    try:
        trainer_name = get_name()
    except ValueError as e:
        print("Invalid Input: {}\nExiting by returning None".format(e), file=sys.stderr)
        return None
    else:
        user_has_profile = user_has_file(trainer_name)
        character_info = {}
        if not user_has_profile:
            character_info = generate_character_info(trainer_name)
        elif user_has_profile:
            # add get character info
            pass
        game_gui(character_info)


if __name__ == '__main__':
    main()