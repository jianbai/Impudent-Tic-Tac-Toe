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
            best_score = None
            for cell in board.get_empty_cells():
                board.update_cell(cell, board.p2)
                val = self.minimax(board, opposite_marker(board, marker))
                board.update_cell(cell, board.blank)
                if marker == board.p2:
                    if val > best_score:
                        best_score = val
                elif marker == board.p1:
                    if val < best_score:
                        best_score = val
                return best_score

    def get_best_move(self, board, marker):
        possible_moves = board.get_empty_cells()
        best_moves = []
        best_score = None
        for cell in possible_moves:
            board.update_cell(cell, marker)
            val = self.minimax(board, opposite_marker(board, marker))
            board.update_cell(cell, None)
            if val > best_score:
                best_score = val
                best_moves = [cell]
            elif val == best_score:
                best_moves.append(cell)
        return random.choice(moves)



