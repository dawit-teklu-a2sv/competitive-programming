# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache
        def solve(node):
            if not node:
                return 0
            dontrob = solve(node.left) + solve(node.right)
            rob = node.val
            if node.left:
                rob += solve(node.left.left) + solve(node.left.right)
            if node.right:
                rob += solve(node.right.left) + solve(node.right.right)
            return max(dontrob,rob)
            # dontrob = solve(node.left,True) + solve(node.right,True)
            # rob = node.val + solve(node.left,False) + solve(node.right,False) if canRob else -1
            # return max(dontrob,rob)
        return solve(root)
                

