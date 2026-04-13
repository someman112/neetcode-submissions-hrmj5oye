class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):

            while stack and stack[-1][0] < temperatures[i]:
                val, j = stack.pop()
                output[j] = i - j 
            
            stack.append((temperatures[i], i))
        
        return output


        