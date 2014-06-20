#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

class Board(object):
    """
    A Tic Tac Toe board
    """

    #FULL = False
    #STATE = bin(0)
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
        #self.__full = full
        #self.__state = state
        #self.__won = False
        self.p1 = p1_marker
        self.p2 = p2_marker
        self.blank = blank_marker
        self.win_combos = win_combos
        self.winner = winner
        self.cells = [[self.blank]*3 for _ in range(3)]
        
    def print_cells(self):
        space = ' '
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

    def reset_cells(self):
        self.cells = [[self.blank]*3 for _ in range(3)]

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
                else:
                    self.winner = self.p2
                break
        if self.is_full():
            result = True
            self.winner = self.blank
        return result

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

def print_instructions():
    print "CPU: Welcome to Tic Tac Toe! Our board has 3 rows and 3 columns, each numbered 0, 1, and 2. To play, input your moves as (x,y) coordinates. Don't forget the parentheses!"

def human_goes_first():
    while True:
        human_first = raw_input("CPU: Would you like to go first? [y/n]:")
        try:
            human_first.lower() == 'y' or human_first.lower() == 'n'
        except:
            human_first = 'x'
        if human_first.lower() == 'y' or human_first.lower() == 'n':
            break
        else:
            print "CPU: I didn't catch that. Make sure you enter 'y' or 'n'!"
    if human_first.lower() == 'y':
        return True
    elif human_first.lower() == 'n':
        return False

def CPU_response():
    responses = ["Touché", "Well played", "Hmmm...", "A worthy opponent, you are", "Let's see here... Aha!", "Shrewd move", "Ah, yes...", "I think I see where you're going", "You can't fool me!", "Do you take me for a simpleton?", "Carefully considered", "Delightful!", "Very clever", "It seems I have found a truly formidable challenger!", "A wise decision", "A cunning play", "Your tactics are crafty", "A deft maneuver", "I can see you are quite sharp", "Finally, a worthy foe!", "You are clearly a diligent student of the game... I can respect that", "Astute", "Careful now!", "Keep your guard up", "Remain ever vigilant!", "Ah, the thrill of combat! I live for this!", "For each of your thrusts, I shall parry! Will you survive my counterattack?", "Ah, the beauty of the game!", "For every action, there must be reaction", "Back and forth until the end of time!", "I was born for this struggle", "Alas, is there no end?", "Though our game must end, I shall remember you"]
    print "CPU: " + random.choice(responses)

def win_message():
    print "CPU: You win! Wait, that wasn't supposed to happen..."

def lose_message():
    print "CPU: Sorry, you lose... Better luck next time!"

def draw_message():
    print "CPU: Look's like a draw. We're both winners!"

def restart_message():
    print "CPU: Wasn't that fun? Let's play again!"

def end_message(board):
    if board.winner == board.p1:
        win_message()
    elif board.winner == board.blank:
        draw_message()
    elif board.winner == board.p2:
        lose_message
    restart_message()

class Game(object):
    
    def __init__(self):
        pass

    def play(self, board, player1, player2):
        
        print_instructions()

        if human_goes_first():
            board.print_cells()
            while board.gameover():
                player1.move(board, player1.get_human_move(board), player1.marker)
                board.print_cells()
                CPU_response()
                player2.move(board, player2.get_CPU_move(board, board.p2), player2.marker)
                board.print_cells()
            else:
                end_message(board)
        else:
            while not board.gameover():
                player2.move(board, player2.get_CPU_move(board, board.p2), player2.marker)
                board.print_cells()
                player1.move(board, player1.get_human_move(board), player1.marker)
                board.print_cells()
                CPU_response()
            else:
                end_message(board)

if __name__ == '__main__':
    board = Board()



    human = Human()
    cpu = CPU()
    game = Game()
    
    if human_goes_first():
        board.print_cells()
        print board.get_empty_cells()
        human.move(board, human.get_human_move(board), board.p1)
        board.print_cells()
        print board.get_empty_cells()
        human.move(board, human.get_human_move(board), board.p1)
        board.print_cells()
        print board.get_empty_cells()
        
    else:
        print "poop"





