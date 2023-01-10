import sys
import numpy as np
import matplotlib.pyplot as plt

'''
The function of finding the best move from any position (stockfish has not yet been implemented)
'''



def find_best_move(piece, board, row, col):
    if piece == "N":
        if (row-2 >= 0 and col-1 >= 0) and board[row-2][col-1] == 0:
            board[row-2][col-1] = 1
            return board
        elif (row-2 >= 0 and col+1 < len(board[0])) and board[row-2][col+1] == 0:
            board[row-2][col+1] = 1
            return board
        elif (row+2 < len(board) and col-1 >= 0) and board[row+2][col-1] == 0:
            board[row+2][col-1] = 1
            return board
        elif (row+2 < len(board) and col+1 < len(board[0])) and board[row+2][col+1] == 0:
            board[row+2][col+1] = 1
            return board
        elif (row-1 >= 0 and col-2 >= 0) and board[row-1][col-2] == 0:
            board[row-1][col-2] = 1
            return board
        elif (row-1 >= 0 and col+2 < len(board[0])) and board[row-1][col+2] == 0:
            board[row-1][col+2] = 1
            return board
        elif (row+1 < len(board) and col-2 >= 0) and board[row+1][col-2] == 0:
            board[row+1][col-2] = 1
            return board
        elif (row+1 < len(board) and col+2 < len(board[0])) and board[row+1][col+2] == 0:
            #Move the knight down 1 and right 2
            board[row+1][col+2] = 1
            #Return the new board
            return board
        #If the knight can't move anywhere, return the original board
        else:
            return board
    #Check if piece is a bishop
    elif piece == "B":
        #Check if the bishop can move up and left
        if row-1 >= 0 and col-1 >= 0:
            #Move the bishop up and left
            board[row-1][col-1] = 1
            #Return the new board
            return board
        #Check if the bishop can move up and right
        elif row-1 >= 0 and col+1 < len(board[0]):
            #Move the bishop up and right
            board[row-1][col+1] = 1
            #Return the new board
            return board
        #Check if the bishop can move down and left
        elif row+1 < len(board) and col-1 >= 0:
            #Move the bishop down and left
            board[row+1][col-1] = 1
            #Return the new board
            return board
        #Check if the bishop can move down and right
        elif row+1 < len(board) and col+1 < len(board[0]):
            #Move the bishop down and right
            board[row+1][col+1] = 1
            #Return the new board
            return board
        #If the bishop can't move anywhere, return the original board
        else:
            return board
    #Check if piece is a rook
    elif piece == "R":
        #Check if the rook can move up
        if row-1 >= 0:
            #Move the rook up
            board[row-1][col] = 1
            #Return the new board
            return board
        #Check if the rook can move down
        elif row+1 < len(board):
            #Move the rook down
            board[row+1][col] = 1
            #Return the new board
            return board
        #Check if the rook can move left
        elif col-1 >= 0:
            #Move the rook left
            board[row][col-1] = 1
            #Return the new board
            return board
        #Check if the rook can move right
        elif col+1 < len(board[0]):
            #Move the rook right
            board[row][col+1] = 1
            #Return the new board
            return board
        #If the rook can't move anywhere, return the original board
        else:
            return board
    #Check if piece is a queen
    elif piece == "Q":
        #Check if the queen can move up and left
        if row-1 >= 0 and col-1 >= 0:
            #Move the queen up and left
            board[row-1][col-1] = 1
            #Return the new board
            return board
        #Check if the queen can move up and right
        elif row-1 >= 0 and col+1 < len(board[0]):
            #Move the queen up and right
            board[row-1][col+1] = 1
            #Return the new board
            return board
        #Check if the queen can move down and left
        elif row+1 < len(board) and col-1 >= 0:
            #Move the queen down and left
            board[row+1][col-1] = 1
            #Return the new board
            return board
        #Check if the queen can move down and right
        elif row+1 < len(board) and col+1 < len(board[0]):
            #Move the queen down and right
            board[row+1][col+1] = 1
            #Return the new board
            return board
        #Check if the queen can move up
        elif row-1 >= 0:
            #Move the queen up
            board[row-1][col] = 1
            #Return the new board
            return board
        elif row+1 < len(board):
            board[row+1][col] = 1
            return board
        elif col-1 >= 0:
            board[row][col-1] = 1
            return board
        elif col+1 < len(board[0]):
            board[row][col+1] = 1
            return board
        else:
            return board
    elif piece == "K":
        if row-1 >= 0 and col-1 >= 0:
            board[row-1][col-1] = 1
            return board
        elif row-1 >= 0 and col+1 < len(board[0]):
            board[row-1][col+1] = 1
            return board
        elif row+1 < len(board) and col-1 >= 0:
            board[row+1][col-1] = 1
            return board
        elif row+1 < len(board) and col+1 < len(board[0]):
            board[row+1][col+1] = 1
            return board
        elif row-1 >= 0:
            board[row-1][col] = 1
            return board
        elif row+1 < len(board):
            board[row+1][col] = 1
            return board
        elif col-1 >= 0:
            board[row][col-1] = 1
            return board
        elif col+1 < len(board[0]):
            board[row][col+1] = 1
            return board
        else:
            return board

    elif piece == "P":
        if row-1 >= 0:
            board[row-1][col] = 1
            return board
        else:
            return board
    else:
        return board
