# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge2Lists(list1, list2):
            mergedList = ListNode()
            mergedListTail = mergedList
            tail1 = list1
            tail2 = list2
            while tail1 and tail2:
                if tail1.val > tail2.val:
                    mergedListTail.next = tail2
                    tail2 = tail2.next
                else:
                    mergedListTail.next = tail1
                    tail1 = tail1.next
                mergedListTail = mergedListTail.next
            if tail1:
                mergedListTail.next = tail1
            if tail2:
                mergedListTail.next = tail2
            
            return mergedList.next
                
        
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i + 1] if i + 1 < len(lists) else None
                
                mergedLists.append(merge2Lists(list1, list2))
            
            lists = mergedLists
        
        return lists[0] if len(lists) > 0 else None
                