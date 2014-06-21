#!/usr/bin/python
# -*- coding: utf-8 -*-

from board import *
from players import *
from ui import *

class Game(object):
    
    def __init__(self):
        pass

    def play(self, board, player1, player2):
        
        print_instructions()

        if human_goes_first():
            board.print_cells()
            while True:
                player1.move(board, player1.get_human_move(board), player1.marker)
                board.print_cells()
                if board.gameover():
                    end_message(board)
                    break
                CPU_response()
                player2.move(board, player2.get_CPU_move(board, board.p2), player2.marker)
                board.print_cells()
                if board.gameover():
                    end_message(board)
                    break
        else:
            while True:
                player2.move(board, player2.get_CPU_move(board, board.p2), player2.marker)
                board.print_cells()
                if board.gameover():
                    end_message(board)
                    break
                player1.move(board, player1.get_human_move(board), player1.marker)
                board.print_cells()
                if board.gameover():
                    end_message(board)
                    break
                CPU_response()

if __name__ == '__main__':
    board = Board()
    human = Human()
    cpu = CPU()
    game = Game()

    game.play(board, human, cpu)
