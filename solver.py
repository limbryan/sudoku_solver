import numpy as np
import matplotlib.pyplot as plt

# Takes in a position in the board and outputs if it is possible or not to put the number n inside 
def possible(board,x,y,n):

    # checks the row 
    for i in range(len(board[0])):
        # exits the function straightaway if the number n already exists in the row
        if board[x][i] == n:
            return False

    # checks the column 
    for j in range(len(board[0])):
        if board[j][y] == n:
            return False

    # first determine which of the 9 major boxes the x-y position is in
    # it doest not matter where in box it is, becasue we haev to check the whole box
    # so we just have to determine which of the box it is in

    x_b = (x//3)*3
    y_b = (y//3)*3
    # check the same box
    for ib in range(3):
        for jb in range(3):
            # checking the entire box the x-y is in 
            if board[x_b+ib][y_b+jb] == n:
                return False
        
    # if it passes all the rules return True 
    return True 


def solve(board):   
    for x in range(9):
        for y in range(9):
            if board[x][y] == 0:
                for n in range(1,10):
                    res = possible(board,x,y,n)
                    if res ==True:
                        board[x][y] = n
                        # further solve again - recursion
                        # the recursion just means going deepre into a tree/node
                        solve(board)

                        # this leaves the option that going deeper into the tree did not work so it remains empty as the previous branch was a wrong move
                        board[x][y] = 0 #NEEDED 
                return board
    print("Solved")
    print(np.matrix(board))
    #input("More")

#initalise the sudoku board as a list
board = [[5,3,0,0,7,0,0,0,0],
         [6,0,0,1,9,5,0,0,0],
         [0,9,8,0,0,0,0,6,0],
         [8,0,0,0,6,0,0,0,3],
         [4,0,0,8,0,3,0,0,1],
         [7,0,0,0,2,0,0,0,6],
         [0,6,0,0,0,0,2,8,0],
         [0,0,0,4,1,9,0,0,5],
         [0,0,0,0,8,0,0,7,9]]
print(board)

#just for viewing purposes - we are doing this sovler with lists only though we can do it with numpy arrays as well
board_np = np.matrix(board)
print(board_np)


# this is the main function
solve(board)

