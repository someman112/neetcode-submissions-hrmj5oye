class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxs = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]


                if val == ".":
                    continue                
                
                # row check    
                if val in rows[r]:
                    return False
                else:
                    rows[r].add(val)

                # col check
                if val in cols[c]:
                    return False
                else:
                    cols[c].add(val)

                # box check
                box_id = (r // 3) * 3 + (c // 3)
                if val in boxs[box_id]:
                    return False
                else:
                    boxs[box_id].add(val)

        return True

                


        