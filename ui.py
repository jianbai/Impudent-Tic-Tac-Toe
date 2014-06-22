#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

def print_instructions(board):
    print "CPU: Welcome to Tic Tac Toe! To play, input your moves as (x,y) coordinates. Our board has 3 rows and 3 columns, numbered 0, 1, and 2:"
    print '\n'
    for row_index, row in enumerate(board.cells):
        for col_index, col in enumerate(row):
            print '(' + str(row_index) + ',' + str(col_index) + ')',
        print '\n'


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

def CPU_goes_first():
    print "CPU: What a gentleman!"

def CPU_response():
    responses = ["Touché...", "Well played", "Hmmm...", "A worthy opponent, you are", "Let's see here... Aha!", "Shrewd move", "Ah, yes... A classic strategy", "I think I see where you're going", "You can't fool me!", "Do you take me for a simpleton?", "Carefully considered", "Delightful!", "Very clever", "A truly formidable challenger!", "A wise decision", "A cunning play", "Your tactics are crafty", "A deft maneuver", "I can see you are quite sharp", "Finally, a worthy foe!", "You are clearly a diligent student of the game... I can respect that", "Good choice", "Careful now!", "Keep your guard up!", "A thrilling contest!", "For each of your thrusts, I shall parry!", "For every action, there must be reaction", "Back and forth until the end of time!", "I was born for this struggle", "Ah, the beauty of the game!", "An unstoppable force meets an immoveable object!", "The best defense is a good offence", "Trial by combat!", "I will not be so easily defeated", "You'll have to do better than that", "You must be one with the board", "Ha!", "Do you think your Wu Tang style can defeat me?", "I will protect this house"]
    print "CPU: " + random.choice(responses)

def win_message():
    print "CPU: You win! Wait, that wasn't supposed to happen..."

def lose_message():
    print "CPU: Sorry, you lose... Better luck next time!"

def draw_message():
    print "CPU: Look's like a draw. We're both winners!"

def restart_message():
    print "CPU: Wasn't that fun? Let's play again!"

def gameover_message(board):
    if board.winner == board.p1:
        win_message()
    elif board.winner == board.blank:
        draw_message()
    elif board.winner == board.p2:
        lose_message()
    restart_message()

def end_message():
    print "CPU: Good game, well played. Bye!"

def play_again():
    again = raw_input("CPU: Would you like to play another game? [y/n]:")
    while True:
        try:
            again.lower() == 'y' or again.lower() == 'n'
        except:
            again = 'x'
        if again.lower() == 'y' or again.lower() == 'n':
            break
        else:
            print "CPU: I didn't catch that. Make sure you enter 'y' or 'n'!"
    if again.lower() == 'y':
        return True
    elif again.lower() == 'n':
        return False
