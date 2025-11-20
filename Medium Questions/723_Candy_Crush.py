"""
QUESTION:

Given a 2D integer array board representing the grid of candy, different positive integers board[i][j] represent different types of candies. A value of board[i][j] = 0 represents that the cell at position (i, j) is empty. The given board represents the state of the game following the player's move. Now, you need to restore the board to a stable state by crushing candies according to the following rules:

If three or more candies of the same type are adjacent vertically or horizontally, "crush" them all at the same time - these positions become empty.
After crushing all candies simultaneously, if an empty space on the board has candies on top of itself, then these candies will drop until they hit a candy or bottom at the same time. (No new candies will drop outside the top boundary.)
After the above steps, there may exist more candies that can be crushed. If so, you need to repeat the above steps.
If there does not exist more candies that can be crushed (ie. the board is stable), then return the current board.

You need to perform the above rules until the board becomes stable, then return the current board.
"""

from typing import List

def candyCrush(board: List[List[int]]) -> List[List[int]]:
    ROWS, COLS = len(board), len(board[0])
    isStable = True
    # Check and Tag Rows
    for i in range(ROWS):
        for j in range(len(board[i]) - 2):
            num1 = abs(board[i][j])
            num2 = abs(board[i][j + 1])
            num3 = abs(board[i][j + 2])

            if num1 == num2 == num3 and num1 != 0:
                board[i][j] = -num1
                board[i][j + 1] = -num2
                board[i][j + 2] = -num3
                isStable = False

    # Check and Tag Columns
    for j in range(COLS):
        for i in range(ROWS - 2):
            num1 = abs(board[i][j])
            num2 = abs(board[i + 1][j])
            num3 = abs(board[i + 2][j])

            if num1 == num2 == num3 and num1 != 0:
                board[i][j] = -num1
                board[i + 1][j] = -num2
                board[i + 2][j] = -num3
                isStable = False

    # Gravity
    if not isStable:
        for j in range(COLS):
            idx = ROWS - 1
            for i in range(ROWS - 1, -1, -1):
                if board[i][j] > 0:
                    board[idx][j] = board[i][j]
                    idx -= 1
            
            while idx >= 0:
                board[idx][j] = 0
                idx -= 1
    
    return board if isStable else candyCrush(board)

board = [[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]
output =  [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[110,0,0,0,114],[210,0,0,0,214],[310,0,0,113,314],[410,0,0,213,414],[610,211,112,313,614],[710,311,412,613,714],[810,411,512,713,1014]]

result = candyCrush(board)
print(output == result)
