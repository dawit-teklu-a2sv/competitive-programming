class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        visited = [False for _ in range(n)]
        
        graph = defaultdict(list)
        
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        queue = deque([source])
        
        while queue:
            curr = queue.popleft()
            if curr == destination:
                return True
            
            if curr in graph and not visited[curr]:
                queue.extend(graph[curr])
            visited[curr] = True
        return False