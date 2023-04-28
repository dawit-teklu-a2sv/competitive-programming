class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        q = deque([[0,0,1]])
        visited = set((0,0))
        directions = [[0,1],[0,-1],[-1,0],[1,0],[-1,-1],[1,1],[-1,1],[1,-1]]
        while q:
            r,c,length = q.popleft()
            
            if min(r,c) < 0 or max(r,c) >= n or  grid[r][c]:
                continue
                        
            if r == n-1 and c==n-1:
                return length
            for dirR,dirC in directions:
                newR = r + dirR
                newC = c + dirC
                if (newR,newC) not in visited:
                    q.append((newR,newC,length+1))
                    visited.add((newR,newC))
        return -1
            
        
        