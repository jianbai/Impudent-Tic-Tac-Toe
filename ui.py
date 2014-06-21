#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
from board import Board

def print_instructions():
    print "CPU: Welcome to Tic Tac Toe! Our board has 3 rows and 3 columns, each numbered 0, 1, and 2. To play, input your moves as (x,y) coordinates."

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
        lose_message()
    restart_message()

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
