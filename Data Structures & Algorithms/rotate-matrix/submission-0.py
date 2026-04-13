class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        end = n - 1

        for row in range(n // 2):

            for col in range(row, end-row):
                temp = matrix[row][col]
                matrix[row][col] = matrix[end-col][row]
                matrix[end-col][row] = matrix[end-row][end-col]

                matrix[end-row][end-col] = matrix[col][end-row]
                matrix[col][end-row] = temp
        


        