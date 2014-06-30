#!/usr/bin/python
# -*- coding: utf-8 -*-

from board import *
from players import *
from ui import *


class Game(object):
    """
    A Tic Tac Toe game between a human player and a CPU player
    """
    
    def __init__(self):
        pass

    def move(self, board, player):
        """
        Consumes: a Board object, a tuple, and a string
        Produces: nothing
        Purpose: change the given cell in the given Board to the given marker
        """
        board.update_cell(player.get_move(board), player.marker)
        print_cells(board)

    def play(self, board, human, cpu):
        """
        Consumes: a Board object, a Human Player object, and a CPU Player object
        Produces: nothing
        Purpose: run the game loop until the game is over
        """        
        print_instructions(board)
        if human_goes_first():
            print_cells(board)
            while True:
                self.move(board, human)
                if board.gameover():
                    gameover_message(board)
                    break
                CPU_response()
                self.move(board, cpu)
                if board.gameover():
                    gameover_message(board)
                    break
        else:
            while True:
                self.move(board, cpu)
                if board.gameover():
                    gameover_message(board)
                    break
                self.move(board,human)
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



