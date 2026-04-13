class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:


        p1 = 0
        p2 = len(numbers) - 1


        while True:
            summ = numbers[p1] + numbers[p2]
            if summ == target:
                return [p1+1, p2+1]

            elif summ > target:
                p2-=1
            
            else:
                p1+=1
            

        