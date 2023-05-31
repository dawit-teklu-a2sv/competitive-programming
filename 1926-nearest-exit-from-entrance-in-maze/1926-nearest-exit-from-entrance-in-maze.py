class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        n = len(maze)
        m = len(maze[0])
        directions = [[0,-1],[0,1],[-1,0],[1,0]]
        queue = deque()
        queue.append([entrance[0],entrance[1],0])
        maze[entrance[0]][entrance[1]] = "+"
        def isValid(row,col):
            return 0 <= row < n and 0 <= col < m and maze[row][col] == "."
        while queue:
            row,col,cost = queue.popleft()
                    
            for r,c in directions:
                nr = row + r
                nc = col + c
                if isValid(nr,nc):
                    if (nr == 0 or nc == 0 or nr == n -1 or nc == m - 1):
                        return cost + 1
                    queue.append([nr,nc,cost+1])
                    maze[nr][nc] = "+"
        return -1     


                    