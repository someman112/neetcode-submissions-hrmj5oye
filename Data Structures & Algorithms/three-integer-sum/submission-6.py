class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        N = len(nums)
        triplets = []

        for idx in range(N - 2):
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue 

            target = nums[idx] * -1
            i,j = idx+1, N -1 

            while i < j:
                curr_val = nums[i] + nums[j]

                if curr_val < target:
                    i+=1
                elif curr_val > target:
                    j-=1

                else:
                    triplets.append([nums[idx], nums[i], nums[j]])
                    i+=1
                    j-=1

                    while i < j and nums[i] == nums[i-1]:
                        i+=1
                    while i < j and nums[j] == nums[j+1]:
                        j-=1
                        
        return triplets   