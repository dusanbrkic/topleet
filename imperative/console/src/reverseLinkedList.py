# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# recursive
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverseDirection(node1, node2):
            if node2 == None:
                return node1
            next = node2.next
            node2.next = node1
            return reverseDirection(node2, next)
        
        if head == None:
            return None
        next = head.next
        head.next = None
        return reverseDirection(head, next)
             
# iterative
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        node = head.next
        head.next = None
        previous = head
        while True:
            next = node.next
            node.next = previous
            previous = node
            if next == None:
                return node
            node = next
            
             