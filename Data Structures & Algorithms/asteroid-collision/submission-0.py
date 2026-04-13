class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            stack.append(a)

            while len(stack) > 1 and stack[-2] > 0 and stack[-1] < 0:

                if abs(stack[-1]) == abs(stack[-2]):
                    stack.pop(); stack.pop()
                
                elif abs(stack[-2]) > abs(stack[-1]):
                    stack.pop()
                
                else:
                    stack.pop(-2)

        return stack

            
        