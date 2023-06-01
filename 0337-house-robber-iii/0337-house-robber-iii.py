# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache
        def solve(node,canRob=True):
            if not node:
                return 0
            
            rob = node.val + solve(node.left,False) + solve(node.right,False) if canRob else -1
            dontrob = solve(node.left,True) + solve(node.right,True)
            
            return max(rob,dontrob)
        return solve(root)
        