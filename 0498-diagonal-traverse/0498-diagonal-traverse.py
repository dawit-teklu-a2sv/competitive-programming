class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        output = [0] * (m * n)
        row,col = 0,0
        i = 0
        up = True # for tracking up and down movments
        
        while (row < m and col < n):
            if up:
                while row > 0 and col < n-1:
                    output[i] = mat[row][col]
                    col += 1
                    row -= 1
                    i += 1
                output[i] = mat[row][col]
                i += 1
                if col == n-1:
                    row += 1
                else:
                    col += 1
                    
            else:
                while col > 0 and row < m-1:
                    output[i] = mat[row][col]
                    row += 1
                    col -= 1
                    i += 1
                output[i] = mat[row][col]
                i += 1
                if row == m-1:
                    col += 1
                else:
                    row += 1
            up = not up
        return output
                
                
                