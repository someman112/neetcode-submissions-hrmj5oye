class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Create bitmaps for rows, columns, and 3x3 sub-boxes
        row_bitmap = [[0] * 9 for _ in range(9)]
        col_bitmap = [[0] * 9 for _ in range(9)]
        subbox_bitmap = [[0] * 9 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue
                
                num = int(num) - 1  # Convert to 0-indexed
                subbox_index = (i // 3) * 3 + (j // 3)  # Determine the sub-box index
                
                # Check the row, column, and sub-box for duplicates
                if (row_bitmap[i][num] or col_bitmap[j][num] or subbox_bitmap[subbox_index][num]):
                    return False
                
                # Mark the number as seen
                row_bitmap[i][num] = 1
                col_bitmap[j][num] = 1
                subbox_bitmap[subbox_index][num] = 1

        return True





        