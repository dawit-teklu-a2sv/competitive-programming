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


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        d = {}
        uf = UnionFind(n)
        for i in range(n):
            for j in range(1,len(accounts[i])):
                email = accounts[i][j]
                if email in d:
                    uf.union(i,d[email])
                else:
                    d[email] = i 
        components = defaultdict(list)
        for key,group in d.items():
            parent = uf.find(group)
            components[parent].append(key)
        output = []
        
        for key,value in components.items():
            name = accounts[key][0]
            value.sort()
            value.insert(0,name)
            output.append(value)
        return output


        