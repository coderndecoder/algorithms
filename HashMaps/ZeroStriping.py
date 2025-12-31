# Replaces numbers with 0s in rows and columns for any 0 found in an m*n matrix

from typing import List

matrix=[[3,1,6,3,5,8,4,7,2],
        [5,2,4,5,2,5,8,4,7],
        [6,8,7,2,3,1,5,3,1],
        [1,7,2,5,8,2,3,2,7],
        [9,0,6,8,6,0,4,8,5],
        [3,5,9,8,9,6,6,6,3],
        [7,3,5,2,7,8,2,5,2],
        [4,0,3,5,2,8,2,7,4]
]

def flip_columns(row: int, col: int):
    for r in range(row):
       matrix[r][col] = 0
def flip_rows(row: int, col: int):
    for c in range(col):
        matrix[row][c] = 0 

def flip_numbers_single_pass():
    m, n = len(matrix), len(matrix[0])
    #hashmap to track 0s in row and col
    row_map = {}
    col_map = {}
    
    for row in range(m):
        for col in range(n):
            if matrix[row][col] == 0:
                if row not in row_map:
                    flip_rows(row,col)
                    row_map[row] = 1
                
                if col not in col_map:
                    flip_columns(row, col)
                    col_map[col] = 1
                    
            elif row in row_map or col in col_map:
                matrix[row][col] = 0
                
                
def print_matrix():
    m = len(matrix)
    for row in range(m):
            print(matrix[row])
             
              
    
flip_numbers_single_pass()
print_matrix()
    