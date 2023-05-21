# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(root1, root2):
            if root1 == root2 == None:
                return True
            if not root1 or not root2:
                return False
            return root1.val == root2.val and sameTree(root1.right, root2.right) and sameTree(root1.left, root2.left)
        
        stack = [root]
        while stack:
            head = stack.pop()
            if sameTree(head, subRoot):
                return True
            if head.left:
                stack.append(head.left)
            if head.right:
                stack.append(head.right)
        
        return False