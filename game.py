#!/usr/bin/python
# -*- coding: utf-8 -*-

from board import Board
from players import *
from ui import *

class Game(object):
    
    def __init__(self):
        pass

    def play(self, board, player1, player2):
        
        print_instructions()

        if human_goes_first():
            while not board.gameover():
                player1.move(board, get_human_move(board), player1.marker)
                CPU_response()
                player2.move(board, get_CPU_move(board), player2.marker)
            else:
                end_message()
        else:
            while not board.gameover():
                player2.move(board, get_CPU_move(board), player2.marker)
                player1.move(board, get_human_move(board), player1.marker)
                CPU_response()
            else:
                end_message()

if __name__ == '__main__':
    board = Board()
    human = Human()
    cpu = CPU()
    game = Game()
    game.play(board, human, cpu)