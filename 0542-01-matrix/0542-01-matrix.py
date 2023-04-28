class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        queue = deque()
        visited = set()
        result = [[0] * m for _ in  range(n)]
        
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    queue.append([i,j])
                    
        distance = 0
        
        while queue:
            for _ in range(len(queue)):
                r,c = queue.popleft()
                if mat[r][c]:
                    result[r][c] = distance
                    
                for dr,dc in directions:
                    nr = r + dr
                    nc = c + dc
                    
                    if 0 <= nr < n and 0 <= nc < m and (nr,nc) not in visited:
                        visited.add((nr,nc))
                        queue.append([nr,nc])
            distance += 1
        return result
    
