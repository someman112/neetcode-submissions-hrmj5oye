class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = [(position[i], speed[i]) for i in range(len(speed))]
        arr.sort(key=lambda x: x[0], reverse=True)
        
        stack = []
        for elem in arr:
            time = (target - elem[0]) / elem[1]
            
            if not stack or stack[-1] < time:
                stack.append(time)

        return len(stack)
        