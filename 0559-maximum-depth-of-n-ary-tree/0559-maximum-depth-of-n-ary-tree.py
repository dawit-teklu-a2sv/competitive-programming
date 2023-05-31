"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        depthG = -float('inf')
        
        def dfs(node,count):
            nonlocal depthG
            if not node:
                depthG = 0
                return 
            if not node.children:
                depthG = max(depthG,count + 1)
                return 
            for child in node.children:
                dfs(child,count+1) 
            return 1

        dfs(root,0)
        return depthG
        