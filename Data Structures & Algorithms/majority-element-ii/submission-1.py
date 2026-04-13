class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        can1, cnt1, can2, cnt2 = None, 0, None, 0


        for n in nums:
            if can1 == n:
                cnt1+=1
            
            elif can2 == n:
                cnt2+=1
            
            elif cnt1 == 0:
                can1, cnt1 = n, 1
            
            elif cnt2 == 0:
                can2, cnt2 = n, 1
            
            else:
                cnt1-=1
                cnt2-=1
            
        return [i for i in set([can1, can2]) if nums.count(i) > len(nums) // 3 ]
        