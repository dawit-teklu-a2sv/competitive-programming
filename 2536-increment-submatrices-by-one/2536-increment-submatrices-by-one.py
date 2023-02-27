class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        prefSum = [[0] * (n+2) for _ in range(n+2)] 
        
        for r1,c1,r2,c2 in queries:
            prefSum[r1+1][c1+1] += 1
            prefSum[r2+2][c1 + 1] -= 1
            prefSum[r1+1][c2+2] -= 1
            prefSum[r2+2][c2+2] += 1
            
        for i in range(1,n+1):
            for j in range(1,n+1):
                prefSum[i][j] += prefSum[i][j-1] + prefSum[i-1][j] - prefSum[i-1][j-1]
        
        return [row[1:-1] for row in prefSum[1:-1]]