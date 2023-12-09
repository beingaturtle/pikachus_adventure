import random
from itertools import cycle

def create_encounter():
    """
    Creates the enemy encounter information.

    :postcondition: cycles and randomizes the character information
    :postcondition: creates a dictionary with enemy information
    :return: dictionary with enemy information
    """
    enemy_names = cycle(["Magikarp", "Bidoof", "Zubat"])
    power_level = random.choice([("Weak", 5), ("Strong", 15), ("Decent", 12)])
    current_enemy_name = next(enemy_names)
    encounter_enemy = {
        "descriptor": power_level[0],
        "name": current_enemy_name,
        "health": 50,
        "attack_power": power_level[1],
        "experience_award": 100
    }
    return encounter_enemy