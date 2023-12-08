import pygame


def boundary_top(screen):
    boundary_x = 465
    boundary_y = -5  # Set the top of the boundary
    boundary_height = 193
    boundary_length = 1

    border = pygame.Rect(boundary_x, boundary_y, boundary_length, boundary_height)  # Set the width to 1 for a vertical
    # line

    pygame.draw.rect(screen, (144, 238, 144), border)

    return border


def boundary_middle(screen):
    boundary_x = 465
    boundary_y = 253  # Set the top of the boundary
    boundary_height = 380
    boundary_length = 1

    border = pygame.Rect(boundary_x, boundary_y, boundary_length,
                         boundary_height)  # Set the width to 1 for a vertical line

    pygame.draw.rect(screen, (144, 238, 144), border)

    return border


def boundary_bottom(screen):
    boundary_x = 465
    boundary_y = 693  # Set the top of the boundary
    boundary_height = 234
    boundary_length = 1

    border = pygame.Rect(boundary_x, boundary_y, boundary_length,
                         boundary_height)  # Set the width to 1 for a vertical line

    pygame.draw.rect(screen, (144, 238, 144), border)

    return border


def boundary_left(screen):
    boundary_x = -8
    boundary_y = 460
    boundary_length = 676
    boundary_height = 1

    border = pygame.Rect(boundary_x, boundary_y, boundary_length, boundary_height)

    pygame.draw.rect(screen, (144, 238, 144), border)

    return border


def boundary_right(screen):
    boundary_x = 728
    boundary_y = 460
    boundary_length = 616
    boundary_height = 1

    border = pygame.Rect(boundary_x, boundary_y, boundary_length, boundary_height)

    pygame.draw.rect(screen, (144, 238, 144), border)

    return border


def check_and_adjust_collision(player, boundary_rect, left, right, up, down):
    if player.colliderect(boundary_rect):
        # Adjust the player's position to prevent crossing the boundary
        if left:
            player.left = boundary_rect.right
        elif right:
            player.right = boundary_rect.left
        elif up:
            player.top = boundary_rect.bottom
        elif down:
            player.bottom = boundary_rect.top

# def main():
#     pass
#
#
# if __name__ + "__main__":
#     main()
