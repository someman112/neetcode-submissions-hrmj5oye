class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        output = []
        nums = sorted(nums)
        prev = None

        for i in range(len(nums)):
            a = nums[i]
            if prev == a:
                continue
            else:
                prev = a


            lp = i+1
            rp = len(nums) - 1
            b = None
            c = None

            while lp < rp:
                summ = nums[lp] + nums[rp]

                if summ == a * -1 and nums[lp]!=b and nums[rp]!=c:
                    output.append([a, nums[lp], nums[rp]])
                    b = nums[lp]
                    c = nums[rp]
                    lp = lp+1
                    rp = len(nums) - 1

                elif summ < a * -1:
                    lp+=1
                else:
                    rp-=1

        return output



            







        