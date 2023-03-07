# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def insert(node,val):
            if not node:
                return TreeNode(val)
            elif node.val > val:
                 node.left = insert(node.left,val)
            else:
                 node.right = insert(node.right,val)
            return node
        return insert(root,val)
        cur = root
        if not cur:
            return TreeNode(val)
        
        while cur:
            if cur.val > val:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = TreeNode(val)
                    break
            else:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = TreeNode(val)
                    break
        return root
         
            
            
            
            
        
        
        