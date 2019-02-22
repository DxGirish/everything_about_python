import numpy as np


def print_diagonal(matrx, row, column, cols):
    col = cols
    while row >= 0 and col < column:
        print(matrx[row][col], end=' ')
        row -= 1
        col += 1


# a = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
rows = 4
columns = 5
c = np.arange(1, 21).reshape(rows, columns)
print(c[0, 0], '\n')
row_start = 1
col_start = 1
while row_start < rows + columns - 1 and col_start < columns:
    if row_start < rows:
        print_diagonal(c, row_start, columns, 0)
        row_start += 1
    else:
        print_diagonal(c, rows - 1, columns, col_start)
        col_start += 1
    print('\n')
