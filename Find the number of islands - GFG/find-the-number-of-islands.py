#User function Template for python3
import sys
sys.setrecursionlimit(10**8)
from collections import deque
class Solution:
    def numIslands(self,grid):
        #code here
        n,m = len(grid),len(grid[0])
        visited = [[0]*m for _ in range(n)]
        def dfs(row,col):
            q = deque()
            q.append([row,col])
            visited[row][col] = 1
            while q:
                row,col = q[0]
                q.popleft()
                
                for i in range(-1,2):
                    for j in range(-1,2):
                        nRow = row +  i
                        nCol =  col + j
                        if nRow >= 0 and nRow < n and nCol >= 0 and nCol < m and grid[nRow][nCol] == 1 and not visited[nRow][nCol]:
                            visited[nRow][nCol] = 1
                            q.append([nRow,nCol])
        count = 0
        for i in range(n):
            for j in range(m):
                # print(type(grid[i][j]),visited[i][j])
                if grid[i][j] == 1 and not visited[i][j]:
                    count += 1
                    dfs(i,j)
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj=Solution()
        print(obj.numIslands(grid))
# } Driver Code Ends