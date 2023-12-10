"""
Pikachu's Adventure
Edro Gonzales A01257468
Ian Chan A00910012
"""
import sys
import pygame
from pygame import Surface
from utils.add_key_logic import add_key_logic
from utils.update_character_level import update_character_level


def display_fight_or_flee(screen: Surface, message: str) -> None:
    """
    Display the fight or flee message

    :param screen: a pygame screen representing the game screen
    :param message: a string representing the message to display
    :precondition: screen must be a pygame screen representing the game screen
    :precondition: message must be a string representing the message to display
    :postcondition: display the fight or flee message
    """
    pygame.font.init()
    font = pygame.font.Font(None, 36)
    text = font.render(message, True, (255, 255, 255))
    screen.blit(text, (10, 90))
    pygame.display.update()


def display_stats(screen: Surface, character: dict, enemy: dict) -> None:
    """
    Display the stats of the player and the enemy

    :param screen: a screen representing the game screen
    :param character: a dictionary representing the character
    :param enemy: a dictionary representing the enemy
    :precondition: screen must be a screen representing the game screen
    :precondition: character must be a non-empty dictionary representing the character
    :precondition: enemy must be a non-empty dictionary representing the enemy
    :postcondition: display the stats of the player and the enemy
    """
    font = pygame.font.Font(None, 30)
    player_health = character["health"]
    player_level = character["level"]
    player_attack_power = character["attack_power"]
    player_skill = character["skill"]
    player_experience = character["total_experience"]
    enemy_name = enemy["name"]
    enemy_pokemon = enemy["pokemon_name"]
    enemy_health = enemy["health"]
    enemy_attack_power = enemy["attack_power"]
    enemy_skill = enemy["skill"]

    player_stats_lines = [
        "Pikachu Stats:",
        f"Level: {player_level}",
        f"Health: {player_health}",
        f"Attack Power: {player_attack_power}",
        f"Skill: {player_skill}",
        f"Experience: {player_experience}"
    ]

    enemy_stats_lines = [
        f"{enemy_name} Stats:",
        f"Pokemon: {enemy_pokemon}",
        f"Health: {enemy_health}",
        f"Attack Power: {enemy_attack_power}",
        f"Skill: {enemy_skill}"
    ]

    y_position = 500
    x_position_player = 200
    x_position_enemy = 500

    for player_line, enemy_line in zip(player_stats_lines, enemy_stats_lines):
        text_player = font.render(player_line, True, (255, 255, 255))
        screen.blit(text_player, (x_position_player, y_position))

        text_enemy = font.render(enemy_line, True, (255, 255, 255))
        screen.blit(text_enemy, (x_position_enemy, y_position))

        y_position += 25

    pygame.display.update()


def battle(screen: Surface, character: dict, enemy: dict) -> None:
    """
    Battle the enemy with a turn based system, giving the player the option to fight or flee.

    :param screen: a screen representing the game screen
    :param character: a dictionary representing the character
    :param enemy: a dictionary representing the enemy
    :precondition: screen must be a screen representing the game screen
    :precondition: character must be a non-empty dictionary representing the character
    :precondition: enemy must be a non-empty dictionary representing the enemy
    :postcondition: battle the enemy with the option to fight or flee
    """
    player_hp = character["health"]
    enemy_hp = enemy["health"]
    enemy_type = enemy["enemy_type"]
    enemy_experience_award = enemy["experience_award"]
    enemy_name = enemy["pokemon_name"]
    font = pygame.font.Font(None, 36)
    player_skill = character["skill"]

    screen.fill((0, 0, 0))
    while True:
        display_fight_or_flee(screen, f"Choose 1 to use {player_skill} or 2 to flee")
        display_stats(screen, character, enemy)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    player_damage = character["attack_power"]
                    enemy_hp -= player_damage
                    screen.fill((0, 0, 0))
                    attack_message = f"You used {player_skill} and {enemy_name} lost {player_damage} HP"
                    text = font.render(attack_message, True, (255, 255, 255))
                    screen.blit(text, (10, 10))
                    pygame.display.update()
                    screen.fill((0, 0, 0))

                    pygame.time.delay(1500)

                    if enemy_hp <= 0:
                        win_message = f"You won the battle and gained {enemy_experience_award} experience points!"
                        text = font.render(win_message, True, (255, 255, 255))
                        screen.blit(text, (10, 50))
                        if enemy_type == "wild":
                            add_key_logic(screen, character)
                        elif enemy_type == "boss":
                            character["bosses_beaten"] += 1
                        update_character_level(character, enemy_experience_award)
                        pygame.display.update()
                        pygame.time.delay(3000)
                        return

                    enemy_damage = enemy["attack_power"]
                    player_hp -= enemy_damage

                    enemy_attack_message = (f"{enemy_name} attacked back and did {enemy_damage} damage. You lost "
                                            f"{enemy_damage} HP")
                    text = font.render(enemy_attack_message, True, (255, 255, 255))
                    screen.blit(text, (10, 50))
                    pygame.display.update()
                    screen.fill((0, 0, 0))

                    pygame.time.delay(1500)

                    if player_hp <= 0:
                        screen.fill((0, 0, 0))
                        lost_message = f"You lost the battle. Game over."
                        text = font.render(lost_message, True, (255, 255, 255))
                        screen.blit(text, (10, 50))
                        pygame.display.update()
                        pygame.time.delay(1000)
                        sys.exit()

                    character["health"] = player_hp

                elif event.key == pygame.K_2:
                    screen.fill((0, 0, 0))
                    flee_message = "You have fled the battle!"
                    text = font.render(flee_message, True, (255, 255, 255))
                    screen.blit(text, (10, 50))
                    pygame.display.update()
                    pygame.time.delay(1000)
                    return

        enemy["health"] = enemy_hp
        pygame.display.update()
