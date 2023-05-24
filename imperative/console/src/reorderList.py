# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        tail = head
        i = 1
        while tail:
            tail = tail.next
            i+=1
        mid = i // 2
        
        tail = head
        i = 1
        head2 = None
        while tail:
            if i == mid:
                head2 = tail.next
                tail.next = None
                break
            tail = tail.next
            i += 1
        
        prev = None
        current = head2
        while current:
            currNext = current.next
            current.next = prev
            prev = current
            current = currNext
            
        
        tail1 = head
        tail2 = prev
        while tail1 and tail2:
            tail1Next = tail1.next
            tail2Next = tail2.next
            
            tail1.next = tail2
            tail2.next = tail1Next
            
            tail2 = tail2Next
            tail1 = tail1Next
        
        
            
            
            
        
        
                