import pygame


def boundary_top(screen):
    """
    Draw the top boundary of the game board.

    :param screen: a pygame object representing the game window
    :precondition: screen must be a pygame object representing the game window
    :postcondition: draw the top boundary of the game board
    :return: a pygame object representing the top boundary of the game board
    """
    boundary_x = 465
    boundary_y = -5
    boundary_height = 193
    boundary_length = 5

    border = pygame.Rect(boundary_x, boundary_y, boundary_length, boundary_height)

    pygame.draw.rect(screen, (150, 75, 0), border)

    return border


def boundary_middle(screen):
    """
    Draw the middle boundary of the game board.

    :param screen: a pygame object representing the game window
    :precondition: screen must be a pygame object representing the game window
    :postcondition: draw the middle boundary of the game board
    :return: a pygame object representing the middle boundary of the game board
    """
    boundary_x = 465
    boundary_y = 253
    boundary_height = 380
    boundary_length = 5

    border = pygame.Rect(boundary_x, boundary_y, boundary_length, boundary_height)

    pygame.draw.rect(screen, (150, 75, 0), border)

    return border


def boundary_bottom(screen):
    """
    Draw the bottom boundary of the game board.

    :param screen: a pygame object representing the game window
    :precondition: screen must be a pygame object representing the game window
    :postcondition: draw the bottom boundary of the game board
    :return: a pygame object representing the bottom boundary of the game board
    """
    boundary_x = 465
    boundary_y = 693
    boundary_height = 234
    boundary_length = 5

    border = pygame.Rect(boundary_x, boundary_y, boundary_length, boundary_height)

    pygame.draw.rect(screen, (150, 75, 0), border)

    return border


def boundary_left(screen):
    """
    Draw the left boundary of the game board.

    :param screen: a pygame object representing the game window
    :precondition: screen must be a pygame object representing the game window
    :postcondition: draw the left boundary of the game board
    :return: a pygame object representing the left boundary of the game board
    """
    boundary_x = -8
    boundary_y = 460
    boundary_length = 676
    boundary_height = 5

    border = pygame.Rect(boundary_x, boundary_y, boundary_length, boundary_height)

    pygame.draw.rect(screen, (150, 75, 0), border)

    return border


def boundary_right(screen):
    """
    Draw the right boundary of the game board.

    :param screen: a pygame object representing the game window
    :precondition: screen must be a pygame object representing the game window
    :postcondition: draw the right boundary of the game board
    :return: a pygame object representing the right boundary of the game board
    """
    boundary_x = 728
    boundary_y = 460
    boundary_length = 616
    boundary_height = 5

    border = pygame.Rect(boundary_x, boundary_y, boundary_length, boundary_height)

    pygame.draw.rect(screen, (150, 75, 0), border)

    return border


def check_and_adjust_collision(player, boundary_rect, left, right, up, down):
    """
    Check if the player is colliding with a certain boundary and stop the player's movement from crossing the boundary.

    :param player: a pygame object representing the player
    :param boundary_rect: a pygame object representing the boundary
    :param left: a boolean representing if the player is moving left
    :param right: a boolean representing if the player is moving right
    :param up: a boolean representing if the player is moving up
    :param down: a boolean representing if the player is moving down
    :precondition: player must be a pygame object representing the player
    :precondition: boundary_rect must be a pygame object representing the boundary
    :precondition: left must be a boolean representing if the player is moving left
    :precondition: right must be a boolean representing if the player is moving right
    :precondition: up must be a boolean representing if the player is moving up
    :precondition: down must be a boolean representing if the player is moving down
    :postcondition: check if the player is colliding with a boundary and stop the player's movement from passing the
                    boundary
    """
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
