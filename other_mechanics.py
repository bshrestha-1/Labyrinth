def move_player(LABYRINTH, position, direction, steps):
    x, y = position
    for _ in range(steps):
        if direction == "up" and x > 0 and LABYRINTH[x-1][y] == 0:
            x -= 1
        elif direction == "down" and x < 9 and LABYRINTH[x+1][y] == 0:
            x += 1
        elif direction == "left" and y > 0 and LABYRINTH[x][y-1] == 0:
            y -= 1
        elif direction == "right" and y < 9 and LABYRINTH[x][y+1] == 0:
            y += 1
        else:
            break  # Stop if we hit a wall or the edge of the board
    return [x, y]

def use_key_card(position, direction):
    x, y = position
    if direction == "up" and x > 1:
        return [x-2, y]
    elif direction == "down" and x < 8:
        return [x+2, y]
    elif direction == "left" and y > 1:
        return [x, y-2]
    elif direction == "right" and y < 8:
        return [x, y+2]
    return position



def rotate_tile(LABYRINTH,row, col):
    LABYRINTH[row][col] = 1 - LABYRINTH[row][col]  # Toggle between 0 and 1


def switch_places(runner_pos, chaser_pos):
    return chaser_pos, runner_pos
