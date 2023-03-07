# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.dfs(root,[])
    def dfs(self,root,output):
        if root == None:
            return output
        output = self.dfs(root.left,output)
        output = self.dfs(root.right,output)
        output.append(root.val)
        return output
        