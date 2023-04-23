class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        
        for u,v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
        print(graph)
        color = {}
        
        def dfs(i,c):
            color[i] = c            
            for e in graph[i]:
                
                if e in color:
                    if color[e] == c:
                        return False
                else:
                    if not dfs(e,1-c):
                        return False
            return True
        
        for i in range(1,n+1):
            if i not in color:
                if not dfs(i,1):
                    return False
        return True
                
                
                
        