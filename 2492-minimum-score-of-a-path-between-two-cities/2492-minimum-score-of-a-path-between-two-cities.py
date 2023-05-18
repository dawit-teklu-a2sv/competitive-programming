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
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        unionFind = UnionFind(n)
        for u,v,d in roads:
            unionFind.union(u,v)
        minScore = float("inf")
        root = unionFind.find(1)
        for u,v,d in roads:
            if unionFind.find(u) == unionFind.find(v) == root:
                minScore = min(minScore,d)
        return minScore
        
        
        