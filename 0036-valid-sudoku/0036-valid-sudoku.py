class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows  = defaultdict(set)
        squares = defaultdict(set)
        
        for row in range(9):
            for column in range(9):
                value = board[row][column]
                if value == ".":
                    continue
                else:
                    if value in cols[column] or value in rows[row] or value in squares[(row//3,column//3)]:
                        return False
                cols[column].add(value)
                rows[row].add(value)
                squares[(row//3,column//3)].add(value)
        return True
                    
       