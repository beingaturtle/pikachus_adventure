import random
from itertools import cycle

def create_encounter_enemy():
    """
    Creates the enemy encounter information.

    :postcondition: cycles and randomizes the character information
    :postcondition: creates a dictionary with enemy information
    :return: dictionary with enemy information
    """
    enemy_names = cycle(["Magikarp", "Bidoof", "Zubat"])
    skill = cycle(["splash", "tackle", "scream"])
    power_level = random.choice([("Weak", 5), ("Strong", 15), ("Decent", 12)])
    current_enemy_name = next(enemy_names)
    skill = next(skill)
    format_enemy_name = power_level[0] + " " + current_enemy_name
    encounter_enemy = {
        "enemy_type": "wild",
        "pokemon_name": current_enemy_name,
        "name": format_enemy_name,
        "health": 50,
        "attack_power": power_level[1],
        "experience_award": 100,
        "skill": skill
    }
    return encounter_enemy