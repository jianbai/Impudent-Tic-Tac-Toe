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

    def opposite_marker(self, board, marker):
        if marker == board.p1:
            return board.p2
        else:
            return board.p1

    def minimax(self, board, marker):
        if board.gameover():
            if board.winner == board.p1:
                return -1
            elif board.winner == board.blank:
                return 0
            elif board.winner == board.p2:
                return 1
        else:
            possible_moves = board.get_empty_cells()
            best_score = None
            for cell in possible_moves:
                board.update_cell(cell, board.p2)
                val = self.minimax(board, self.opposite_marker(board, marker))
                board.update_cell(cell, board.blank)
                if marker == board.p2:
                    if val > best_score:
                        best_score = val
                elif marker == board.p1:
                    if val < best_score:
                        best_score = val
                return best_score

    def get_CPU_move(self, board, marker):
        possible_moves = board.get_empty_cells()
        best_moves = []
        best_score = None
        for cell in possible_moves:
            board.update_cell(cell, marker)
            val = self.minimax(board, self.opposite_marker(board, marker))
            board.update_cell(cell, board.blank)
            if val > best_score:
                best_score = val
                best_moves = [cell]
            elif val == best_score:
                best_moves.append(cell)
        return random.choice(best_moves)
