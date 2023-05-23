class UnionFind:
    def __init__(self,size):
        self.root = [i for i in range(size )]
        self.size = [1] * (size)

    
    def find(self,x):
        if x == self.root[x]:
            return x
        parent = self.find(self.root[x])
        self.root[x] = parent
        return self.root[x]
    
    def union(self,x,y):
        xparent = self.find(x)
        yparent = self.find(y)
        xsize = self.size[xparent]
        ysize = self.size[yparent]
        
        if xparent != yparent:
            if xsize >= ysize:
                self.root[yparent] = xparent 
                self.size[xparent] += xsize + ysize
            else:
                self.root[xparent] = yparent 
                self.size[yparent] += xsize + ysize
            return True
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        def distance(point1,point2):
            return abs(point1[0]-point2[0]) + abs(point1[1]-point2[1])
        edges = []
        n = len(points)
        for i in range(n):
            for j in range(i+1,n):
                edges.append([distance(points[i],points[j]),i,j])
        edges.sort()
        uf = UnionFind(n*2)
        result = 0
        for cost,x,y in edges:
            if uf.union(x,y):
                result += cost
        return result
        