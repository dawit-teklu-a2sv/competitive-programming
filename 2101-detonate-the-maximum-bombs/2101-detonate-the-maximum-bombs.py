class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        n = len(bombs)
        
        for i in range(n):
            required_distance = bombs[i][2] ** 2
            for j in range(n):
                if i != j:
                    temp_distance = (bombs[i][0]-bombs[j][0]) ** 2 + (bombs[i][1]-bombs[j][1]) ** 2 
                    if required_distance >= temp_distance:
                        graph[i].append(j)
        def dfs(node,visited):
            for child in graph[node]:
                if child not in visited:
                    visited.add(child)
                    dfs(child,visited)
        ans = -float('inf')
        for i in range(n):
            visited = set([i])
            dfs(i,visited)
            ans = max(ans,len(visited))
        return ans
            