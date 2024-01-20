import pygame


# to draw the board
def draw_board(LABYRINTH, CELL_SIZE, screen, BLACK, WHITE, GREEN, BLUE,RED, runner_position, chaser_position, EXIT):
    for row in range(10):
        for col in range(10):
            x = col * CELL_SIZE
            y = row * CELL_SIZE
            if LABYRINTH[row][col] == 1:
                pygame.draw.rect(screen, BLACK, (x, y, CELL_SIZE, CELL_SIZE))
            else:
                pygame.draw.rect(screen, WHITE, (x, y, CELL_SIZE, CELL_SIZE), 1)

    # Draw exit
    pygame.draw.rect(screen, GREEN, (EXIT[1] * CELL_SIZE, EXIT[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Draw runner
    pygame.draw.circle(screen, BLUE, (runner_position[1] * CELL_SIZE + CELL_SIZE // 2,
                                      runner_position[0] * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 3)

    # Draw chaser
    pygame.draw.circle(screen, RED, (chaser_position[1] * CELL_SIZE + CELL_SIZE // 2,
                                     chaser_position[0] * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 3)
