class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [[float('inf')] * n for _ in range(n)]
        for i, j, w in times:
            dist[i-1][j-1] = w

        for i in range(n):
            dist[i][i] = 0
        for l in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][l] + dist[l][j])
        result = max(dist[k-1])
        
        return result if result != float('inf') else -1
        