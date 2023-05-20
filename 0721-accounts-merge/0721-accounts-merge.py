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
        uf = UnionFind(n)
        d = {}
        for i in range(n):
            for j in range(1,len(accounts[i])):
                email = accounts[i][j]
                name = accounts[i][0]
                if email not in d:
                    d[email] = i 
                else:
                    uf.union(i,d[email])
        components = defaultdict(list)
        for key in d:
            group = d[key]
            rep = uf.find(group)
            components[rep].append(key)
            
        mergedAccounts = []
        for key in components:
            component = components[key]
            component.sort()
            component.insert(0,accounts[key][0])
            mergedAccounts.append(component)
        return mergedAccounts
        
        