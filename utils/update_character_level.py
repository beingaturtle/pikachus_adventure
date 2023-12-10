def update_character_level(character: dict, experience_reward: int):
    """
    Updates the character level based on the experience reward.

    :param character: dict representing character information
    :param experience_reward: integer representing the winning of experience from the enemy
    :precondition: character is a dictionary representing character stats
    :precondition: experience_reward is a positive integer representing the experience rewarded
    :postcondition: update character experience and level to reflect stats
    :postcondition: based on experience of character, will update the attack power and health
    """
    character["total_experience"] += experience_reward
    new_level = character["total_experience"] // 1000

    if new_level > character["level"]:
        levels_gained = new_level - character["level"]
        character["level"] = new_level

        for _ in range(levels_gained):
            character["attack_power"] *= 1.50
            character["health"] *= 1.50

    if character["level"] == 0:
        character["skill"] = "Tackle"
    elif character["level"] == 1:
        character["skill"] = "Quick Attack"
    elif character["level"] >= 2:
        character["skill"] = "Thunder"