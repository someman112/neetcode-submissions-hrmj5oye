class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def can_split(limit):
            subarrs, curr_sum = 0, 0

            for n in nums:
                if curr_sum + n > limit:
                    subarrs+=1
                    curr_sum=n
                else:
                    curr_sum+=n

            return subarrs+1<=k


        start,end = max(nums), sum(nums)
        while start<=end:
            mid = (start+end)//2

            if can_split(mid):
                end=mid-1
            
            else:
                start=mid+1
        
        return start

        