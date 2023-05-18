class UnionFind:
    def __init__(self,size):
        self.root = [i for i in range(size)]
        self.size = [0] * size
    
    
    def find(self,x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
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
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        findUnion = UnionFind(n)
        for u,v in edges:
            findUnion.union(u,v)
        return findUnion.find(source) == findUnion.find(destination)
        
#         visited = [False for _ in range(n)]
        
#         graph = defaultdict(list)
        
#         for u,v in edges:
#             graph[u].append(v)
#             graph[v].append(u)
            
#         queue = deque([source])
        
#         while queue:
#             curr = queue.popleft()
#             if curr == destination:
#                 return True
            
#             if curr in graph and not visited[curr]:
#                 queue.extend(graph[curr])
#             visited[curr] = True
#         return False
