import pygame
import random

# setting up tiles
black = pygame.image.load("tiles/black.png")
white = pygame.image.load("tiles/white.png")
cell1 = pygame.image.load("tiles/cell1.png")
cell2 = pygame.image.load("tiles/cell2.png")
possible = pygame.image.load("tiles/possible.png")

# scale tiles
TILE_SIZE = 64
black = pygame.transform.scale(black, (TILE_SIZE, TILE_SIZE))
white = pygame.transform.scale(white, (TILE_SIZE, TILE_SIZE))
cell1 = pygame.transform.scale(cell1, (TILE_SIZE, TILE_SIZE))
cell2 = pygame.transform.scale(cell2, (TILE_SIZE, TILE_SIZE))
possible = pygame.transform.scale(possible, (TILE_SIZE, TILE_SIZE))

# select starting pos
side = random.random() < 0.5

# setting up the game window!
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

start_x = (800 - (8 * TILE_SIZE)) // 2
start_y = (800 - (8 * TILE_SIZE)) // 2

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# draws image ontop of tile
def draw_image_on_tile(img, col, row):
    x = start_x + col * TILE_SIZE - 1
    y = start_y + row * TILE_SIZE + 1
    screen.blit(img, (x, y))

# game loop
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #bg colour
    screen.fill((0, 68, 0))

    #draw grid
    for row in range(8):
        for col in range(8):
            x = start_x + col * TILE_SIZE
            y = start_y + row * TILE_SIZE
            tile = cell1 if (row + col) % 2 == 0 else cell2
            screen.blit(tile, (x, y))

    #draw starting positions
    if side:
        draw_image_on_tile(black, 3, 3)
        draw_image_on_tile(black, 4, 4)
        draw_image_on_tile(white, 3, 4)
        draw_image_on_tile(white, 4, 3)
    else:
        draw_image_on_tile(white, 3, 3)
        draw_image_on_tile(white, 4, 4)
        draw_image_on_tile(black, 3, 4)
        draw_image_on_tile(black, 4, 3)

    
    
    pygame.display.flip();
pygame.quit()