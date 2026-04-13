class LL:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        self.vals = [LL(-1,-1) for _ in range(10**4)]


    def put(self, key: int, value: int) -> None:
        node = self.vals[key % 10**4]

        while node.next:
            if node.next.key == key:
                node.next.val = value
                return 
            node = node.next
        node.next = LL(key, value)
        

    def get(self, key: int) -> int:
        node = self.vals[key % 10**4]
        
        while node:
            if node.key == key:
                return node.val
            node = node.next

        return -1
        

    def remove(self, key: int) -> None:
        node = self.vals[key % 10**4]

        while node.next:
            if node.next.key == key:
                node.next = node.next.next
                return
            node = node.next