# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n + 1
        
        bad_version = -1
        while left < right - 1:
            mid = (left + right) // 2
            if(isBadVersion(mid)):
                bad_version = mid 
                right = mid 
            else:
                left = mid 
        return bad_version
            
            