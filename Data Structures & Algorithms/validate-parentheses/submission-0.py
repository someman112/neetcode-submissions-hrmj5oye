class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {"(":")", "[":"]", "{":"}"}
        dvals = ")]}"
        i = 0

        while i < len(s):

            if s[i] in d:
                stack.append(s[i])
            
            elif s[i] in dvals:
                if stack == []:
                    return False

                itm = stack.pop()
                if d[itm] != s[i]:
                    return False

            i+=1
            
        return stack == []


        