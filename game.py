#!/usr/bin/python
# -*- coding: utf-8 -*-

from board import *
from players import *
from ui import *

class Game(object):
    
    def __init__(self):
        pass

    def human_move(self, board, human):
        human.move(board, human.get_human_move(board), human.marker)
        board.print_cells()

    def CPU_move(self, board, cpu):
        cpu.move(board, cpu.get_CPU_move(board), cpu.marker)
        board.print_cells()

    def play(self, board, player1, player2):
        
        print_instructions(board)

        if human_goes_first():
            board.print_cells()
            while True:
                self.human_move(board, player1)
                if board.gameover():
                    gameover_message(board)
                    break
                CPU_response()
                self.CPU_move(board, player2)
                if board.gameover():
                    gameover_message(board)
                    break
        else:
            while True:
                self.CPU_move(board, player2)
                if board.gameover():
                    gameover_message(board)
                    break
                self.human_move(board,player1)
                if board.gameover():
                    gameover_message(board)
                    break
                CPU_response()

if __name__ == '__main__':

    while True:
        board = Board()
        human = Human()
        cpu = CPU()
        game = Game()

        game.play(board, human, cpu)
        
        if not play_again():
            end_message()
            break



