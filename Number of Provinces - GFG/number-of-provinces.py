#User function Template for python3

class Solution:
    def numProvinces(self, adj, V):
        # code here 
        adjL = [[] for _ in range(V)]
        for i in range(V):
            for j in range(V):
                if adj[i][j] and i != j:
                    adjL[i].append(j)
                    adjL[j].append(i)
        vis = [0] * V
        def dfs(node):
            vis[node] = 1
            for item in adjL[node]:
                if not vis[item]:
                    dfs(item)
        count = 0
        for i in range(V):
            if not vis[i]:
                count += 1
                dfs(i)
        return count
                    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        V=int(input())
        adj=[]
        
        for i in range(V):
            temp = list(map(int,input().split()))
            adj.append(temp);
        
        ob = Solution()
        print(ob.numProvinces(adj,V))
# } Driver Code Ends