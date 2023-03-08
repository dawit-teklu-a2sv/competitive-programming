# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideViewHelper(self,currNode,result,depth):
        if currNode == None:
            return 
        if len(result) == depth:
            result.append(currNode.val)
        self.rightSideViewHelper(currNode.right,result,depth + 1)   
        self.rightSideViewHelper(currNode.left,result,depth + 1)   

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
         result = []
         self.rightSideViewHelper(root,result,0)
         return result