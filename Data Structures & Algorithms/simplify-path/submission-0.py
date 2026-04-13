class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split("/")
        stack = []

        for p in paths:

            if p!="" and p!=".":

                if p == ".." and stack:
                    stack.pop()
                
                elif p!="..":
                    stack.append(p)
        
        return "/"+"/".join(stack)

        