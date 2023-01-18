class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #Transpose
        for i in range(len(matrix)):
            for j in range(i,len(matrix[0])):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        for i in range(len(matrix)):
            start = 0
            end = len(matrix[i]) - 1
            while start < end:
                matrix[i][start],matrix[i][end] = matrix[i][end],matrix[i][start]
                start += 1
                end -= 1
