# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #Inorder traversal
        stack = []
        curr = root
        output = []
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            temp = stack.pop()
            if output and temp.val <= output[-1]:
                return False
            output.append(temp.val)
            curr = temp.right
        return True
            