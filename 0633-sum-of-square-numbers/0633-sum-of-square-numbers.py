class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        left = 0
        right = int(sqrt(c)) 
        
        while left <= right:
            temp_square = pow(left,2) + pow(right,2)
            if temp_square == c:
                return True
            elif temp_square > c:
                right -= 1
            else:
                left += 1
        return False
        