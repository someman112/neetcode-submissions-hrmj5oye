class ListNode:
    def __init__(self, val, nxt):
        self.val=val
        self.next=nxt
    

class MyCircularQueue:

    def __init__(self, k: int):
        self.head=ListNode(-1, None)
        
        curr=self.head
        for _ in range(k-1):
            curr.next = ListNode(-1, None)
            curr=curr.next
        
        curr.next=self.head

        self.dq,self.enq=self.head,self.head


    def enQueue(self, value: int) -> bool:
        if self.isEmpty():
            self.enq.val = value
            return True
        
        elif self.enq.next.val ==-1:
            self.enq.next.val=value
            self.enq=self.enq.next
            return True

        return False

    def deQueue(self) -> bool:
        if self.dq.val!=-1:
            self.dq.val=-1

            if self.dq.next.val!=-1:
                self.dq = self.dq.next
            
            return True 

        return False
        

    def Front(self) -> int:
        return self.dq.val
        

    def Rear(self) -> int:
        return self.enq.val
        

    def isEmpty(self) -> bool:
        return self.dq.val==-1
        

    def isFull(self) -> bool:
        return self.enq.next.val!=-1
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()