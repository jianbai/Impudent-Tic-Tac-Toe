#!/usr/bin/python
# -*- coding: utf-8 -*-

class Board(object):
    """
    A Tic Tac Toe board
    """

    P1_MARKER = 'X'             #Human player
    P2_MARKER = 'O'             #CPU player
    BLANK_MARKER = '-'
    WIN_COMBOS = [
        #Horizontal
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        #Vertical
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        #Diagonal
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]
    WINNER = None

    def __init__(self, p1_marker=P1_MARKER, p2_marker=P2_MARKER, blank_marker=BLANK_MARKER, win_combos=WIN_COMBOS, winner=WINNER):
        self.p1 = p1_marker
        self.p2 = p2_marker
        self.blank = blank_marker
        self.win_combos = win_combos
        self.winner = winner
        self.cells = [[self.blank]*3 for _ in range(3)]
        
    def print_cells(self):
        space = ' '
        print '\n'
        for row in self.cells:
            for cell in row:
                print cell + space*2,
            print '\n'

    def update_cell(self, (x, y), marker):
        self.cells[x][y] = marker

    def check_cell(self, (x, y)):
        return self.cells[x][y]

    def get_empty_cells(self):
        empty_cells = []
        for row_index, row in enumerate(self.cells):
            for col_index, col in enumerate(row):
                if self.cells[row_index][col_index] == self.blank:
                    empty_cells.append((row_index, col_index))
        return empty_cells

    def is_empty(self):
        result = True
        for row in self.cells:
            for cell in row:
                if cell != self.blank:
                    result = False
        return result

    def is_full(self):
        result = True
        for row in self.cells:
            for cell in row:
                if cell == self.blank:
                    result = False
        return result

    def gameover(self):
        result = False
        for combo in self.win_combos:
            cell_0 = self.check_cell(combo[0])
            cell_1 = self.check_cell(combo[1])
            cell_2 = self.check_cell(combo[2])
            if cell_0 == cell_1 == cell_2 and cell_0 != self.blank:
                result = True
                if cell_0 == self.p1:
                    self.winner = self.p1
                elif cell_0 == self.p2:
                    self.winner = self.p2
                return result
        if self.is_full():
            result = True
            self.winner = self.blank
        return result