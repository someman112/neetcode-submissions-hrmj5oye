class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        vals = {")":"(", "}":"{", "]":"["}


        for i in s:
            if i in "({[":
                stack.append(i)
            
            elif not stack or stack[-1]!= vals[i]:
                return False

            else:
                stack.pop()

        return not stack
        