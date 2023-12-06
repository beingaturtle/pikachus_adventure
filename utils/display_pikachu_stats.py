# def display_pikachu_stats(character_info: dict) -> None:
#     """
#     Display pikachu's current stats.
#
#     :param character_info: a non-empty dictionary
#     :precondition: character_info must be a non-empty dictionary containing the user character information
#     :postcondition: display pikachu's current stats
#     >>> first_character = {
#     ... "name": "edro",
#     ... "health": 100,
#     ... "coordinates": (2, 1),
#     ... "skill": "tackle",
#     ... "attack_power": 10,
#     ... "defense": 10,
#     ... "keys": 0,
#     ... "total_experience": 0,
#     ... "bosses_beaten": 0
#     ... }
#     >>> display_pikachu_stats(first_character)
#     Pikachu's stats:
#     -----------------------------------------
#     Health: 100
#     Skill: tackle
#     Number of Keys: 0
#     Experience: 0
#     Number of trainers to defeat: 4
#
#     >>> second_character = {
#     ... "name": "ian",
#     ... "health": 50,
#     ... "coordinates": (6, 3),
#     ... "skill": "iron tail",
#     ... "attack_power": 999,
#     ... "defense": 999,
#     ... "keys": 6,
#     ... "total_experience": 89,
#     ... "bosses_beaten": 3
#     ... }
#     >>> display_pikachu_stats(second_character)
#     Pikachu's stats:
#     -----------------------------------------
#     Health: 50
#     Skill: iron tail
#     Number of Keys: 6
#     Experience: 89
#     Number of trainers to defeat: 1
#     """
#
#     print(f"Pikachu's stats:\n"
#           f"-----------------------------------------\n"
#           f"Health: {character_info['health']}\n"
#           f"Skill: {character_info['skill']}\n"
#           f"Number of Keys: {character_info['keys']}\n"
#           f"Experience: {character_info['total_experience']}\n"
#           f"Number of trainers to defeat: {4 - character_info['bosses_beaten']}")
import pygame


def display_pikachu_stats(pygame_screen, player, character_info: dict) -> None:
    """
    Display Pikachu's current stats.

    :param pygame_screen: pygame screen object where the name will be inputted and displayed
    :param player: pygame rect object where the object represents Pikachu's coordinates and size
    :param character_info: a non-empty dictionary
    :precondition: character_info must be a non-empty dictionary containing the user character information
    :postcondition: display Pikachu's current stats
    """
    font = pygame.font.Font(None, 25)
    text = font.render(f"Pikachu's stats:", True, (0, 0, 0))
    pygame_screen.blit(text, (10, 935))

    stats = [
        f"Coordinates: {player.x, player.y}",
        f"Health: {character_info['health']}",
        f"Skill: {character_info['skill']}",
        f"Number of Keys: {character_info['keys']}",
        f"Experience: {character_info['total_experience']}",
        f"Number of trainers to defeat: {4 - character_info['bosses_beaten']}"
    ]

    for index, stat in enumerate(stats):
        stat_text = font.render(stat, True, (0, 0, 0))
        pygame_screen.blit(stat_text, (10, 965 + index * 14))

    pygame.display.update()
