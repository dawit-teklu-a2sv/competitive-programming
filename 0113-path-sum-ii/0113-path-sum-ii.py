# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        paths = []
        def dfs(node,current,target):
            if not node:
                return 
            current.append(node.val)
            
            if not node.left and not node.right and node.val == target:
                paths.append(current)
                return 
            dfs(node.left,current.copy(),target-node.val)
            dfs(node.right,current.copy(),target-node.val)
        dfs(root,[],targetSum)
        return paths
            
                
        
      