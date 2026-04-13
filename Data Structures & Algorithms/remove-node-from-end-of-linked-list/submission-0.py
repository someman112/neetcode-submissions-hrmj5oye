# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ll = 0
        curr = head

        while curr:
            ll+=1
            curr=curr.next
        ll = ll - n

        if ll == 0:
            head = head.next
            return head 
            
        i = 1
        curr = head
        while i < ll and curr is not None:
            curr = curr.next
            i+=1
        
        if curr.next is not None:
            curr.next = curr.next.next
            return head
        