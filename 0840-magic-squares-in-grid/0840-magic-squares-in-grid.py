class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        
        
        def check(a,b,c,d,e,f,g,h,i):
            return (sorted([a,b,c,d,e,f,g,h,i]) == list(range(1,10)) and(a + b + c == d + e + f == g + h + i == a + d + g == b + e + h == c + f + i == a + e + i == c + e + g == 15))
        
        R = len(grid)
        C = len(grid[0])
        ans = 0
        for i in range(R-2):
            for j in range(C-2):
                if grid[i+1][j+1] != 5:
                    continue
                if check(grid[i][j],grid[i][j+1],grid[i][j+2],grid[i+1][j],grid[i+1][j+1],grid[i+1][j+2],grid[i+2][j],grid[i+2][j+1],grid[i+2][j+2]):
                    ans += 1
        return ans
                
        