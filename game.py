#!/usr/bin/python
# -*- coding: utf-8 -*-

"""

"""

from board import *
from players import *
from ui import *


class Game(object):
    """
    A Game
    """
    
    def __init__(self):
        pass

    def human_move(self, board, human):
        """
        Consumes: a Board object and a Human Player object
        Produces: nothing
        Purpose: ask the human player for a move, execute that move and reprint the updated board
        """        
        human.move(board, human.get_human_move(board), human.marker)
        board.print_cells()

    def CPU_move(self, board, cpu):
        """
        Consumes: a Board object and a CPU Player object
        Produces: nothing
        Purpose: get a minimax() optimized move, execute that move and reprint the updated board
        """        
        cpu.move(board, cpu.get_CPU_move(board), cpu.marker)
        board.print_cells()

    def play(self, board, human, cpu):
        """
        Consumes: a Board object, a Human Player object, and a CPU Player object
        Produces: nothing
        Purpose: run the game loop until the game is over
        """        
        print_instructions(board)
        if human_goes_first():
            board.print_cells()
            while True:
                self.human_move(board, human)
                if board.gameover():
                    gameover_message(board)
                    break
                CPU_response()
                self.CPU_move(board, cpu)
                if board.gameover():
                    gameover_message(board)
                    break
        else:
            while True:
                self.CPU_move(board, cpu)
                if board.gameover():
                    gameover_message(board)
                    break
                self.human_move(board,human)
                if board.gameover():
                    gameover_message(board)
                    break
                CPU_response()


if __name__ == '__main__':

    while True:
        #Instantiate a Board object
        board = Board()
        #Instantiate a Human Player object
        human = Human()
        #Instantiate a CPU Player object
        cpu = CPU()
        #Instantiate a Game object
        game = Game()
        #Run game loop
        game.play(board, human, cpu)
        #Rerun game loop as long as the human player chooses to play again
        if not play_again():
            end_message()
            break



