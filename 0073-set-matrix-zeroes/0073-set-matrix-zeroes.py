class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = []
        cols = []
        col_len = len(matrix[0])
        row_len = len(matrix)
        for row in range(row_len):
            for col in range(col_len):
                if matrix[row][col] == 0:
                    rows.append(row)
                    cols.append(col)
        for row in rows:
            for column in range(col_len):
                matrix[row][column] = 0
        for col in cols:
            for row in range(row_len):
                matrix[row][col] = 0
            
        