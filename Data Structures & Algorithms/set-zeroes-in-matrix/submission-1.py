class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m,n = len(matrix), len(matrix[0])
        first_row,first_col = False,False


        for i in range(m):
            for j in range(n):

                if matrix[i][j] == 0:
                    first_row = True if i == 0 else first_row
                    first_col = True if j == 0 else first_col

                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1,m):
            for j in range(1,n):

                if matrix[i][j] == 0 or matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        
        if first_row:
            matrix[0] = [0] * n
        
        if first_col:
            for i in range(m):
                matrix[i][0] = 0
        
        