# run_nn.py
import pygame
from src.game import ReversiGame
from src.graphic import init_display, draw_board, get_clicked_cell
from src.nn import NeuralNetworkAI   

def main():
    screen = init_display()
    clock = pygame.time.Clock()
    game = ReversiGame()

    # choose who plays
    black_player = "human"
    white_player = "nn"

    ai_black = NeuralNetworkAI() if black_player == "nn" else None
    ai_white = NeuralNetworkAI() if white_player == "nn" else None

    running = True
    while running:
        valid_moves = game.available_moves()
        draw_board(screen, game.board, valid_moves)

        current = game.current_player  # 1 = black, -1 = white

        # nn auto move
        if (current == 1 and black_player == "nn") or (current == -1 and white_player == "nn"):
            ai = ai_black if current == 1 else ai_white

            move = ai.get_move(game.board, valid_moves, current)

            if move is not None:
                r, c = move
                game.step_move(r, c)

        # human move

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    cell = get_clicked_cell(pos)

                    if cell and cell in valid_moves:
                        r, c = cell
                        game.step_move(r, c)

        # game over
        if game.is_over():
            print("Game Over! Score:", game.score())
            running = False

        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()
