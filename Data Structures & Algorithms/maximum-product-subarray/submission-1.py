class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = max(nums)
        maxx, minn = 1, 1 

        for i in nums:
            tmp_maxx = maxx
            maxx = max(i * maxx, i * minn, i)
            minn = min(i * tmp_maxx, i * minn, i)

            ans = max(ans, maxx)

            maxx = 1 if maxx == 0 else maxx
            minn = 1 if minn == 0 else minn
        
        return ans
        