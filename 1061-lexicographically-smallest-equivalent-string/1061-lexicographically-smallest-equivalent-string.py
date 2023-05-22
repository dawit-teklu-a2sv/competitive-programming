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
        if xparent < yparent:
            self.root[yparent] = xparent
            # self.size[xparent] += ysize
        else:
            self.root[xparent] = yparent
            # self.size[yparent] += xsize
        # if xparent != yparent:
        #     if xsize > ysize:
        #         self.root[yparent] = xparent 
        #     elif ysize > xsize:
        #         self.root[xparent] = yparent 
        #     else:
        #         self.root[yparent] = xparent
        #         self.size[xparent] += 1
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = UnionFind(26)
        for i in range(len(s1)):
            s1Ord = ord(s1[i]) - ord('a')
            s2Ord = ord(s2[i]) - ord('a')
            uf.union(s1Ord,s2Ord)
        output = ""
        for j in range(len(baseStr)):
            parent = uf.find(ord(baseStr[j])-ord('a'))
            output += chr(parent + ord('a'))
        return output
