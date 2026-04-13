class Solution:
    def minEnd(self, n: int, x: int) -> int:
        ans=x
        k=n-1
        pos=0

        while k>0:
            
            #if ans' bit at position `pos` is 0
            if ans&(1<<pos)==0:

                # if lowest bit of k is 1, then set it
                if k & 1: ans|=(1<<pos) 
                k>>=1
            
            pos+=1
        
        return ans