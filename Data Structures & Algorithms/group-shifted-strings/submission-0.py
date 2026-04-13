class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        groups=defaultdict(list)

        for s in strings:
            key=[]

            for i in range(1, len(s)):
                key.append((ord(s[i]) - ord(s[i-1]))%26)
            
            groups[tuple(key)].append(s)
        
        return [groups[key] for key in groups]
            




