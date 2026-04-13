# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return 

        dq = deque()
        while head:
            dq.append(head)
            head = head.next
        
        dummy = ListNode(0)
        head = dummy
        toggle = True

        while dq:
            if toggle:
                nxt = dq.popleft()
            else:
                nxt = dq.pop()
            
            dummy.next = nxt 
            dummy = dummy.next
            toggle = not toggle
        
        dummy.next = None
        