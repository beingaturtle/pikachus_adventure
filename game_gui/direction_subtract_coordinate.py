import pygame


def character_direction_facing(player, facing_left, facing_right, facing_up, facing_down):
    """
    Subtract the coordinate of the player based on the direction it is facing by 10 pixels.

    :param drawn_character: a pygame object draws the player
    :param player: a pygame object representing the player
    :precondition: player must be a pygame object representing the player
    :precondition: drawn_character must be a pygame object that draws the player
    :postcondition: player's coordinate is subtracted by 10 pixels based on the direction it is facing
    >>> character = pygame.Rect(0, 0, 10, 10)
    >>> character_direction_facing(character, True, False, False)
    >>> character
    <rect(-10, 0, 10, 10)>

    >>> character = pygame.Rect(0, 10, 15, 15)
    >>> character_direction_facing(character, False, False, True)
    >>> character
    <rect(0, 0, 15, 15)>
    """
    if facing_left:
        player.left -= 10
    elif facing_right:
        player.right += 10
    elif facing_up:
        player.top -= 10
    elif facing_down:
        player.bottom += 10
