class UnionFind:
    def __init__(self,size):
        self.root = [i for i in range(size + 1)]
        self.size = [1] * (size + 1)
    
    
    def find(self,x):
        if x == self.root[x]:
            return x
        parent = self.find(self.root[x])
        self.root[x] = parent
        return self.root[x]
    
    def union(self,x,y):
        xparent = self.find(x)
        yparent = self.find(y)
        xsize = self.size[x]
        ysize = self.size[y]
        if xparent != yparent:
            if xsize > ysize:
                self.root[yparent] = xparent 
            elif ysize > xsize:
                self.root[xparent] = yparent 
            else:
                self.root[yparent] = xparent
                self.size[xparent] += 1
    
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        right = {1: {1, 3, 5}, 2: {}, 3: {}, 4: {1, 3, 5}, 5: {}, 6: {1, 3, 5}}
        down = {1: {}, 2: {2, 5, 6}, 3: {2, 5, 6}, 4: {2, 5, 6}, 5: {}, 6: {}}
        uf = UnionFind(m * n)
        for x in range(m):
            for y in range(n):
                if y + 1 <= n - 1 and grid[x][y + 1] in right[grid[x][y]]:
                    uf.union(x * n + y, x * n + y + 1)
                if x + 1 <= m - 1 and grid[x + 1][y] in down[grid[x][y]]:
                    uf.union(x * n + y, (x + 1) * n + y)
        return uf.find(0) == uf.find(m * n - 1)
#         up = {x: set([2,3,4]) for x in [2,5,6]}
#         down = {x: set([2,5,6]) for x in [2,3,4]}
#         left = {x:set([1,4,6])  for x in [1,3,5]}
#         right = {x: set([1,3,5]) for x in [1,4,6]}
        
#         grid[0][0] = -grid[0][0]
        
#         queue = deque([[0,0]])
#         n = len(grid)
#         m = len(grid[0])
#         while queue:
#             i,j = queue.popleft()
#             if i == n-1 and j == m - 1:return True
            
#             for k,l,d in [(i-1,j,up),(i+1,j,down),(i,j-1,left),(i,j+1,right)]:
#                 if 0 <=k < n and 0 <=l < m and -grid[i][j] in d and grid[k][l] in d[-grid[i][j]]:
#                     grid[k][l] = -grid[k][l]
#                     queue.append([k,l])
#         return False
        