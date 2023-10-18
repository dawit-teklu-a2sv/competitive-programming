class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        
        graph = [[] for _ in range(n+1)]
        
        
        for u,v in relations:
            graph[u].append(v)
            
        dp = [0] * (n + 1)
        def dfs(u):
            if dp[u]:
                return dp[u]
            
            dp[u] = max((dfs(v) for v in graph[u]),default=0) + time[u-1]
            
            return dp[u]
            
        for i in range(n+1):
            dfs(i)
            
        return max(dp)