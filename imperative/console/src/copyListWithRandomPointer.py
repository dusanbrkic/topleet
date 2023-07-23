"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        currNode = head
        m = {None : None}
        while currNode:
            m[currNode] = Node(currNode.val)
            currNode = currNode.next
        currNode = head
        while currNode:
            m[currNode].next = m[currNode.next]
            m[currNode].random = m[currNode.random]
            currNode = currNode.next
        
        return m[head]