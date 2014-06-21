#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import board

class Player(object):
    """
    General Player Class
    """

    def __init__(self, marker):
        self.marker = marker

    def move(self, board, cell, marker):
        board.update_cell(cell, marker)

class Human(Player):
    """
    Human Player Class
    """
    
    def __init__(self, marker='X'):
        self.marker = marker

    def get_human_move(self, board):
        while True:
            try:
                move = eval(raw_input("Input your move in (x,y) coordinates:"))
                type(move) == tuple and len(move) == 2
            except:
                move = (3, 3)

            if move in board.get_empty_cells():
                break
            else:
                print "That's not a valid move! Try again."
        return move

class CPU(Player):
    """
    CPU Player Class
    """

    def __init__(self, marker='O'):
        self.marker = marker

    def score(self, board):
        if board.winner == board.p2:
            return 1
        elif board.winner == board.p1:
            return -1
        else:
            return 0

    def opposite_marker(self, marker):
        if marker == 'X':
            return 'O'
        else:
            return 'X'

    def minimax(self, board, marker):
        if board.gameover():
            return self.score(board)
        else:
            max_score = -1
            min_score = 1
            for cell in board.get_empty_cells():
                board.update_cell(cell, marker)
                val = self.minimax(board, self.opposite_marker(marker))
                board.update_cell(cell, board.blank)
                if marker == board.p2:
                    if val > max_score:
                        max_score = val
                elif marker == board.p1:
                    if val < min_score:
                        min_score = val
            if marker == board.p2:
                return max_score
            if marker == board.p1:
                return min_score

    def get_CPU_move(self, board):
        best_moves = []
        best_score = 0
        for cell in board.get_empty_cells():
            board.update_cell(cell, board.p2)
            val = self.minimax(board, board.p1)
            board.update_cell(cell, board.blank)
            if val > best_score:
                best_score = val
                best_moves = [cell]
            elif val == best_score:
                best_moves.append(cell)
        return random.choice(best_moves)
