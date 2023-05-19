class UnionFind:
    def __init__(self,size):
        self.root = [i for i in range(size + 1)]
        self.size = [1] * (size + 1)
        self.minimum = [float('inf') for _ in range(size + 1)]

        
    
    def find(self,x):
        if x == self.root[x]:
            return x
        parent = self.find(self.root[x])
        self.root[x] = parent
        return self.root[x]
    
    def union(self,x,y,cost):
        xparent = self.find(x)
        yparent = self.find(y)
        xsize = self.size[xparent]
        ysize = self.size[yparent]
        minS = min(self.minimum[xparent],self.minimum[yparent],cost)
        
        if xsize >= ysize:
            self.root[yparent] = xparent 
            self.size[xparent] += xsize + ysize
            self.minimum[xparent] = minS
        else:
            self.root[xparent] = yparent 
            self.size[yparent] += xsize + ysize
            self.minimum[yparent] = minS

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        unionFind = UnionFind(n)
        
        for u,v,d in roads:
            unionFind.union(u,v,d)
        # minScore = float("inf")
        root = unionFind.find(1)
        # for u,v,d in roads:
        #     if unionFind.find(u) == unionFind.find(v) == root:
        #         minScore = min(minScore,d)
        print(unionFind.minimum[unionFind.find(1)])
        return unionFind.minimum[root]
        
        
        