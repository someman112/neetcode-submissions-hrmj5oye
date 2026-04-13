class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summ = sum(nums)
        if summ % 2 != 0:
            return False
        
        target = summ // 2

        sums = {0}
        
        for n in nums:
            curr_sums = set()
            for i in sums:
                curr_sums.add(n + i)

            sums.update(curr_sums)

            if target in sums:
                return True
            
        return False
        