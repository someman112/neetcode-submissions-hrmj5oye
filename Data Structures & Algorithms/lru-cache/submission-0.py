from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity: int):
        self.od = OrderedDict()
        self.cap = capacity
        

    def get(self, key: int) -> int:
        if key in self.od:
            self.od.move_to_end(key, last=False)
            return self.od[key]
        return -1
        

    def put(self, key: int, value: int) -> None:

        if key not in self.od and len(self.od) >= self.cap:
            self.od.popitem()
        
        self.od[key] = value
        self.od.move_to_end(key, last=False)
        
