class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols, pd, nd = set(), set(), set()
        res = []

        def recurse(row):
            if row >= n:
                return [[]]
            
            ans = []
            for col in range(n):
                if not (col in cols or (row+col) in pd or (row-col) in nd):
                    string = ("." * col) + "Q" + ("." * (n-col-1))
                    cols.add(col)
                    pd.add(row+col)
                    nd.add(row-col)

                    for rest in recurse(row+1):
                        ans.append([string] + rest)

                    cols.remove(col)
                    pd.remove(row+col)
                    nd.remove(row-col)

            return ans
        
        return recurse(0)
        