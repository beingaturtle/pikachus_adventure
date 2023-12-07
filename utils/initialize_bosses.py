# character_info = {
#     "name": "hi",
#     "health": 100,
#     "coordinates": (2, 1),
#     "skill": "tackle",
#     "attack_power": 10,
#     "agility": 10,
#     "keys": 13,
#     "total_experience": 0,
#     "current_boss": 0
# }

def has_enough_keys(character_info, boss_info):
    if character_info["keys"] >= boss_info["required_key"]:
        return True


def initialize_bosses():
    """
    Initializes bosses.

    :postcondition: initializes a list of bosses and their information
    :return: list of bosses and their information
    """
    first_boss = {
        "name": "Trainer Ian Chan",
        "health": 100,
        "coordinates": [
            446, 253
        ],
        "skill": "",
        "attack_power": 10,
        "agility": 10,
        "keys_required": 3,
    }
    second_boss = {
        "name": "Trainer Edro Gonzales",
        "health": 100,
        "coordinates": [
            446, 253
        ],
        "skill": "cross-arms",
        "attack_power": 20,
        "agility": 10,
        "keys_required": 3,
    }
    third_boss = {
        "name": "Grace Hopper",
        "health": 100,
        "coordinates": [
            446, 253
        ],
        "skill": "cross-arms",
        "attack_power": 10,
        "agility": 10,
        "keys_required": 3,
    }
