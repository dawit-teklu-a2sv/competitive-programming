# class UnionFind:
    
#     def __init__(self,n):
    
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        up = {x: set([2,3,4]) for x in [2,5,6]}
        down = {x: set([2,5,6]) for x in [2,3,4]}
        left = {x:set([1,4,6])  for x in [1,3,5]}
        right = {x: set([1,3,5]) for x in [1,4,6]}
        
        grid[0][0] = -grid[0][0]
        
        queue = deque([[0,0]])
        n = len(grid)
        m = len(grid[0])
        while queue:
            i,j = queue.popleft()
            if i == n-1 and j == m - 1:return True
            
            for k,l,d in [(i-1,j,up),(i+1,j,down),(i,j-1,left),(i,j+1,right)]:
                if 0 <=k < n and 0 <=l < m and -grid[i][j] in d and grid[k][l] in d[-grid[i][j]]:
                    grid[k][l] = -grid[k][l]
                    queue.append([k,l])
        return False
        