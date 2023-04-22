class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not len(board) or not len(board[0]):
            return 
        rows,cols = len(board),len(board[0])
        
        #capture the unsurrouned regions
        def dfs(r,c):
            if r < 0 or c < 0 or r == rows or c == cols or board[r][c] != "O":
                return 
            board[r][c] = "T"
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c-1)
            dfs(r,c+1)
            # for row in range(-1,2):
            #     for col in range(-1,2):
            #         if row != col
            #             nR = r+row
            #             nC = c+col
            #             dfs(nr,nC)
        for i in range(rows):
            for j  in range(cols):
                if (board[i][j] == 'O' and 
                (i in [0,rows-1] or j in [0,cols-1])):
                    dfs(i,j)
        #capture the surrouneded regions
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
        #unCapture the unsurrouned regions
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "T":
                    board[row][col] = 'O'