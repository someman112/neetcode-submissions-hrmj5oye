class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        summ = sum(nums)
        if summ % k != 0: return False
        target = summ // k 

        nums.sort(reverse=True)


        sums = [0]*k
        def dfs(i):
            if i == len(nums): return True

            for j in range(k):
                if sums[j] + nums[i] <= target:
                    sums[j]+=nums[i]
                    if dfs(i+1): return True
                    sums[j]-=nums[i]
                
                if sums[j] == 0: break
                
            return False
        
        return dfs(0)