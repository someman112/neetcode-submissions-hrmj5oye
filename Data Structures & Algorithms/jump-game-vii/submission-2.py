class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q = deque([0])
        r=0
        n = len(s)

        while q:
            idx = q.popleft()
            if idx==n-1: return True

            start=max(idx+minJump, r+1)
            end  =min(idx+maxJump+1, n)

            for i in range(start, end):
                if s[i]=="0": q.append(i)
            
            r = idx+maxJump
        return False
