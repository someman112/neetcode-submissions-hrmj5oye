class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        N = len(temperatures)
        output = [0] * N
        stack = []
        
        for i in range(N):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                elem = stack.pop()
                output[elem] = i - elem

            stack.append(i)

        return output  
        