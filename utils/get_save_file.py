import json
import os

def get_save_file(trainer_name: str) -> dict:
    """
    Grabs json information from saved folder.

    :param trainer_name: string representing the username
    :precondition: trainer_name must be a string representing the username typed by the user
    :postcondition: pulls the json data from the saved folder
    :postcondition: converts the json data into a dictionary
    :return: a dictionary containing game character information
    """
    saved_directory_path = os.path.join(os.path.dirname(__file__), '..', 'saved')
    file_name = os.path.join(saved_directory_path, f"{trainer_name}_info.json")
    with open(file_name) as file_object:
        character_info = json.load(file_object)

    return character_info
