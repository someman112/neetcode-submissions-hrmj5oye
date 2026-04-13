# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None: return head



        def gcd(a, b):
            if b==0: return a
            return gcd(b, a % b)

        prev=None
        curr=head

        while curr.next is not None:
            prev=curr
            nxt = curr.next
            gcd_node = ListNode(gcd(prev.val, nxt.val),nxt)
            prev.next=gcd_node
            curr = nxt
        
        return head