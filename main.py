# main.py
import pygame
from src.game import ReversiGame
from src.graphic import init_display, draw_board, get_clicked_cell

def main():
    screen = init_display()
    clock = pygame.time.Clock()
    game = ReversiGame()

    running = True
    while running:
        valid_moves = game.available_moves()
        draw_board(screen, game.board, valid_moves)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                cell = get_clicked_cell(pos)
                if cell and cell in valid_moves:
                    r, c = cell
                    game.step_move(r, c)

        if game.is_over():
            print("Game Over! Score:", game.score())
            running = False

        clock.tick(30)  # 30 FPS cap

    pygame.quit()

if __name__ == "__main__":
    main()
