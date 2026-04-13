class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        iters=0
        while left!=right:
            left>>=1
            right>>=1
            iters+=1
        
        return left<<iters