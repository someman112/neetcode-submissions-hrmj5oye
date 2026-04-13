class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(i,j, indx):
            if indx >= len(word):
                return True 
            
            if (i < 0 or j < 0 or i >= rows or j>=cols or word[indx] != board[i][j]):
                return False
            
            tmp, board[i][j] = board[i][j], "#"
            res = dfs(i+1, j,indx+1) or dfs(i, j+1,indx+1) or dfs(i-1 , j,indx+1) or dfs(i, j-1,indx+1)
            board[i][j] = tmp

            return res
        

        for i in range(rows):
            for j in range(cols):
                
                if dfs(i, j, 0):
                    return True
        
        return False
        