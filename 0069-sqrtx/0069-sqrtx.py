class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        
        left = 0
        right = x + 1
        
        while left < right -1:
            mid = left + (right - left) // 2
            
            temp = x // mid
            
            # if temp == mid:
            #     return mid
            if mid > temp:
                right = mid 
            else:
                left = mid
        return left
        
        