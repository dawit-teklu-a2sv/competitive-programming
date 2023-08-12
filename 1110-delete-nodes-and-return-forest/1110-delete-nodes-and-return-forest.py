# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root, to_delete):
        to_delete = set(to_delete)
        res = []
        
        def helper(root,parent_deleted):
            if root == None:
                return 
            if parent_deleted and not root.val in to_delete:
                res.append(root)
            root.left = helper(root.left,root.val in to_delete)
            root.right = helper(root.right,root.val in to_delete)
            
            return None if root.val in to_delete else root
        helper(root,True)
        return res

        