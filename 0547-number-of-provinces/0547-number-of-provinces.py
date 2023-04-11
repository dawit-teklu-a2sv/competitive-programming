class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        def dfs(i):
            for j in range(n):
                if sum (visited) == n:
                    return 
                if isConnected[i][j] == 1 and not visited[j]:
                    visited[j] = 1
                    dfs(j)
        n = len(isConnected)
        visited = [0] * n
        count  = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                count += 1
        return count
            