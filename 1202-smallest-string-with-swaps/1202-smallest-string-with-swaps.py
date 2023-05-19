class UnionFind:
    def __init__(self,size):
        self.root = [i for i in range(size)]
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
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        uf = UnionFind(n)
        
        for u,v in pairs:
            uf.union(u,v)
        d = defaultdict(list)
        
        for i in range(n):
            root = uf.find(i)
            d[root].append(s[i])
        for key,value in d.items():
            value.sort(reverse=True)
        output = ""
        for i in range(n):
            root = uf.root[i]
            output += d[root].pop()
        
        return output
