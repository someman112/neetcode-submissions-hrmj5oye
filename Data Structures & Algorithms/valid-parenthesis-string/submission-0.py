class Solution:
    def checkValidString(self, s: str) -> bool:
        left_min, left_max = 0, 0 


        for i in s:

            if i == "(":
                left_min+=1
                left_max+=1
            
            elif i == ")":
                left_min-=1
                left_max-=1
            
            else:
                left_min-=1
                left_max+=1
            
            if left_max < 0:
                return False
            
            left_min = max(0, left_min)

        return left_min == 0
        