# src/run_Table.py
import subprocess
import sys
import re
from pathlib import Path

# How many games per matchup
N_GAMES_PER_MATCHUP = 10

# Folder that contains the run_*.py scripts (this src folder)
BASE_DIR = Path(__file__).resolve().parent

# Matchups to run: {label: (script_name, black_name, white_name)}
MATCHUPS = {
    "Greedy vs Minimax": ("run_GreedyvsMiniMax.py", "Greedy (Black)", "Minimax (White)"),
    "Random vs Minimax": ("run_RandomvsMiniMax.py", "Random (Black)", "Minimax (White)"),
}

# Matches: Game Over! Score — Black: 34  White: 30
SCORE_PATTERN = re.compile(r"Game Over!.*Black:\s*(\d+)\s*White:\s*(\d+)")


def run_one_game(script_name: str):
    """Run a single game script and return (black_score, white_score) or None."""
    script_path = BASE_DIR / script_name

    result = subprocess.run(
        [sys.executable, str(script_path)],
        capture_output=True,
        text=True,
    )

    output = result.stdout + result.stderr
    m = SCORE_PATTERN.search(output)
    if not m:
        print("Could not parse score from output:")
        print(output)
        return None

    b, w = map(int, m.groups())
    return b, w


def run_matchup(label: str, script_name: str, black_name: str, white_name: str):
    scores = []
    for i in range(N_GAMES_PER_MATCHUP):
        print(f"[{label}] Game {i+1}/{N_GAMES_PER_MATCHUP}...")
        s = run_one_game(script_name)
        if s is not None:
            scores.append(s)

    if not scores:
        print(f"No valid results for {label}")
        return

    wins_black = wins_white = draws = 0
    total_black = total_white = 0

    for b, w in scores:
        total_black += b
        total_white += w
        if b > w:
            wins_black += 1
        elif w > b:
            wins_white += 1
        else:
            draws += 1

    n = len(scores)
    avg_black = total_black / n
    avg_white = total_white / n

    # Simple text table
    print(f"\n=== {label} ({n} games) ===")
    print(f"{'Player':20} {'Wins':>6} {'Avg Score':>11}")
    print("-" * 40)
    print(f"{black_name:20} {wins_black:6d} {avg_black:11.2f}")
    print(f"{white_name:20} {wins_white:6d} {avg_white:11.2f}")
    print(f"{'Draws':20} {draws:6d}")
    print()


def main():
    for label, (script, bname, wname) in MATCHUPS.items():
        run_matchup(label, script, bname, wname)


if __name__ == "__main__":
    main()
