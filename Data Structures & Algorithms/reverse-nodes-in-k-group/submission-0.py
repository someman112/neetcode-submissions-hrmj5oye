# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        tail = dummy
        stack = []
        i = 0
        j = i+k

        while head is not None:
            stack.append(head)
            head = head.next
            i+=1

            if i == j:
                while stack:
                    tail.next = stack.pop()
                    tail = tail.next
                tail.next = head 
                j = i + k
                 
        return dummy.next


        