# run_basic_greedy.py
import pygame

from src.game import ReversiGame
from src.graphic import init_display, draw_board, get_clicked_cell
from src.board import BLACK, WHITE
from src.BasicGreedy import BasicGreedy


MOVE_DELAY_MS = 200  # 0.2s delay after any move for readability


def main():
    ai = BasicGreedy()          # Black is AI
    screen = init_display()
    clock = pygame.time.Clock()
    game = ReversiGame()

    # Let the human (White) start
    game.current_player = WHITE

    running = True
    while running:
        valid_moves = game.available_moves()
        draw_board(screen, game.board, valid_moves)

        if game.current_player == BLACK:
            # AI (Black) turn
            move = ai.select_move(game.board, game.current_player)
            if move is not None:
                r, c = move
                game.step_move(r, c)
                pygame.time.wait(MOVE_DELAY_MS)
            else:
                game.current_player *= -1  # pass
        else:
            # Human (White) turn
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    cell = get_clicked_cell(pos)
                    if cell and cell in valid_moves:
                        r, c = cell
                        game.step_move(r, c)
                        pygame.time.wait(MOVE_DELAY_MS)

        if game.is_over():
            black, white = game.score()
            print(f"Game Over! Score — Black: {black}  White: {white}")
            running = False

        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()
