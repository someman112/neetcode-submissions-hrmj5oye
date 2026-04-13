class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        

        rest = self.permute(nums[1:])

        answer = []
        for permutation in rest:

            for i in range(len(permutation)+1):
                answer.append(permutation[0:i] + [nums[0]] + permutation[i:])
        
        return answer
        