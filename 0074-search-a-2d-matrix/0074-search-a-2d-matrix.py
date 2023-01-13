class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = None
        
        for i in range(len(matrix)):
            if target <= matrix[i][len(matrix[i])-1] and target >= matrix[i][0]:
                row = i
                
                
        if row != None:
            for i  in range(len(matrix[row])):
                if matrix[row][i] == target:
                    return True
        return False
    

        