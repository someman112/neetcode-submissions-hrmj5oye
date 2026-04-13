class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]

        
        rest = self.subsets(nums[1:])

        return [[nums[0]] + part for part in rest] + rest
        