class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        N = len(s)
        if N == 0 or N == 1:
            return N

        seen = set()
        l, r = 0, 0 
        diff = 0

        while r < N:

            while s[r] in seen:
                seen.remove(s[l])
                l+=1

            seen.add(s[r])
            r+=1
            diff = max(diff, r - l)

        return diff
        