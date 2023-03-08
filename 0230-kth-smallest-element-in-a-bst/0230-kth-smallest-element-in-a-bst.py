# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        count = 0
        
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            count += 1
            temp = stack.pop()
            if count == k:
                return temp.val
            root = temp.right
        