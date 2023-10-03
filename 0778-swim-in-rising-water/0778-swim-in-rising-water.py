class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        queue = [(grid[0][0],0,0)]
        visited = set([grid[0][0]])
        n = len(grid)
        m = len(grid[0])
        nodes = []
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        def isInBound(row,col):
            return 0 <= row < n and 0 <= col < m
        while queue:
            val,row,col = heappop(queue)
            nodes.append(val)
            if row == n - 1 and col == m-1:
                return max(nodes)
            
            for dx,dy in directions:
                r,c = row + dx, col + dy
                
                if isInBound(r,c) and grid[r][c] not in visited:
                    heappush(queue,(grid[r][c],r,c))
                    visited.add(grid[r][c])
        return max(nodes)
        
        