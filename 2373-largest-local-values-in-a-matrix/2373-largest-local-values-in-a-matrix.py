class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        row = len(grid)
        column = len(grid[0])
        maxLocal = [[1] * (column-2) for _ in range(row-2)]
        for i in range(len(maxLocal)):
            for j in range(len(maxLocal[0])):
                temp = 1
                for row in range(i,i+3):
                    for col in range(j,j+3):
                        temp = max(grid[row][col],temp)
                maxLocal[i][j] = temp
        return maxLocal

                