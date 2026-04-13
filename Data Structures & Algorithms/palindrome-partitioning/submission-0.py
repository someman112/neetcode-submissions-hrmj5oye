class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def recurse(string):

            if not string:
                return [[]]

            
            res = []

            for i in range(1, len(string)+1):
                prefix = string[:i]
                suffix = string[i:]

                if prefix == prefix[::-1]:
                    for partitions in recurse(suffix):
                        res.append([prefix] + partitions)

            return res

        return recurse(s) 
        