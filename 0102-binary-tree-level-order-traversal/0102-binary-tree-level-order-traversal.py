# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = []
    def levelOrderHelper(self,root,depth):
        if not root:
            return
        if len(self.result) == depth:
            self.result.append([])
        self.result[depth].append(root.val)
        self.levelOrderHelper(root.left,depth + 1)        
        self.levelOrderHelper(root.right,depth + 1)

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
         self.levelOrderHelper(root,0)
         return self.result
                    
          