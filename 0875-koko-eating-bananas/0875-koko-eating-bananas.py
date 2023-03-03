class Solution:
    
    def isPossible(self,piles,h,mid):
        hours = 0
        for p in piles:
            hours += ceil((p)/(mid))
            if hours > h:
                break
        return hours <= h
        
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # brute force approach 
        # min_i = min(piles)
        # max_i = max(piles)
        # i = 1
        # while i <= max_i:
        #     hours = 0
        #     for p in piles:
        #         hours += ceil((p)/(i))
        #         if hours > h:
        #             break
        #     if hours <= h:
        #         break 
        #     i += 1
        # return i
        
        left = 1
        # right = (len(piles) * h) + 1
        right = max(piles) 
        
        while right >= left:
            mid = left + (right - left) // 2
            if self.isPossible(piles,h,mid):
                right = mid - 1
            else:
                left = mid + 1
        return left 
        
        
            
        