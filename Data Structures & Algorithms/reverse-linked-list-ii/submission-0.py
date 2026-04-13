# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=ListNode(-1, head)
        start=dummy
        left_node=head

        for _ in range(left-1):
            left_node=left_node.next
            start=start.next
        
        reverse_start=left_node
        prev=None

        for _ in range(right-left+1):
            nxt = left_node.next
            left_node.next = prev
            prev = left_node
            left_node = nxt
        
        reverse_start.next=left_node
        start.next=prev

        return dummy.next

        

        




        