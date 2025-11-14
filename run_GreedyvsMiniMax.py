# run_basic_greedy.py
import pygame

from src.game import ReversiGame
from src.graphic import init_display, draw_board, get_clicked_cell
from src.board import BLACK, WHITE
from src.BasicGreedy import BasicGreedy
from src.MiniMax import MinimaxAI 

MOVE_DELAY_MS = 20  # 0.2s delay after any move for readability


def main():
    greedy_ai = BasicGreedy() # White 
    minimax_ai = MinimaxAI(depth = 4) # Black 
    screen = init_display()
    clock = pygame.time.Clock()
    game = ReversiGame()

    game.current_player = WHITE

    running = True
    while running:
        valid_moves = game.available_moves()
        draw_board(screen, game.board, valid_moves)

        if game.current_player == BLACK:
            move = greedy_ai.select_move(game.board, game.current_player) #black turn

        else:
            move = minimax_ai.select_move(game.board, game.current_player) #white turn

        if move is not None:
                r, c = move
                game.step_move(r, c)
                pygame.time.wait(MOVE_DELAY_MS)
        else: game.current_player = game.current_player*-1 
                
                
        if game.is_over():
            black, white = game.score()
            print(f"Game Over! Score — Black: {black}  White: {white}")
            running = False

        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()
