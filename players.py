#!/usr/bin/python
import board.py

class Player(object):
    pass

class P1(Player):
    """
    Human Player Class
    """
    pass

class P2(Player):
    """
    CPU Player Class
    """

    def minimax(self, node, marker):
        max_score = None
        if node.gameover():
            if node.__winner == node.__p1:
                return -1
            elif node.__winner == node.__blank:
                return 0
            elif node.__winner == node.__p2:
                return 1
        for move in node.get_empty_cells():

    def get_best_move(self):
        possible_moves = Board.get_empty_cells()
        for move in possible_moves:
