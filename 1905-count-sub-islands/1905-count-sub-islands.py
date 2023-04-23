class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        deltaRow = [1,-1,0,0]
        deltaCol = [0,0,1,-1]
        n = len(grid2)
        m = len(grid2[0])
        ans = 0
        
        def dfs(i,j):
            nonlocal flag
            if not grid1[i][j]:
                flag = False
                return 
            grid2[i][j] = 0
            for k in range(4):
                nRow = i + deltaRow[k]
                nCol = j + deltaCol[k]
                
                if nRow >= 0 and nRow < n and nCol >= 0 and nCol < m and grid2[nRow][nCol] == 1:
                    dfs(nRow,nCol)
        for i in range(n):
            flag = True
            for j in range(m):
                if grid2[i][j] == 1:
                    dfs(i,j)
                    if flag:
                        ans += 1
                    flag = True 
        return ans
        
                        
            
            