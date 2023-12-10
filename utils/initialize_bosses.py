"""
Pikachu's Adventure
Edro Gonzales A01257468
Ian Chan A00910012
"""


def has_enough_keys(character_info: dict, current_boss: dict) -> bool:
    """
    Checks if the character has enough keys to fight the boss.

    :param character_info: a non-empty dictionary containing the character's information
    :param current_boss: a non-empty dictionary containing the boss' information
    :precondition: character_info must be a non-empty dictionary containing the character's information
    :precondition: current_boss must be a non-empty dictionary containing the boss' information
    :postcondition: checks if the character has enough keys to fight the boss
    :return: a boolean value True if the character has enough keys to fight the boss
    >>> has_enough_keys({"keys": 3}, {"keys_required": 3})
    True

    >>> has_enough_keys({"keys": 2}, {"keys_required": 3})
    False
    """
    if character_info["keys"] >= current_boss["keys_required"]:
        return True


def initialize_bosses() -> tuple:
    """
    Initializes bosses for the game.

    :postcondition: initializes a tuple of bosses and their information in dictionaries
    :return: tuple of bosses and their information
    """
    first_boss = {
        "enemy_type": "boss",
        "name": "Trainer Edro Gonzales",
        "health": 100,
        "coordinates": [
            453, 189
        ],
        "skill": "Splash",
        "pokemon_name": "Magikarp",
        "attack_power": 10,
        "keys_required": 3,
        "experience_award": 500
    }

    second_boss = {
        "enemy_type": "boss",
        "name": "Trainer Ian Chan",
        "health": 100,
        "coordinates": [
            675, 441
        ],
        "skill": "Quick Attack",
        "pokemon_name": "Rattata",
        "attack_power": 20,
        "keys_required": 6,
        "experience_award": 500
    }

    third_boss = {
        "enemy_type": "boss",
        "name": "Trainer Richard M",
        "health": 100,
        "coordinates": [
            434, 633
        ],
        "skill": "Hyper Beam",
        "pokemon_name": "Dragonite",
        "attack_power": 30,
        "keys_required": 9,
        "experience_award": 500
    }

    fourth_boss = {
        "enemy_type": "boss",
        "name": "Trainer Chris Thompson",
        "health": 600,
        "coordinates": [
            14, 861
        ],
        "skill": "Beard Beam",
        "pokemon_name": "Raichu",
        "attack_power": 60,
        "keys_required": 12,
        "experience_award": 500
    }

    return first_boss, second_boss, third_boss, fourth_boss
