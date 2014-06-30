#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import sys


class Human(object):
    """
    A Human player Class
    """
    
    MARKER = 'X'

    def __init__(self, board, marker=MARKER):
        self.board = board
        self.marker = marker

    def get_move(self):
        """
        Consumes: nothing
        Produces: a tuple
        Purpose: ask the human player to input the coordinates of the cell they want to mark, and return the value
        """        
        while True:
            try:
                move = ()
                string = raw_input("Input your move in (x,y) coordinates: ")
                chars = list(string)
                for char in chars:
                    if char.isdigit():
                        move = move + (int(char),)
                type(move) == tuple and len(move) == 2
            except KeyboardInterrupt:
                sys.exit()
            if move in self.board.get_empty_cells():
                break
            else:
                print "That's not a valid move! Try again."
        return move


class CPU(object):
    """
    A CPU player Class
    """

    MARKER = 'O'

    def __init__(self, board, marker=MARKER):
        self.board = board        
        self.marker = marker

    def score(self):
        """
        Consumes: nothing
        Produces: an integer
        Purpose: return 1 if the CPU has won or -1 if the human has won, otherwise return 0
        """        
        if self.board.winner == self.board.p2:
            return 1
        elif self.board.winner == self.board.p1:
            return -1
        else:
            return 0

    def opposite_marker(self, marker):
        """
        Consumes: a string
        Produces: a string
        Purpose: return the opposite marker of the given marker
        """        
        if marker == 'X':
            return 'O'
        else:
            return 'X'

    def minimax(self, marker):
        """
        Consumes: a string
        Produces: an integer
        Purpose: recursively construct all possible outcomes of the current Board state, identify the best outcome based on which player's turn it is, and return the score() of that outcome
        """        
        if self.board.gameover():
            return self.score()
        else:
            max_score = -1
            min_score = 1
            for cell in self.board.get_empty_cells():
                self.board.update_cell(cell, marker)
                score = self.minimax(self.opposite_marker(marker))
                self.board.update_cell(cell, self.board.blank)
                if marker == self.board.p2:
                    if score > max_score:
                        max_score = score
                elif marker == self.board.p1:
                    if score < min_score:
                        min_score = score
            if marker == self.board.p2:
                return max_score
            if marker == self.board.p1:
                return min_score

    def get_move(self):
        """
        Consumes: nothing
        Produces: a tuple
        Purpose: return a random pair of coordinates from an array of best moves, constructed by calling minimax() on each available cell
        """        
        best_moves = []
        best_score = 0
        #If CPU is playing the first move, return a random cell to cut lag time from calling minimax() on every cell
        if self.board.is_empty():
            return random.choice(self.board.get_empty_cells())
        for cell in self.board.get_empty_cells():
            self.board.update_cell(cell, self.board.p2)
            score = self.minimax(self.board.p1)
            self.board.update_cell(cell, self.board.blank)
            if score > best_score:
                best_score = score
                best_moves = [cell]
            elif score == best_score:
                best_moves.append(cell)
        return random.choice(best_moves)
