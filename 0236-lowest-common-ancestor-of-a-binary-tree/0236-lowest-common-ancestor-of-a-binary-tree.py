# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#if the current node is null return it to the parent
#checking if the left and right subtree of the current node contains either of p and q
#checking if the value of the current nodes is equal to either p and q if so return it to the parent
# if the returned values of left and right subtree of current node is not none
# the ansewer will be the current node else the LCA is the one that returned non null value
# Time complexity O(n) the worest case exploring all nodes where n is the number of nodes
# Space complexity log(n) for the call stack
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root.val == p.val or root.val == q.val:
            return root
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if left and right:
            return root 
        
        return left or right
        

        
        
    
    
            
            
        
        