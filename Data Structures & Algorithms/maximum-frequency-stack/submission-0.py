from collections import defaultdict
class FreqStack:

    def __init__(self):
        self.vals_to_freqs = defaultdict(int)
        self.freqs_to_vals = defaultdict(list)
        self.max_freq = 0
        

    def push(self, val: int) -> None:
        self.vals_to_freqs[val]+=1
        self.max_freq = max(self.max_freq, self.vals_to_freqs[val])
        self.freqs_to_vals[self.vals_to_freqs[val]].append(val)
        

    def pop(self) -> int:
        val = self.freqs_to_vals[self.max_freq].pop()
        if not self.freqs_to_vals[self.max_freq]:
            self.max_freq-=1

        self.vals_to_freqs[val]-=1
        return val
        
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()