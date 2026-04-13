class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ds = []
        ans = []


        for st in strs:

            curr_d = {}

            for i in st:
                if i in curr_d:
                    curr_d[i]+=1
                else:
                    curr_d[i] = 1
            
            if curr_d not in ds:
                ds.append(curr_d)
                ans.append([])

            if curr_d in ds:
                ans[ds.index(curr_d)].append(st)
            
            else:
                ans.append([st])
        
        return ans






        