# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tail = head
        while n > 0:
            tail = tail.next
            n -= 1
        
        if not tail:
            return head.next
        
        finder = ListNode(0, head)
        
        while tail:
            tail = tail.next
            finder = finder.next
        
        finder.next = finder.next.next
        
        return head