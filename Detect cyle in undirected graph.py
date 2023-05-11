from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		colors = [0 for _ in range(V)]
        
        def dfs(i,parent):
            if colors[i] == 1:
                return False
            colors[i] = 1
            for item in adj[i]:
                if colors[item] == 2:
                    continue
                if item != parent and not dfs(item,i):
                    return False
            colors[i] = 2
            return True
        for i in range(V):
            visited = [False for _ in range(V)]
            if  colors[i]:
                continue 
            if not dfs(i,-1):
                return 1
        return 0


#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends
