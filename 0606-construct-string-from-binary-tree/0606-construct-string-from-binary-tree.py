# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        result = ""
        #preorder
        def preorder(node):
            nonlocal result
            if not node:
                return 
            result += str(node.val)
            if not node.left and not node.right:
                return 
            result += "("
            preorder(node.left)
            result += ")"
            if node.right:
                result += "("
                preorder(node.right)
                result += ")"
        preorder(root)
        return result
        