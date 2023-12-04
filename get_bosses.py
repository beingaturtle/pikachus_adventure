"""
Pikaachu's Adventure
Edro Gonzales A01257468
Ian Chan A00910012
"""
character_info = {
    "name": "hi",
    "health": 100,
    "coordinates": (2, 1),
    "skill": "tackle",
    "attack_power": 10,
    "defense": 10,
    "keys": 13,
    "total_experience": 0,
    # "bosses": [1, 2, 3, 4]
    "current_boss": 0
}

def has_enough_keys(character_info, boss_info):
    if character_info["keys"] >= boss_info["required_key"]:
        return True


def get_bosses(character_info, boss_info):
    """
    Calculate the current boss given the number of keys the character is holding.
    boss_info = {
    "required_key" = 3, 6, 9, 12
    }


    :param character_info:
    :return:
    """

    if character_info["keys"] <= 3 and character_info["current_boss"] == 0:
        current_bosses = character_info["bosses"][0]
    elif character_info["keys"] <= 6:
        current_bosses = character_info["bosses"][1]
    elif character_info["keys"] <= 9:
        current_bosses = character_info["bosses"][2]
    elif character_info["keys"] <= 12:
        current_bosses = character_info["bosses"][3]
    else:
        return

    return current_bosses

print(get_bosses(character_info))



