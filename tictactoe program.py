# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 18:32:28 2020

@author: gandh
"""

def LoadBoard():
    board = []
    file = open('defaultboard.txt', 'r')
    for k in range(9):
        board.append([])
        boardline = file.readline()
        boardline = boardline.rstrip('\n')
        boardline = boardline.rstrip('\t')
        for i in boardline:
            print(i, end='')
            board[k].append(i)
        print('\n')
    file.close()
    print('')
    """
    for i in board:
        print(i)
    """
    return board
    
def makemove(grid, square, player):
    if player == '1':
        row = int(ord(square[0])-ord('A'))
        column = int(square[1])-1
        if grid[row][column] == ".":
            grid[row][column] = 'X'
            Valid = True
        else:
            print("You cannot place there!")
            Valid = False
    if player == '2':
        row = int(ord(square[0])-ord('A'))
        column = int(square[1])-1
        if grid[row][column] == ".":
            grid[row][column] = 'O'
            Valid = True
        else:
            print("You cannot place there!")
            Valid = False
            
    return grid, Valid


def UpdateBoard(grid, square, player, board):
    rows = {'A':[1,2],'B':[4,5],'C':[7,8]}
    columns = {'1':[1,2],'2':[5,6],'3':[9,10]}
    DisplayBoard(board)
    
    if player == '1':
        count = 0
        for i in rows[square[0]]:
            for j in columns[square[1]]:
                r = i
                c = j
                if count == 0:
                    board[r][c] = '\\'
                elif count == 1:
                    board[r][c] = '/'
                elif count == 2:
                    board[r][c] = '/'
                elif count == 3:
                    board[r][c] = '\\'
                count += 1
    
    if player == '2':
        count = 0
        for i in rows[square[0]]:
            for j in columns[square[1]]:
                r = i
                c = j
                if count == 0:
                    board[r][c] = '/'
                elif count == 1:
                    board[r][c] = '\\'
                elif count == 2:
                    board[r][c] = '\\'
                elif count == 3:
                    board[r][c] = '/'
                count += 1
                
    return board

def DisplayBoard(board):
    print("-----------------")
    boardline = [i for i in board]
    for i in boardline:
        line = ""
        for j in i:
            line += j
        print(line + '\n')
    
   
def checkstate(grid):
    win = False
    for row in range(3):
        for column in range(3):
            if grid[row][column] != '.':
                try:
                    if grid[row][column] == grid[row+1][column] and grid[row+1][column] == grid[row+2][column]:
                        win = True
                except:
                    pass
                try:
                    if grid[row][column] == grid[row][column+1] and grid[row][column+1] == grid[row][column+2]:
                        win = True
                except:
                    pass
                try:
                    if grid[row][column] == grid[row+1][column+1] and grid[row+1][column+1] == grid[row+2][column+2]:
                        win = True
                except:
                    pass
                try:
                    if grid[row][column] == grid[row+1][column-1] and grid[row+1][column-1] == grid[row+2][column-2]:
                        win = True  
                except:
                    pass
    return win

def game():
    grid = [["." for i in range(3)] for j in range(3)]
    
    print("Let's play tictactoe!")
    print("To make a move type the row then column.")
    print("")
    board = LoadBoard()
    count = 0
    wincondition = False
    
    while wincondition != True:
        if count%2==0:
            player = '1'
            square = input("Player 1 make your move: ").upper()
            grid, Valid = makemove(grid,square,player)
            if Valid == False:
                print("You lose your move!")
        elif count%2==1:
            player = '2'
            square = input("Player 2 make your move: ").upper()
            grid, Valid = makemove(grid,square,player)
            if Valid == False:
                print("You lose your move!")
        count += 1
        if Valid == True:
            board = UpdateBoard(grid, square, player, board)
            DisplayBoard(board)
            
        wincondition = checkstate(grid)
    if wincondition == True:    
        print("")
        print('player ' + player + ' has won this match!')
    
if __name__ == '__main__':    
    game()