from collections import defaultdict, OrderedDict
class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.key_table = {}
        self.freq_table = defaultdict(OrderedDict)
        self.min_freq = 1
        self.size = 0
    
    def _update(self, key, val=None):
        curr_val, freq = self.key_table[key]
        curr_val = val if val else curr_val

        self.freq_table[freq].pop(key)
        if self.min_freq == freq and len(self.freq_table[freq]) == 0:
            self.min_freq+=1
        
        freq+=1
        self.key_table[key] = [curr_val, freq]
        self.freq_table[freq][key] = None

    def get(self, key: int) -> int:
        if key in self.key_table:
            self._update(key)
            return self.key_table[key][0]
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.key_table:
            self._update(key, value)
            return
        

        if self.size >= self.cap:
            min_key, _ = self.freq_table[self.min_freq].popitem(last=False)
            del self.key_table[min_key]
            self.size-=1
        
        self.key_table[key] = [value, 1]
        self.freq_table[1][key] = None
        self.min_freq = 1 
        self.size+=1
        

        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)