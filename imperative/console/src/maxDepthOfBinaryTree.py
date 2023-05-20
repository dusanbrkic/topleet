# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def getDepth(root, d):
            if not root:
                return d
            
            resultRight = d + 1
            resultLeft = d + 1
            if root.right:
                resultRight = getDepth(root.right, d + 1)
            if root.left:
                resultLeft = getDepth(root.left, d + 1)
            
            return max(resultRight, resultLeft)
        
        return getDepth(root, 0)
                