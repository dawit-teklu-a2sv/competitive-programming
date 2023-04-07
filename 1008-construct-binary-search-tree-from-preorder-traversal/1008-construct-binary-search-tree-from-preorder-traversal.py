# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        i = 0
        def construct(bound):
            nonlocal i
            if i == len(preorder) or preorder[i] > bound:
                return 
            root  = TreeNode(preorder[i])
            i += 1
            root.left = construct(root.val)
            root.right = construct(bound)
            return root
        return construct(float('inf'))