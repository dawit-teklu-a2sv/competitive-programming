# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n 
        
        bad_version = -1
        while left <= right:
            mid = (left + right) // 2
            if(isBadVersion(mid)):
                bad_version = mid 
                right = mid - 1
            else:
                left = mid + 1
        return bad_version
            
            