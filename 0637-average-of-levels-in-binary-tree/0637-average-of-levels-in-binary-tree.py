# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque()
        
        queue.append(root)
        ans = []
        while queue:
            length = len(queue)
            total = 0
            for _ in range(length):
                temp = queue.popleft()
                total += temp.val
                
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
            ans.append(total/length)
        return ans
#         graph = defaultdict(list)
        
#         def levelOrder(node,level):
#             if not node:
#                 return 
#             graph[level].append(node.val)
#             levelOrder(node.left,level+1)
#             levelOrder(node.right,level+1)
#         levelOrder(root,0)
#         output = []
#         for key,value in graph.items():
#             output.append(sum(value)/len(value))
#         return output
        
    