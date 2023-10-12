class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        if n <= 1:
            return 1
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        queue = deque()
        count = 0
        for vertex,nodes in graph.items():
            if len(nodes) == 1:
                queue.append(vertex)
                
        while queue:
            
            for _ in range(len(queue)):
                
                u = queue.popleft()
                
                p = graph[u][0] if u in graph and graph[u] else -1
                
                if p >= 0:
                    graph[p].remove(u)
                    
                if values[u] % k == 0:
                    count += 1
                else:
                    values[p] += values[u]
                
                if p >= 0 and len(graph[p]) == 1:
                    queue.append(p)
        return count
                    
                
            