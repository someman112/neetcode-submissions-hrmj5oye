class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_l = min(len(i) for i in strs)
        ans = []

        for i in range(min_l):
            ltr = strs[0][i]

            for j in range(1, len(strs)):
                if strs[j][i] != ltr:
                    return "".join(ans)
                    
            ans.append(ltr)
        return "".join(ans)
        