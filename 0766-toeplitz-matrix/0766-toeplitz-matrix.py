class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        diagonal_elements = defaultdict(set)
        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                diagonal_elements[row-column].add(matrix[row][column])
        for _,value in diagonal_elements.items():
            if len(value) > 1:
                return False
        return True