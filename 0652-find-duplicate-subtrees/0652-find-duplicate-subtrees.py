# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Creating serialization for each nodes and checking if there is pre computed
# value for the current serializtion
# Time complexity O(n**2)
# Space complexity O(n)
#Inorder traversal
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        container = defaultdict(list)
        def dfs(root):
            if not root:
                return "null"
            
            temp =",".join([str(root.val),dfs(root.left),dfs(root.right)])
            
            if len(container[temp]) == 1:
                res.append(root)
                
            container[temp].append(root)
            
            return temp 
        
        res = []
        dfs(root)
        return res
        
        
        