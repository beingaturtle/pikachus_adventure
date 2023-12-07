from constants import SPEED, SCREEN_WIDTH, PLAYER_WIDTH, PLAYER_HEIGHT

def movement(player, left, right, up, down):
    """
    Update the character position based on movement keys.

    :param player: a pygame.Rect object representing the player
    :param left: boolean indicating movement to the left
    :param right: boolean indicating movement to the right
    :param up: boolean indicating movement upwards
    :param down: boolean indicating movement downwards
    :precondition: left right up down should be booleans indicative of player direction
    :postcondition: character position updated based on movement keys
    :return: the walk count as an integer
    """
    walk_count = 0
    if left and player[0] > SPEED - SPEED * 2:
        player.move_ip(-SPEED, 0)
        walk_count += 1
    elif right and player[0] < SCREEN_WIDTH - PLAYER_WIDTH + SPEED:
        player.move_ip(SPEED, 0)
        walk_count += 1
    elif up and player[1] > SPEED - SPEED:
        player.move_ip(0, -SPEED)
        walk_count += 1
    elif down and player[1] < 925 - PLAYER_HEIGHT:
        player.move_ip(0, SPEED)
        walk_count += 1
    return walk_count

