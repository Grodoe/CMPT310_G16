# Reversi AI: An analysis on the performance of Minimax with Alpha Beta Pruning 

This project implements Minimax to play the game Reversi/Othello using various methods to analyse the behaviour
- Greedy AI
- Random AI
- Minimax AI
- Agent vs Agent simulation
- Pygame for game visualisation

# Installation
To run the simulations, you must have these prerequisites
Create a virtual environment
- python3 -m venv venv
- source venv/bin/activate

Install the proper libraries, like Numpy
- pip install -r requirements.txt
  
# Running the simulations 
Human vs Greedy
python3 run_Greedy.py

Human vs MiniMax
python3 run_Minimax.py

Greedy vs Minimax 
python3 run_GreedyvsMiniMax.py

Minimax vs Minimax
python3 run_MiniMaxvsMiniMax.py

Random vs Minimax
python3 run_RandomvsMiniMax.py

Run multiple simulation games
python3 run_Table.py


# Game-playing Agents
Greedy AI
- Basic Algorithm that picks the most immediate reward, which flips the  most discs
Random AI
- Makes random moves based on the currently available legal moves
Minimax AI
- Makes the most max action based on specified depths 1-5
- Assumes opponent takes the minimum action
- Uses alpha-beta pruning for faster and more efficient computation
- Weighs Disc Difference, Mobility, and Corner to evaluate the best action


# Challenges
- Running time and cost for the initial Minimax without alpha-beta pruning made testing difficult and time-consuming
- Initial pivot from implementing a self-playing Algorithm using convolutional neural networks proved to be out of scope and difficult to implement, as it wasn't covered in the lecture

# Contributors
Artin Jafari Rad (301555369)

Gordon Cheuk (301543060)

Molly McAlpine (301604991)

Vincent Ha (301592732)


