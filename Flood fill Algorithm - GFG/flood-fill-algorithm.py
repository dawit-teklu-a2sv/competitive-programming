class Solution:
	def floodFill(self, image, sr, sc, newColor):
		#Code here
	    iniColor = image[sr][sc]
	    ans = image
	    deltaRow = [-1,0,1,0]
	    deltaCol = [0,1,0,-1]
	    n = len(image)
	    m = len(image[0])
	    def dfs(row,col):
	        ans[row][col] = newColor
	        for i in range(4):
	            nRow = row + deltaRow[i]
	            nCol = col + deltaCol[i]
	            
	            if nRow >= 0 and nRow < n and nCol >= 0 and nCol < m and image[nRow][nCol] == iniColor and ans[nRow][nCol] != newColor:
	                dfs(nRow,nCol)
	    dfs(sr,sc)
	    return ans
	            
	        
	   

#{ 
 # Driver Code Starts
import sys
sys.setrecursionlimit(10**7)
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n)
		m = int(m)
		image = []
		for _ in range(n):
			image.append(list(map(int, input().split())))
		sr, sc, newColor = input().split()
		sr = int(sr); sc = int(sc); newColor = int(newColor);
		obj = Solution()
		ans = obj.floodFill(image, sr, sc, newColor)
		for _ in ans:
			for __ in _:
				print(__, end = " ")
			print()
# } Driver Code Ends