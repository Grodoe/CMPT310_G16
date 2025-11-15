import pygame
from src.game import ReversiGame
from src.graphic import init_display, draw_board, get_clicked_cell
from src.MiniMax import MinimaxAI

MOVE_DELAY_MS = 50  # shorten delay for multiple games
NUM_GAMES = 10      # run 10 games

def play_single_game(black_ai, white_ai, display=False):
    game = ReversiGame()
    players = {1: black_ai, -1: white_ai}
    game.current_player = 1  # Black starts

    if display:
        screen = init_display()
        clock = pygame.time.Clock()
    else:
        screen = clock = None

    while not game.is_over():
        valid_moves = game.available_moves()
        if display:
            draw_board(screen, game.board, valid_moves)

        current_ai = players[game.current_player]
        move = current_ai.select_move(game.board, game.current_player)

        if move is not None:
            r, c = move
            game.step_move(r, c)
            if display:
                pygame.time.wait(MOVE_DELAY_MS)
        else:
            game.current_player *= -1  # pass turn

        if display:
            clock.tick(30)

    black_score, white_score = game.score()
    return black_score, white_score

def main():
    black_ai = MinimaxAI(depth=3, player=1)
    white_ai = MinimaxAI(depth=3, player=-1)

    point_differences = []

    for i in range(NUM_GAMES):
        print(f"\nStarting Game {i+1}")
        black, white = play_single_game(black_ai, white_ai, display=False)  # set True to watch
        diff = black - white
        point_differences.append(diff)
        print(f"Game {i+1} finished — Black: {black}, White: {white}, Difference: {diff}")

    print("\nAll games finished!")
    print("Point differences per game:", point_differences)
    avg_diff = sum(point_differences) / len(point_differences)
    print("Average point difference (Black - White):", avg_diff)

    pygame.quit()

if __name__ == "__main__":
    main()
