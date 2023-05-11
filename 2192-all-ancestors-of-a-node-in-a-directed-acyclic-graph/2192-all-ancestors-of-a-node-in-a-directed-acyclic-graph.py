class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        
        for fromm,to in edges:
            graph[to].append(fromm)
            
        def dfs(node,ancestors,visited):
            for ancestor in graph[node]:
                if not visited[ancestor]:
                    visited[ancestor] = 1
                    ancestors.append(ancestor)
                    dfs(ancestor,ancestors,visited)
        output = [[] for _ in range(n)]
        for i in range(n):
            visited = [0 for _ in range(n)]
            dfs(i,output[i],visited)
            output[i].sort()
        return output