class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1,nums2 = nums2,nums1
        
        m,n = len(nums1), len(nums2)

        l,r = 0, m
        lenn = m + n
        half = lenn // 2

        while l<=r:
            m1 = (l + r) // 2
            m2 = half - m1

            left1 = nums1[m1-1] if m1 > 0 else float("-inf")
            right1 = nums1[m1] if m1 < m  else float("inf")

            left2 = nums2[m2-1] if m2 > 0 else float("-inf")
            right2 = nums2[m2] if m2 < n else float("inf")

            if left1 <= right2 and left2 <= right1:

                if lenn % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2 
                else:
                    return min(right1, right2)
            
            elif left1 > right2:
                r = m1 - 1
            
            else:
                l = m1 + 1 



              
        

        
        
        
        