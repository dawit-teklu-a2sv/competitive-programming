# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        d = {}
        for i,item in enumerate(inorder):
            d[item] = i
        return self.buildT(preorder,0,len(preorder)-1,inorder,0,len(inorder)-1,d)
    def buildT(self,preorder,pStart,pEnd,inorder,inStart,iEnd,d):
        if pStart > pEnd or inStart > iEnd:
            return 
        root = TreeNode(preorder[pStart])
        inRoot = d[root.val]
        numsLeft = inRoot - inStart
        root.left = self.buildT(preorder,pStart + 1, pStart + numsLeft,inorder,inStart,inRoot-1,d)
        root.right = self.buildT(preorder,pStart + numsLeft + 1,pEnd,inorder,inRoot + 1,iEnd, d)
        return root