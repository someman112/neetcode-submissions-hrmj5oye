class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        visited = set()
        turns=0

        q = deque(['0000'])
        while q:
            lenn = len(q)
            for _ in range(lenn):
                combo = q.popleft()
                if combo == target: return turns

                if combo in visited or combo in deadends:
                    continue

                visited.add(combo)
                for i in range(4):
                    num = int(combo[i])
                    new_num = str((num + 1) % 10)
                    new_num2 = str(num-1) if num-1>=0 else '9'

                    nei1 = combo[0:i] + new_num + combo[i+1:]
                    nei2 = combo[0:i] + new_num2 + combo[i+1:]
                    q.append(nei1)
                    q.append(nei2)
            turns+=1
        
        return -1
                



                
