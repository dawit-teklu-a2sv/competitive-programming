class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[n-1][n-1]:
            return -1

        q = deque([[0,0,1]])
        visited = set((0,0))
        directions = [[0,1],[0,-1],[-1,0],[1,0],[-1,-1],[1,1],[-1,1],[1,-1]]
        while q:
            r,c,length = q.popleft()
            
            if r == n-1 and c==n-1:
                return length
            for dirR,dirC in directions:
                newR = r + dirR
                newC = c + dirC
                if (min(newR,newC) >= 0 and 
                    max(newR,newC) < n and 
                    not grid[newR][newC] and 
                    (newR,newC) not in visited):
                    q.append((newR,newC,length+1))
                    visited.add((newR,newC))
        return -1
            
        
        