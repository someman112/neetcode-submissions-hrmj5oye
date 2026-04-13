class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n = len(matrix), len(matrix[0])
        UP,DOWN,LEFT,RIGHT = 0,1,2,3
        ans = []
        i,j = 0,0
        dr = RIGHT

        for _ in range(m*n):
            ans.append(matrix[i][j])
            matrix[i][j] = -101
            
            if dr == RIGHT:
                if j+1 == n or matrix[i][j+1] == -101:
                    i+=1
                    dr = DOWN
                else:
                    j+=1
            
            elif dr == DOWN:
                if i+1 == m or matrix[i+1][j] == -101:
                    j-=1
                    dr = LEFT
                else:
                    i+=1
            
            elif dr == LEFT:
                if j-1<0 or matrix[i][j-1] == -101:
                    i-=1
                    dr = UP
                else:
                    j-=1
            
            elif dr == UP:
                if i-1<0 or matrix[i-1][j] == -101:
                    j+=1
                    dr = RIGHT
                else:
                    i-=1
        return ans