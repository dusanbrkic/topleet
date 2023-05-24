from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        d = deque()
        d.append(root)
        
        result = []
        while len(d) > 0:
           result.append([])
           for _ in range(len(d)):
                node = d.popleft()
                result[-1].append(node.val)
                if node.left:
                   d.append(node.left)
                if node.right:
                   d.append(node.right)
        return result