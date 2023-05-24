# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(root, validRange):
            if not root:
                return True
            if not (root.val > validRange[0] and root.val < validRange[1]):
                return False
            
            return isValid(root.right, (root.val, validRange[1])) and isValid(root.left, (validRange[0], root.val))
        
        return isValid(root, (-float('inf'), float('inf')))