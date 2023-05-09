class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        colors = [0 for _ in range(numCourses)]
        graph = [[] for _ in range(numCourses)]
        for c, p in prerequisites:
            graph[c].append(p)
            
        def dfs(node):
            if colors[node] == 1:
                return False
            
            colors[node] = 1
            
            for p in graph[node]:
                if colors[p] == 2:
                    continue
                if not dfs(p):
                    return False
            colors[node] = 2
            return True
        output = 0
        for i in range(numCourses):
            if dfs(i):
                output += 1
        return output == numCourses
        