class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        queue = deque([])
        
        rows = len(grid)
        cols = len(grid[0])
        
        fresh_count = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh_count += 1
        time = 0
        while queue and fresh_count > 0:
            time += 1
            for _ in range(len(queue)):
                x,y = queue.popleft()
                for dx,dy  in [(1,0),(-1,0),(0,1),(0,-1)]:
                    xx = x + dx
                    yy = y + dy

                    if 0 <= xx < rows and 0 <= yy < cols and grid[xx][yy] == 1:
                        fresh_count -= 1
                        grid[xx][yy] = 2
                        queue.append((xx,yy))
        return time if fresh_count == 0 else -1
        
                    
    
        