class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1,nums2=nums2,nums1

        total=len(nums1)+len(nums2)
        half = total // 2

        start,end = 0, len(nums1)

        while True:
            mid = (start+end) // 2
            mid2 = half - mid

            left1 = nums1[mid-1] if mid > 0 else float("-inf")
            right1 = nums1[mid] if mid < len(nums1) else float("inf")

            left2 = nums2[mid2-1] if mid2 > 0 else float("-inf")
            right2 = nums2[mid2] if mid2 < len(nums2) else float("inf")

            if left1<=right2 and left2<=right1:

                if total%2:
                    return min(right1, right2)

                return (max(left1, left2) + min(right1, right2)) / 2 
            
            elif left1 > right2:
                end = mid-1
            
            else:
                start = mid+1
        



        