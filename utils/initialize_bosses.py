def has_enough_keys(character_info, current_boss):
    if character_info["keys"] >= current_boss["keys_required"]:
        return True


def initialize_bosses():
    """
    Initializes bosses.

    :postcondition: initializes a tuple of bosses and their information in dictionaries
    :return: tuple of bosses and their information
    """
    first_boss = {
        "enemy_type": "boss",
        "name": "Trainer Edro Gonzales",
        "health": 100,
        "coordinates": [
            446, 253
        ],
        "skill": "Splash",
        "pokemon_name": "Magikarp",
        "attack_power": 10,
        "agility": 10,
        "keys_required": 3,
        "experience_award": 500
    }

    second_boss = {
        "enemy_type": "boss",
        "name": "Trainer Ian Chan",
        "health": 100,
        "coordinates": [
            446, 253
        ],
        "skill": "Quick Attack",
        "pokemon_name": "Rattata",
        "attack_power": 20,
        "agility": 20,
        "keys_required": 6,
        "experience_award": 500
    }

    third_boss = {
        "enemy_type": "boss",
        "name": "Trainer Richard M",
        "health": 100,
        "coordinates": [
            446, 253
        ],
        "skill": "Hyper Beam",
        "pokemon_name": "Dragonite",
        "attack_power": 30,
        "agility": 30,
        "keys_required": 9,
        "experience_award": 500
    }

    fourth_boss = {
        "enemy_type": "boss",
        "name": "Trainer Chris Thompson",
        "health": 100,
        "coordinates": [
            446, 253
        ],
        "skill": "Beard Beam",
        "pokemon_name": "Raichu",
        "attack_power": 40,
        "agility": 40,
        "keys_required": 9,
        "experience_award": 500
    }

    return first_boss, second_boss, third_boss, fourth_boss
