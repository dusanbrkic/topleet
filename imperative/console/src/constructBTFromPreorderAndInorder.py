# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        stack = []
        i = 0
        j = 0
        newTree = TreeNode()
        node = newTree
        while i < len(preorder):
            node.val = preorder[i]
            
            if preorder[i] != inorder[j]:
                stack.append(node)
                if i < len(preorder) - 1:
                    node.left = TreeNode()
                    node = node.left
            else:
                j += 1
                while len(stack) > 0 and stack[-1].val == inorder[j]:
                    node = stack.pop()
                    j += 1
                if i < len(preorder) - 1:
                    node.right = TreeNode()
                    node = node.right
            i += 1
        return newTree
                