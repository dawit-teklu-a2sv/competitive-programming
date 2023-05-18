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
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
#         graph = defaultdict(set)
        
#         def dfs(source,target):
#             if source not in visited:
#                 visited.add(source)
#                 if source == target:
#                     return True

                
#                 for n in graph[source]:
#                     if dfs(n,target):
#                         return True

        unionFind = UnionFind(len(edges))
        for u,v in edges:
            visited = set()
            if unionFind.find(u) == unionFind.find(v):
                return [u,v]
            unionFind.union(u,v)
                
            
                