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


def battle(screen, character, enemy):
    player_hp = character["health"]
    enemy_hp = enemy["health"]
    font = pygame.font.Font(None, 36)
    player_skill = character["skill"]

    while True:
        screen.fill((0, 0, 0))
        display_fight_or_flee(screen, f"Choose 1 to use {player_skill} or 2 to flee")
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    player_damage = character["attack_power"]
                    enemy_hp -= player_damage

                    attack_message = f"You used {player_skill} and the enemy lost {player_damage} HP"
                    text = font.render(attack_message, True, (255, 255, 255))
                    screen.blit(text, (10, 10))
                    pygame.display.update()

                    pygame.time.delay(1000)

                    if enemy_hp <= 0:
                        screen.fill((0, 0, 0))
                        win_message = f"You won the battle!!"
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

                    pygame.time.delay(1000)

                    if player_hp <= 0:
                        screen.fill((0, 0, 0))
                        lost_message = f"You lost the battle. Game over."
                        text = font.render(lost_message, True, (255, 255, 255))
                        screen.blit(text, (10, 50))
                        pygame.display.update()
                        pygame.time.delay(1000)
                        sys.exit()

                elif event.key == pygame.K_2:
                    screen.fill((0, 0, 0))
                    flee_message = "You have fled the battle!"
                    text = font.render(flee_message, True, (255, 255, 255))
                    screen.blit(text, (10, 50))
                    pygame.display.update()
                    pygame.time.delay(1000)
                    return


def main():
    pass


if __name__ + "__main__":
    main()
