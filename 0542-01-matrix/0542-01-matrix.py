class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        ans = [[0]* n for _ in range(m)]
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        queue = deque()
        visited = set()
        
        for r in range(m):
            for c in range(n):
                if not mat[r][c]:
                    queue.append([r,c])
                    visited.add((r,c))
                    
        dist = 0
        
        while queue:
            
            for _ in range(len(queue)):
                r,c = queue.popleft()
                
                if mat[r][c]:
                    ans[r][c] = dist
                    
                for dR,dC in directions:
                    newR = r + dR
                    newC = c + dC
                    
                    if 0<=newR<m and 0<=newC<n and (newR,newC) not in visited:
                        queue.append([newR,newC])
                        visited.add((newR,newC))
            dist += 1
        return ans
                    
                
            
