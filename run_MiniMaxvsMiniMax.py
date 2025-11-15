import pygame
from src.game import ReversiGame
from src.graphic import init_display, draw_board
from src.MiniMax import MinimaxAI

MOVE_DELAY_MS = 0
NUM_GAMES = 5   # games per depth matchup

def play_single_game(black_ai, white_ai, display=False):
    game = ReversiGame()
    game.current_player = 1   # black starts
    players = {1: black_ai, -1: white_ai}

    if display:
        screen = init_display()
        clock = pygame.time.Clock()
    else:
        screen = clock = None

    while not game.is_over():
        valid_moves = game.available_moves()

        if display:
            draw_board(screen, game.board, valid_moves)

        ai = players[game.current_player]
        move = ai.select_move(game.board, game.current_player)

        if move:
            r, c = move
            game.step_move(r, c)
            if display:
                pygame.time.wait(MOVE_DELAY_MS)
        else:
            game.current_player *= -1  # pass

        if display:
            clock.tick(30)

    return game.score()  # returns (black_score, white_score)


def main():
    matchups = [(1, 2), (2, 3), (3, 4)]
    results_summary = {}

    for d1, d2 in matchups:
    
        print(f"      MATCHUP {d1} vs {d2}")


        # normal
        print(f"\n--- Normal: Black = depth {d1}, White = depth {d2} ---")
        black_ai = MinimaxAI(depth=d1, player=1)
        white_ai = MinimaxAI(depth=d2, player=-1)

        diffs_normal = []

        for g in range(NUM_GAMES):
            black, white = play_single_game(black_ai, white_ai, display=False)
            diff = white - black
            diffs_normal.append(diff)
            print(f"Game {g+1}: Black={black}  White={white}  Diff(white-black)={diff}")

        avg_normal = sum(diffs_normal) / NUM_GAMES
        print(f"Average Diff (White - Black) normal: {avg_normal:.2f}")

        # swapped
        print(f"\n--- Swapped: Black = depth {d2}, White = depth {d1} ---")
        black_ai = MinimaxAI(depth=d2, player=1)
        white_ai = MinimaxAI(depth=d1, player=-1)

        diffs_swap = []

        for g in range(NUM_GAMES):
            black, white = play_single_game(black_ai, white_ai, display=False)
            diff = white - black
            diffs_swap.append(diff)
            print(f"Game {g+1}: Black={black}  White={white}  Diff(white-black)={diff}")

        avg_swap = sum(diffs_swap) / NUM_GAMES
        print(f"Average Diff (White - Black) swapped: {avg_swap:.2f}")

        # store in summary
        results_summary[(d1, d2)] = (avg_normal, avg_swap)

    # final summary
 
    print("        FINAL SUMMARY")


    for (d1, d2), (avgN, avgS) in results_summary.items():
        print(f"{d1} vs {d2}:  Normal Avg={avgN:.2f},  Swapped Avg={avgS:.2f}")

    pygame.quit()


if __name__ == "__main__":
    main()
