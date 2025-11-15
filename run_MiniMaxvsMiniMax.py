import pygame

from src.game import ReversiGame
from src.graphic import init_display, draw_board, get_clicked_cell
from src.MiniMax import MinimaxAI

MOVE_DELAY_MS = 200  # 0.2s delay after any move for readability

def main():
    # Two Minimax AIs
    black_ai = MinimaxAI(depth=3, player=1)   # Black
    white_ai = MinimaxAI(depth=3, player=-1)  # White

    screen = init_display()
    clock = pygame.time.Clock()
    game = ReversiGame()

    players = {
        1: black_ai,
        -1: white_ai,
    }

    game.current_player = 1  # Black starts

    running = True
    while running:
        valid_moves = game.available_moves()
        draw_board(screen, game.board, valid_moves)

        current_player_ai = players[game.current_player]
        move = current_player_ai.select_move(game.board, game.current_player)

        if move is not None:
            r, c = move
            game.step_move(r, c)
            pygame.time.wait(MOVE_DELAY_MS)
        else:
            # Pass turn if no valid moves
            game.current_player *= -1

        if game.is_over():
            black, white = game.score()
            print(f"Game Over! Score — Black: {black}  White: {white}")
            running = False

        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
