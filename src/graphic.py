# src/ui.py
import pygame
from src.board import BLACK, WHITE, EMPTY

TILE_SIZE = 64
SCREEN_WIDTH = SCREEN_HEIGHT = 800
start_x = (SCREEN_WIDTH - (8 * TILE_SIZE)) // 2
start_y = (SCREEN_HEIGHT - (8 * TILE_SIZE)) // 2

# images
black_tile = pygame.transform.scale(pygame.image.load("tiles/black.png"), (TILE_SIZE, TILE_SIZE))
white_tile = pygame.transform.scale(pygame.image.load("tiles/white.png"), (TILE_SIZE, TILE_SIZE))
cell1 = pygame.transform.scale(pygame.image.load("tiles/cell1.png"), (TILE_SIZE, TILE_SIZE))
cell2 = pygame.transform.scale(pygame.image.load("tiles/cell2.png"), (TILE_SIZE, TILE_SIZE))
possible = pygame.transform.scale(pygame.image.load("tiles/possible.png"), (TILE_SIZE, TILE_SIZE))

def init_display():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    return screen

def draw_board(screen, board, valid_moves):
    screen.fill((0, 68, 0))
    # draw background grid
    for row in range(8):
        for col in range(8):
            x = start_x + col * TILE_SIZE
            y = start_y + row * TILE_SIZE
            tile = cell1 if (row + col) % 2 == 0 else cell2
            screen.blit(tile, (x, y))
    # draw pieces
    for r in range(8):
        for c in range(8):
            piece = board[r, c]
            if piece == BLACK:
                screen.blit(black_tile, (start_x + c*TILE_SIZE, start_y + r*TILE_SIZE))
            elif piece == WHITE:
                screen.blit(white_tile, (start_x + c*TILE_SIZE, start_y + r*TILE_SIZE))
    # draw hints for valid moves
    for (r, c) in valid_moves:
        screen.blit(possible, (start_x + c*TILE_SIZE, start_y + r*TILE_SIZE))

    pygame.display.flip()

def get_clicked_cell(pos):
    x, y = pos
    col = (x - start_x) // TILE_SIZE
    row = (y - start_y) // TILE_SIZE
    if 0 <= row < 8 and 0 <= col < 8:
        return row, col
    return None
