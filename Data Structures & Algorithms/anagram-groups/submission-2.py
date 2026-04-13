class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keymap = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            keymap[key].append(s)
        
        return [keymap[key] for key in keymap]