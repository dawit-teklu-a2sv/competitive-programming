class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #BFS Implementation
        graph = [[] for _ in range(numCourses)]
        incoming = [0 for _ in range(numCourses)]
        
        for c,p in prerequisites:
            graph[p].append(c)
            incoming[c] += 1
        queue = deque()
        order = []
        for i,indegree in enumerate(incoming):
            if not indegree:
                queue.append(i)
        print(queue)       
        while queue:
            f = queue.popleft()
            order.append(f)
            
            for n in graph[f]:
                incoming[n] -= 1
                if not incoming[n]:
                    queue.append(n)
                    
        return len(order) == numCourses
        
        # dfs implementaion
#         colors = [0 for _ in range(numCourses)]
#         graph = [[] for _ in range(numCourses)]
#         for p, c in prerequisites:
#             graph[c].append(p)
            
#         def dfs(node):
#             if colors[node] == 1:
#                 return False
            
#             colors[node] = 1
            
#             for p in graph[node]:
#                 if colors[p] == 2:
#                     continue
#                 if not dfs(p):
#                     return False
#             colors[node] = 2
#             return True
        
#         for i in range(numCourses):
#             if not dfs(i):
#                 return False
#         return True
        