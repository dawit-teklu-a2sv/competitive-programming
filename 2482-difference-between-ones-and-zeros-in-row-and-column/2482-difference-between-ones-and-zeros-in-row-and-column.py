class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        output = [[0] * m for _ in range(n)]
        rows = {}
        cols = {}
        for i in range(n):#calculating row values
            row_value = 0
            for j in range(m):
                row_value += (1 if grid[i][j] == 1 else -1)
            rows[i] = row_value
        for j in range(m):
            col_value = 0
            for i in range(n):
                col_value += (1 if grid[i][j] == 1 else -1)
            cols[j] = col_value 
        for i in range(n):
            for j in range(m):
                output[i][j] = rows[i] + cols[j]
            
        return output
            
            
            
