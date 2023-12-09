"""
ADD A DOCSTRING
"""
import sys
import pygame


def display_fight_or_flee(screen, message):
    pygame.font.init()
    font = pygame.font.Font(None, 36)
    text = font.render(message, True, (255, 255, 255))
    screen.blit(text, (10, 90))
    pygame.display.update()


def display_stats(screen, character, enemy):
    font = pygame.font.Font(None, 30)
    player_health = character["health"]
    player_attack_power = character["attack_power"]
    player_skill = character["skill"]
    enemy_health = enemy["health"]
    enemy_attack_power = enemy["attack_power"]
    enemy_skill = enemy["skill"]

    player_stats_lines = [
        "Player Stats:",
        f"Health: {player_health}",
        f"Attack Power: {player_attack_power}",
        f"Skill: {player_skill}",
        f"Experience: {character['total_experience']}"
    ]

    enemy_stats_lines = [
        "Enemy Stats:",
        f"Health: {enemy_health}",
        f"Attack Power: {enemy_attack_power}",
        f"Skill: {enemy_skill}"
    ]

    y_position = 500

    for line in player_stats_lines:
        text_line = font.render(line, True, (255, 255, 255))
        screen.blit(text_line, (50, y_position))
        y_position += 25

    y_position += 25

    for line in enemy_stats_lines:
        text_line = font.render(line, True, (255, 255, 255))
        screen.blit(text_line, (50, y_position))
        y_position += 25

    pygame.display.update()

def battle(screen, character, enemy):
    player_hp = character["health"]
    player_experience = character["total_experience"]
    enemy_hp = enemy["health"]
    enemy_experience_award = enemy["experience_award"]
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
                    attack_message = f"You used {player_skill} and the enemy lost {player_damage} HP"
                    text = font.render(attack_message, True, (255, 255, 255))
                    screen.blit(text, (10, 10))
                    pygame.display.update()

                    pygame.time.delay(1000)

                    if enemy_hp <= 0:
                        player_experience += enemy_experience_award
                        win_message = f"You won the battle and gained {enemy_experience_award} experience points!"
                        text = font.render(win_message, True, (255, 255, 255))
                        screen.blit(text, (10, 50))
                        pygame.display.update()
                        return

                    enemy_damage = enemy["attack_power"]
                    player_hp -= enemy_damage

                    enemy_attack_message = (f"The enemy attacked back and did {enemy_damage} damage. You lost "
                                            f"{enemy_damage} HP")
                    text = font.render(enemy_attack_message, True, (255, 255, 255))
                    screen.blit(text, (10, 50))
                    pygame.display.update()
                    screen.fill((0, 0, 0))

                    pygame.time.delay(1000)

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


def main():
    pass


if __name__ + "__main__":
    main()
