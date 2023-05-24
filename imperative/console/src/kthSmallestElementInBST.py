# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    _found = None
    _currentK = 1
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(node):
            if self._found:
                return
            
            if not node:
                return 0
            
            if node.left:
                inorder(node.left)
                
            if self._currentK == k:
                self._found = node.val
            self._currentK += 1
            
            if node.right:
                inorder(node.right)
        
        inorder(root)
        return self._found
        