class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [[0,-1],[0,1],[-1,0],[1,0]]
        
        perimeter = 0 
        
        m,n = len(grid),len(grid[0])
        
        for i in range(m):
            for j in range(n):
                temp =  grid[i][j]
                perimeter += 4 * temp
                for x,y in directions:
                    di = i + x
                    dj = j + y
                    if 0 <= di < m and 0 <= dj < n:
                        perimeter -= temp * grid[di][dj]
        return perimeter
        