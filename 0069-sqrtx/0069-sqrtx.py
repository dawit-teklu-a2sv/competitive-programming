class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        
        left = 1
        right = x 
        
        while left <= right:
            mid = left + (right - left) // 2
            
            temp = x // mid
            
            if temp == mid:
                return mid
            elif mid > temp:
                right = mid -1
            else:
                left = mid + 1
        return right
        
        