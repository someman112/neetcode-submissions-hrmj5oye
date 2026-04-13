class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows,cols = len(board), len(board[0])

        def dfs(i,j):
            if i < 0 or j < 0 or i==rows or j==cols or board[i][j] != "O":
                return 

            board[i][j] = "T"
            for x,y in [(0,1),(1,0),(-1,0),(0,-1)]:
                dfs(i+x,j+y)

        for i in range(rows):
            for j in range(cols):

                if (i in [0, rows-1] or j in [0, cols-1]) and board[i][j] == "O":
                    dfs(i,j)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"

                elif board[i][j] == "T":
                    board[i][j] = "O"  
        