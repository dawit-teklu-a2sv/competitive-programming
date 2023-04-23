# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        result = -float('inf')
        
        def postOrder(root):
            nonlocal result
            if not root:
                return 0
            
            left = postOrder(root.left)
            right = postOrder(root.right)
            
            straightSum = max(max(left,right) + root.val, root.val)
            caseVal = max(straightSum , left + right + root.val)
            result = max(result,caseVal)
            return straightSum
        postOrder(root)
        return result;
        
        