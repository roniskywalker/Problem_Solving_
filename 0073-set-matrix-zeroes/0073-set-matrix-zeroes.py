class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row_size, col_size = len(matrix), len(matrix[0])
        row_zero = 1
        for i in range(row_size):
            for j in range(col_size):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    if i == 0:
                        row_zero = 0
                    else:
                        matrix[i][0] = 0
        for i in range(1, row_size):
            for j in range(1, col_size):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        if matrix[0][0] == 0:
            for i in range(row_size):
                matrix[i][0] = 0
        if row_zero == 0:
            for j in range(col_size):
                matrix[0][j] = 0