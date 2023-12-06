import json
import os

def generate_character_info(name: str) -> dict:
    """
    Generates character information.

    :param name: string name of character
    :precondition: name must be a string of characters representing username
    :postcondition: makes a dictionary containing information of character
    :postcondition: saves that dictionary into a JSON file for future use
    :return: dictionary of character information

    >>> generate_character_info("test_user")
    {'name': 'test_user', 'health': 100, 'coordinates': (2, 1), 'skill': 'tackle', 'attack_power': 10, 'defense': 10, 'keys': 0, 'total_experience': 0}

    >>> generate_character_info("xxxxxxxxxx")
    {'name': 'xxxxxxxxxx', 'health': 100, 'coordinates': (2, 1), 'skill': 'tackle', 'attack_power': 10, 'defense': 10, 'keys': 0, 'total_experience': 0}
    """
    character_info = {
        "name": name,
        "health": 100,
        "coordinates": [2, 1],
        "skill": "tackle",
        "attack_power": 10,
        "defense": 10,
        "keys": 0,
        "total_experience": 0,
        "bossesKilled": 0
    }

    saved_directory_path = os.path.join(os.path.dirname(__file__), '..', 'saved')
    file_name = os.path.join(saved_directory_path, f"{name}_info.json")
    with open(file_name, "w") as file:
        json.dump(character_info, file, indent=4)

    return character_info

