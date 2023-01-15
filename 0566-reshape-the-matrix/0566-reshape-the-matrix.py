class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) * len(mat[0]) != r * c:
            return mat
        output = [[0] * c for _ in range(r)]
        row = 0
        col = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if col == c:
                    row += 1
                    col = 0
                output[row][col] = mat[i][j]
                col += 1
        return output