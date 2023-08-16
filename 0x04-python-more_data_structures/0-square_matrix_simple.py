#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    row_len = len(matrix)
    col_len = len(matrix[0])

    sqrd_matrix = [[0 for j in range(col_len)] for i in range(row_len)]
    for i in range(row_len):
        for j in range(col_len):
            sqrd_matrix[i][j] = matrix[i][j] ** 2
            
    return sqrd_matrix
