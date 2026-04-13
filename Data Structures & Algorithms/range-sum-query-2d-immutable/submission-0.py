class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        self.matrix = [[0] * (len(matrix[0])+1) for _ in range(len(matrix)+1)]

        for i in range(1, len(self.matrix)):
            for j in range(1, len(self.matrix[0])):
                val = matrix[i-1][j-1]
                up = self.matrix[i-1][j]
                side = self.matrix[i][j-1]

                self.matrix[i][j] = val + up + side - self.matrix[i-1][j-1]        
                
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1+1, col1+1, row2+1, col2+1

        return self.matrix[row2][col2] - self.matrix[row2][col1-1] - self.matrix[row1-1][col2] + self.matrix[row1-1][col1-1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)