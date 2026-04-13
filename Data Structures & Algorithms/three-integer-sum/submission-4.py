class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums = sorted(nums)
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            lp = i + 1
            rp = len(nums) - 1

            while lp < rp:
                summ = nums[lp] + nums[rp]

                if summ == -nums[i]:
                    output.append([nums[i], nums[lp], nums[rp]])
                    lp += 1

                    
                    while lp < rp and nums[lp] == nums[lp - 1]:
                        lp += 1
        

                elif summ < -nums[i]:
                    lp += 1
                else:
                    rp -= 1

        return output



            







        