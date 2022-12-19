class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        max_sum = 0
        rows = len(grid)
        cols = len(grid[0])
        
        for i in range(1,rows-1):
            for j in range(1,cols-1):
                max_sum = max(max_sum,(sum(grid[i-1][j-1:j+2]) + grid[i][j] + sum(grid[i+1][j-1:j+2])))
                
        return max_sum
        
        