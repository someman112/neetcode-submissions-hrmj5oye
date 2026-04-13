class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr)<2: return 1
        SIGN = None
        n=len(arr)
        curr_len=1
        max_len=float("-inf")
        
        i=1
        while i<n:
            if arr[i-1] < arr[i]:
                if SIGN==">":
                    curr_len+=1
                else:
                    curr_len=2
                SIGN = "<"
                
            elif arr[i-1] > arr[i]:
                if SIGN=="<":
                    curr_len+=1
                else:
                    curr_len=2
                SIGN = ">"
            else:
                curr_len=1
                SIGN=None
                
            max_len=curr_len if curr_len > max_len else max_len
            i+=1
        
        return max_len