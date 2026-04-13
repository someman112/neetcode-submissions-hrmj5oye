class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in s:
            if i!= "]":
                stack.append(i)

            else:
                string = ""
                while stack:
                    val = stack.pop()
                    if val == "[":
                        break    
                    string = val + string
                
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                
                string = int(num) * string
                for s in string:
                    stack.append(s)
                    
        return "".join(stack)
                


        