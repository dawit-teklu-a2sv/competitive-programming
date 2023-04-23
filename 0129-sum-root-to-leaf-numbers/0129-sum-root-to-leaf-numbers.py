# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def dfs(curr,summ):
            if not curr:
                return 0
            summ = summ * 10 + curr.val
            if not curr.left and not curr.right:
                return summ
            return dfs(curr.left,summ) + dfs(curr.right,summ)
        
        return dfs(root,0)
       \
    
          
        