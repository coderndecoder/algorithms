#Given 9X9 sudoku board, determin if current state of board is valid
# 1. each row and column contains unique number(1 and 9) or 0s - empty
# 2. Each 3x3 matrix muct contain unique numbers between 1 and 9
# Return True or False

from typing import List

board=[ [3,0,6,0,5,8,4,0,0],
        [5,2,0,0,0,0,0,0,0],
        [0,8,7,0,0,0,0,3,1],
        [1,0,2,5,0,0,3,2,0],
        [9,0,0,8,6,3,0,0,5],
        [0,5,0,0,9,0,6,0,0],
        [0,3,0,0,0,8,2,5,0],
        [0,1,0,0,2,0,0,7,4],
        [0,0,5,2,0,6,0,0,0]
]

def find_status_single_pass()-> bool:
    
    hashmap = {}
    col_set = [set() for _ in range(9)]
    subgrid = [[set() for _ in range(3)] for _ in range(3)]
    
    for row in range(9):
        for col in range(9):
            num = board[row][col]
            if num == 0:
                continue
            # find in row
            if num in hashmap:
                #print(num, " ", hashmap[num])
                return False
            hashmap[num] = (row,col)
            # find in col
            if num in col_set[col]: 
                #print(num, " ", col_set[col])
                return False
            else:
                col_set[col].add(num)
                
            # subgrid check
            if num in subgrid[row//3][col//3]:
                #print(num, " ", subgrid[row//3][col//3])
                return False
            else:
                subgrid[row//3][col//3].add(num)
                
        hashmap.clear()    
        
    return True
    
print(find_status_single_pass())
