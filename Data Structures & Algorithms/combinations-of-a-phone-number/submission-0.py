class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {"2": "abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}

        def gencombs(s):
            if not s:
                return []
                
            if len(s) == 1:
                return [i for i in mapping[s]]

            first = [i for i in mapping[s[0]]]
            rest =  gencombs(s[1:])

            result = []
            for i in first:
                for j in rest:
                    result.append(i + j)
            
            return result
        
        return gencombs(digits)
        