class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        carry = (a&b) << 1
        summ = a^b

        while mask&carry > 0:
            summ, carry = summ^carry, (summ&carry)<<1

        return mask&summ if carry > 0 else summ
        