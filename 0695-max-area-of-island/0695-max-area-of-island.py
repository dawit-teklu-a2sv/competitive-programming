class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        deltaRow = [-1,1,0,0]
        deltaCol = [0,0,-1,1]
        
        rows,cols = len(grid),len(grid[0])
        visited = set()
        
        
        def dfs(r,c):
            if r < 0 or r == rows or c < 0 or c == cols or not grid[r][c] or (r,c) in visited:
                return 0
            
            visited.add((r,c))
            
            temp_sum = 1
            
            for i in range(4):
                temp_sum += dfs(r+deltaRow[i],c+deltaCol[i])
            return temp_sum
        
        ans = 0
        for row in range(rows):
            for col in range(cols):
                ans = max(ans,dfs(row,col))
        return ans
        