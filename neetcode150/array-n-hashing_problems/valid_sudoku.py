'''
The brute force method is to check every column, row, and 3x3 table
one by one, one after the other.
'''

def brute_force(board: list[list[str]]) -> bool:
    # We know the board is 9x9. 
    n = len(board)
    
    # Each row
    for i in range(n):
        for j in range(n):
            checker = []
            if (board[i][j] not in checker) or (board[i][j] == '.'):
                checker.append(board[i][j])
            else:
                return False
            
    # check all the columns
    for j in range(n):
        for i in range(n):
            checker = []
            if (board[i][j] not in checker) or (board[i][j] == '.'):
                checker.append(board[i][j])
            else:
                return False
            
    # The iteration pattern to check all the boxes in a similar manner
    # is quite complex. I can't seem to figure it out, but perhaps this 
    # is not the best to go
    
    
    # check all the boxes
    for i in range(0, 9, 3):
        checker = []
        for j in range(i, i + 2, 1):
            if (board[i][j] not in checker) or (board[i][j] == '.'):
                checker.append(board[i][j])
            else:
                return False
            
    return True
    
    