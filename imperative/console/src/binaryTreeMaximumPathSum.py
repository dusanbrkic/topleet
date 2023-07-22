# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        
        def dfs(node):
            if not node:
                return 0
            maxLeftChildNode = dfs(node.left)
            maxRightChildNode = dfs(node.right)
            
            maxLeftChildNode = max(maxLeftChildNode, 0)
            maxRightChildNode = max(maxRightChildNode, 0)
            
            res[0] = max(res[0], node.val + maxLeftChildNode + maxRightChildNode)
            
            return node.val + max(maxLeftChildNode, maxRightChildNode)
            
        dfs(root)
        return res[0]