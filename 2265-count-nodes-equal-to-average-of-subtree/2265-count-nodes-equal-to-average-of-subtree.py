# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = 0
    def averageOfSubtreeHelper(self,root):
        if not root:
            return [0,0]
        left = self.averageOfSubtreeHelper(root.left)
        right = self.averageOfSubtreeHelper(root.right)
        currSum = left[0] + right[0] + root.val
        currCount = left[1] + right[1] + 1
        
        if (currSum // currCount == root.val):
            self.result += 1
        return [currSum,currCount]
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.averageOfSubtreeHelper(root)
        return self.result
        