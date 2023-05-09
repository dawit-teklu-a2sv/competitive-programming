class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        n = len(graph)
        
        colors = [0 for _ in range(n)]
        
        def dfs(node):
            if colors[node] == 1:
                return False
            
            colors[node] = 1
            
            for neighbor in graph[node]:
                if colors[neighbor] == 2:
                    continue
                if not dfs(neighbor):
                    return False
            colors[node] = 2
            return True
        output = []
        for i in range(n):
            if dfs(i):
                output.append(i)
        return output
        
        
                