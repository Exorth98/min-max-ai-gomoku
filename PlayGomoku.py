'''
Created on 4 avr. 2019

@author: CAILLIEUX
'''

import os
from GomokuV2 import *
from GlobalVariables import *

def initiateBoard():
    board = [' '] * 15
    for i in range(15):
        board[i] = [' '] * 15
    return board

def choose(text, min = 7, max = 7):
    while 1 :
        print("Choisir "+text+" : ")
        nombre = input()
        try:
            nb = int(nombre)
            if nb>= 1 and (nb<=min or nb>=max) and nb<=15 :
                return nb-1
        except:
            print("Pas un nombre entre 1 et 15")    

def chooseLetter(text, min = 7, max = 7):
    while 1 :
        print("Choisir "+text+" : ")
        lettre = input()
        try:
            nb = ConvertToInt(lettre)
            if nb>-1 and (nb <= min or nb >= max):
                return nb
        except:
            print("Pas une lettre entre conforme")   

def playReal(board):
    print("A toi de jouer !")
    isOk = False
    while isOk == False :
        i = chooseLetter("la ligne (lettre entre A et O)",7,7)
        j = choose("la colonne (nombre entre 1 et 15)",7,7)
        if board[i][j] == ' ':
            isOk = True
        else:
            print("Case invalide")

    board[i][j] = user
    printBoard(board)

def playReal3(board):
    global user
    print("A toi de jouer !")
    isOk = False
    while isOk == False :
        i = chooseLetter("la ligne (lettre hors E et K)",3,11)
        j = choose("la colonne (nombre hors 5 et 11)",4,12)
        if board[0][j] == ' ':
            isOk = True
        else:
            print("Impossible sur cette case")

    board[i][j] = user
    printBoard(board)

def printWinner(winner):
    if winner == 'Draw':
        print("Egalité !")
    else:
        print("Victoire de {}".format(winner))

def play(board):
    global playing
    global ai
    global user
    global round
    if(playing == ai):
        playing = user
        playAI(board,0,user,ai)
    else:
        playing = ai
        if(round == 1):
            print("Premier coup en tant que noir (o) au centre")
            board[7][7] = user
            printBoard(board)
        elif(round == 3):
            playReal(board)
        else:
            playReal(board)
    round +=1

def main():
    global winner
    global board
    global user
    global ai

    print("Voulez vous commencez ? (pions noirs)  (y/n)")
    rep = input()
    if(rep == 'y'):
        user = 'N'
        ai = 'R'

    board = initiateBoard()
    printBoard(board)


    while(winner == 'Nobody'):
        play(board)
        winner = TerminalTest(board,user,ai)
    
    printWinner(winner)
    os.system("pause")


main()