class Solution:
    def matrixBlockSum(self, matrix: List[List[int]], k: int) -> List[List[int]]:
            for r in range(len(matrix)):
                matrix[r].insert(0,0)

            zeros = [0] * len(matrix[0])
            matrix.insert(0,zeros)

            for r in range(1,len(matrix)):
                for c in range(1,len(matrix[0])):
                    matrix[r][c] += (matrix[r][c-1] + matrix[r-1][c] - matrix[r-1][c-1])
            result =  []
            rows = len(matrix) - 1
            cols = len(matrix[0]) - 1
            for r in range(rows):
                for c in range(cols):
                    row1 = max(0,r-k)
                    col1 = max(0,c-k)
                    row2 = min(r+k,rows-1)
                    col2 = min(c+k,cols-1)
                    bottom_right = matrix[row2+1][col2+1]
                    bottom_left = matrix[row2+1][col1]
                    top_right = matrix[row1][col2+1]
                    top_left = matrix[row1][col1]
                    
                    curr_sum = bottom_right - bottom_left - top_right + top_left
                    
                    if c == 0:
                        result.append([])
                    
                    result[r].append(curr_sum)
            return result
           
                