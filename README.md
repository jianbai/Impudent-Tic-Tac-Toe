========
Tic Tac Toe
========

To run
--------

Navigate to the TTT folder in the terminal and then run game.py:

	python game.py

Hopes and dreams for the future
--------

1. Move input mechanism

In order to input a move, the human player has to input a tuple with index values for the board, which is a multi-directional array. This isn’t the most intuitive method, and it would be nice if the human could just input a single key press to make a move, instead of entering coordinate values and then hitting enter.

2. CPU player always taking most direct path to winning

Currently, the CPU populates an array with the best moves available to it and then chooses a random item from the array. Sometimes, when the CPU is at match point it will not make the winning move and instead trap the human player, which still leads to victory. It would be nice if the minimax algorithm also directed the CPU to take the most direct path to victory if available.

3. Possibly using less functions

Some of the high level functions have 3 or 4 levels of nested callbacks, and it’s likely that this is not really necessary. I could be possible to streamline the classes further to cut some of the intermediate functions out.

4. Implementing a GUI

5. Alpha Beta Pruning
