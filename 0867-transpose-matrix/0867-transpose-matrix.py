class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix[0])
        m = len(matrix)
        output = [[0] * m for i in range(n)]
        print(output)
        for i in range(m):
            for j in range(n):
                output[j][i] = matrix[i][j]
        return output
                
         
                