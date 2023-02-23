class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        for r in range(len(matrix)):
            self.matrix[r].insert(0,0)
            
        zeros = [0] * len(self.matrix[0])
        self.matrix.insert(0,zeros)
        
        for r in range(1,len(self.matrix)):
            for c in range(1,len(self.matrix[0])):
                self.matrix[r][c] += (self.matrix[r][c-1] + self.matrix[r-1][c] - self.matrix[r-1][c-1])
                

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        bottom_right = self.matrix[row2+1][col2+1]
        bottom_left = self.matrix[row2+1][col1]
        top_right = self.matrix[row1][col2+1]
        top_left = self.matrix[row1][col1]
        curr_sum = bottom_right - bottom_left - top_right + top_left
        return curr_sum
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
