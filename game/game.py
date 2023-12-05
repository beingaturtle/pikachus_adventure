"""
Pikachu's Adventure
Edro Gonzales A01257468
Ian Chan A00910012
"""
import sys
from game.game_gui import game_gui
from utils.get_name import get_name
from utils.user_has_file import user_has_file
from utils.generate_character_info import generate_character_info

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