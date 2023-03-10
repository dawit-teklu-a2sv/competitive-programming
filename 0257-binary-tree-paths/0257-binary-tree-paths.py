# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        answer = []
        
        def backtrack(root,path):
            if not root.left and not root.right:
                answer.append(f"{path}{root.val}")
                
            if root.left:
                backtrack(root.left,f"{path}{root.val}->")
            if root.right:
                backtrack(root.right,f"{path}{root.val}->")
                              
        backtrack(root,"")                    
        
        # def backtrack(root,array):
        #     if not root:
        #         answer.append("->".join(str(x) for x in array)) 
        #         return 
        #     array.append(root.val)
        #     if root.left and root.right:
        #         backtrack(root.left,array)
        #         backtrack(root.right,array)
        #     elif root.left:
        #         backtrack(root.left,array)
        #     else:
        #         backtrack(root.right,array)
        #     array.pop()
        # backtrack(root,[])
        return answer
        