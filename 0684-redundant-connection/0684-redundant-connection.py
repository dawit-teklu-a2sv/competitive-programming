class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        
        def dfs(source,target):
            if source not in visited:
                visited.add(source)
                if source == target:
                    return True
                
                # res =  [dfs(n,target) for n in graph[source]]
                # return any(res)
                for n in graph[source]:
                    if dfs(n,target):
                        return True
                # for nei in graph[source]:
                #     print(f"nei: {nei} source {source}")
                #     return dfs(nei,target)
        
        for u,v in edges:
            visited = set()
            if u in graph and v in graph and dfs(u,v):
                return [u,v]
            graph[u].add(v)
            graph[v].add(u)
                
            
                