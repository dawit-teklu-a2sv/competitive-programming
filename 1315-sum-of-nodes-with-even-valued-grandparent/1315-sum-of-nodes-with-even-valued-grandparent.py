# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        result = 0
        
        def dfs(node):
            nonlocal result
            if not node:
                return 
            if node.val % 2 == 0:
                if node.left:
                    if node.left.left:
                        result += node.left.left.val
                    if node.left.right:
                        result += node.left.right.val
                    
                if node.right:
                    if node.right.left:
                        result += node.right.left.val
                    if node.right.right:
                        result += node.right.right.val   
            dfs(node.left)
            dfs(node.right)
                
        dfs(root)
        return result