# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        nums = defaultdict(int)
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            temp = stack.pop()
            nums[temp.val] += 1
            root = temp.right
            
        max_node = max(nums.values())
        return [key for key,value in nums.items() if value == max_node]
           
        