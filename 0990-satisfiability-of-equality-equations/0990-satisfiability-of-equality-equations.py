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
        if ysize <= xsize:
            self.root[yparent] = xparent
            self.size[xparent] += ysize
            # self.size[xparent] += ysize
        else:
            self.root[xparent] = yparent
            self.size[yparent] += xsize
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind(26)
        for equation in equations:
            num1,symbol1,symbol2,num2= equation
            symbol = symbol1 + symbol2
            if symbol == "==":
                uf.union(ord(num1)-ord('a'),ord(num2)-ord('a'))
        for equation in equations:
            num1,symbol1,symbol2,num2= equation
            symbol = symbol1 + symbol2
            if symbol == "!=":
                parent1 = uf.find(ord(num1)-ord('a'))
                parent2 = uf.find(ord(num2)-ord('a'))
                if parent1 == parent2:
                    return False
        return True
        