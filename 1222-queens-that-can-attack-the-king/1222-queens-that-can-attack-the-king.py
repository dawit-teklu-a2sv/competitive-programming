class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        seen = [[False for _ in range(8)] for _ in range(8)]
        for x,y in queens:
            seen[x][y] = True
            
        directions = [-1,0,1]
        result = []
        for i in directions:
            for j in directions:
                if i == 0 and j == 0:
                    continue
                x = king[0]
                y = king[1]
                
                while x+i >=0 and x+i < 8 and y + j >= 0 and y + j < 8:
                    x += i
                    y += j
                    if seen[x][y]:
                        result.append([x,y])
                        break
        return result
                        