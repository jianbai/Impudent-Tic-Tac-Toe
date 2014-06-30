#!/usr/bin/python
# -*- coding: utf-8 -*-

from board import *
from players import *
from ui import *


class Game(object):
    """
    A Tic Tac Toe game between a human player and a CPU player
    """
    
    def __init__(self, board, human, cpu):
        self.board = board
        self.human = human
        self.cpu = cpu

    def move(self, player):
        """
        Consumes: a Player object
        Produces: nothing
        Purpose: change the given cell in the given Board to the given marker
        """
        self.board.update_cell(player.get_move(), player.marker)
        print_cells(self.board)

    def play(self):
        """
        Consumes: nothing
        Produces: nothing
        Purpose: run the game loop until the game is over
        """        
        print_instructions(self.board)
        if human_goes_first():
            print_cells(self.board)
            while True:
                self.move(self.human)
                if self.board.gameover():
                    gameover_message(self.board)
                    break
                CPU_response()
                self.move(self.cpu)
                if self.board.gameover():
                    gameover_message(self.board)
                    break
        else:
            while True:
                self.move(self.cpu)
                if self.board.gameover():
                    gameover_message(self.board)
                    break
                self.move(self.human)
                if self.board.gameover():
                    gameover_message(self.board)
                    break
                CPU_response()


if __name__ == '__main__':
    while True:
        #Instantiate a Board object
        board = Board()
        #Instantiate a Human Player object
        human = Human(board)
        #Instantiate a CPU Player object
        cpu = CPU(board)
        #Instantiate a Game object
        game = Game(board, human, cpu)
        #Run game loop
        game.play()
        #Rerun game loop as long as the human player chooses to play again
        if not play_again():
            end_message()
            break