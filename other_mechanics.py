
def rotate_tile(LABYRINTH,row, col):
    LABYRINTH[row][col] = 1 - LABYRINTH[row][col]  # Toggle between 0 and 1


def switch_places(runner_pos, chaser_pos):
    return chaser_pos, runner_pos