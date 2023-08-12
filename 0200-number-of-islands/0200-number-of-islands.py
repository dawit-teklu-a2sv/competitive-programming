class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        visited = [[False] * n for _ in range(m)]
        def dfs(i,j):
            if 0 <= i < m and 0 <= j < n and not visited[i][j] and grid[i][j] == '1':
                visited[i][j] = True
                for k,l in directions:
                    dfs(i+k,j+l)
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    dfs(i,j)
                    count += 1
        return count