import random 
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def quicksort(i,j):
            if j-i<=0:
                return
            
            idx = random.randint(i, j)
            nums[idx], nums[i] = nums[i], nums[idx]
            pvt = nums[i]

            start, end = i+1, j
            while True:
                
                while start<=end and nums[start] < pvt:
                    start+=1
                while start<=end and nums[end] > pvt:
                    end-=1

                if end < start:
                    break
                
                nums[start], nums[end] = nums[end], nums[start]
                start+=1
                end-=1

            nums[i], nums[end] = nums[end], nums[i]

            quicksort(i, end-1)
            quicksort(end+1, j)

        quicksort(0, len(nums)-1)
        return nums


        