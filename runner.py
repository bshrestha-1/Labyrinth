import pygame
import random
from draw_board import draw_board
from other_mechanics import switch_places,rotate_tile, move_player, use_key_card

pygame.init()

# Game constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
CELL_SIZE = 50

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
GRAY = (200, 200, 200)

# Game setup
LABYRINTH = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

EXIT = (8, 0)
runner_position = [1, 1]
chaser_position = [8, 8]

# Card types
MOVEMENT_CARDS = ["Move 1 Step", "Move 2 Steps", "Move 3 Steps"]
KEY_CARDS = ["Key Card 1", "Key Card 2", "Key Card 3"]
ROTATE_CARDS = ["Rotate Card 1", "Rotate Card 2", "Rotate Card 3"]
DRAW_CARDS = ["Draw Card"]
SWITCH_PLACES_CARDS = ["Switch Places Card"]

ALL_CARDS = MOVEMENT_CARDS + KEY_CARDS + ROTATE_CARDS + DRAW_CARDS + SWITCH_PLACES_CARDS

# player cards
runner_cards = random.sample(ALL_CARDS, 3)
chaser_cards = random.sample(ALL_CARDS, 3)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Labyrinth Game")

# Font setup
font = pygame.font.Font(None, 36)


def draw_cards(cards, y_offset):
        card_rects = []
        for i, card in enumerate(cards):
            rect = pygame.Rect(550, y_offset + i * 40, 400, 30)
            pygame.draw.rect(screen, GRAY, rect)
            text = font.render(card, True, BLACK)
            screen.blit(text, (560, y_offset + i * 40))
            card_rects.append(rect)
        return card_rects

def draw_direction_buttons():
    buttons = {}
    directions = ["up", "down", "left", "right"]
    for i, direction in enumerate(directions):
        rect = pygame.Rect(550 + i * 100, 450, 80, 30)
        pygame.draw.rect(screen, GRAY, rect)
        text = font.render(direction, True, BLACK)
        screen.blit(text, (560 + i * 100, 455))
        buttons[direction] = rect
    return buttons


def main():
    global runner_position, chaser_position, runner_cards, chaser_cards
    current_player = "Runner"
    selected_card = None
    
    running = True
    while running:
        screen.fill(WHITE)
        # Draw the initial game board
        draw_board(LABYRINTH, CELL_SIZE, screen, BLACK, WHITE, GREEN, BLUE,RED, runner_position, chaser_position, EXIT)
        
        runner_text = font.render("Runner Cards:", True, BLACK)
        chaser_text = font.render("Chaser Cards:", True, BLACK)
        screen.blit(runner_text, (550, 50))
        screen.blit(chaser_text, (550, 200))
        runner_card_rects = draw_cards(runner_cards, 100)
        chaser_card_rects = draw_cards(chaser_cards, 250)
        
        current_player_text = font.render(f"Current Player: {current_player}", True, BLACK)
        screen.blit(current_player_text, (550, 400))
        
        direction_buttons = draw_direction_buttons()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                
                if current_player == "Runner":
                    for i, rect in enumerate(runner_card_rects):
                        if rect.collidepoint(mouse_pos):
                            selected_card = runner_cards[i]
                            print(f"Selected card: {selected_card}")
                else:
                    for i, rect in enumerate(chaser_card_rects):
                        if rect.collidepoint(mouse_pos):
                            selected_card = chaser_cards[i]
                            print(f"Selected card: {selected_card}")
                
                if selected_card:
                    for direction, rect in direction_buttons.items():
                        if rect.collidepoint(mouse_pos):
                            if selected_card.startswith("Move"):
                                steps = int(selected_card.split()[1])
                                if current_player == "Runner":
                                    runner_position = move_player(LABYRINTH,runner_position, direction, steps)
                                    runner_cards.remove(selected_card)
                                    runner_cards.append(random.choice(ALL_CARDS))
                                else:
                                    chaser_position = move_player(LABYRINTH,chaser_position, direction, steps)
                                    chaser_cards.remove(selected_card)
                                    chaser_cards.append(random.choice(ALL_CARDS))
                            elif selected_card.startswith("Key Card"):
                                if current_player == "Runner":
                                    runner_position = use_key_card(runner_position, direction)
                                    runner_cards.remove(selected_card)
                                    runner_cards.append(random.choice(ALL_CARDS))
                                else:
                                    chaser_position = use_key_card(chaser_position, direction)
                                    chaser_cards.remove(selected_card)
                                    chaser_cards.append(random.choice(ALL_CARDS))
                            elif selected_card.startswith("Rotate Card"):
                                row = random.randint(0, 9)
                                col = random.randint(0, 9)
                                rotate_tile(LABYRINTH,row, col)
                                if current_player == "Runner":
                                    runner_cards.remove(selected_card)
                                    runner_cards.append(random.choice(ALL_CARDS))
                                else:
                                    chaser_cards.remove(selected_card)
                                    chaser_cards.append(random.choice(ALL_CARDS))
                            elif selected_card == "Switch Places Card":
                                runner_position, chaser_position = switch_places(runner_position, chaser_position)
                                if current_player == "Runner":
                                    runner_cards.remove(selected_card)
                                    runner_cards.append(random.choice(ALL_CARDS))
                                else:
                                    chaser_cards.remove(selected_card)
                                    chaser_cards.append(random.choice(ALL_CARDS))
                            elif selected_card == "Draw Card":
                                if current_player == "Runner":
                                    runner_cards.remove(selected_card)
                                    runner_cards.append(random.choice(ALL_CARDS))
                                    runner_cards.append(random.choice(ALL_CARDS))
                                else:
                                    chaser_cards.remove(selected_card)
                                    chaser_cards.append(random.choice(ALL_CARDS))
                                    chaser_cards.append(random.choice(ALL_CARDS))
                            
                            current_player = "Chaser" if current_player == "Runner" else "Runner"
                            selected_card = None
                            print(f"{current_player}'s turn")
        
        if runner_position == list(EXIT):
            print("Runner wins!")
            running = False
        elif runner_position == chaser_position:
            print("Chaser wins!")
            running = False
        
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
