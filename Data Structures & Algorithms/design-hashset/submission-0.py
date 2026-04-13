class LL:

    def __init__(self, val):
        self.val = val
        self.next = None

class MyHashSet:

    def __init__(self):
        self.set = [LL(-1) for _ in range(10**4)]
    

    def add(self, key: int) -> None: 
        node = self.set[key % (10**4)]
        while node.next:
            if node.next.val == key:
                return
                
            node = node.next
        node.next = LL(key)  

    def remove(self, key: int) -> None:
        node = self.set[key % (10**4)]

        while node.next:
            if node.next.val == key:
                node.next = node.next.next
                return
            node = node.next
        

    def contains(self, key: int) -> bool:
        node = self.set[key % (10**4)]

        while node.next:
            if node.next.val == key:
                return True
            node = node.next 
        return False