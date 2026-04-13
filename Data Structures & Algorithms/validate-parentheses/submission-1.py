class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {"(":")", "{":"}", "[":"]"}

        for i in s:
            if i in "({[":
                stack.append(i)

            else:
                if not stack:
                    return False

                val = stack.pop()
                if i!= pairs[val]:
                    return False


        return stack == []

        