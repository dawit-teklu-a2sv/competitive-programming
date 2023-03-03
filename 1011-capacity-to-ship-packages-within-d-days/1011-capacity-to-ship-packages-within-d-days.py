class Solution:
    def isPossible(self,weights,k,mid):
        current,need = 0,1
        for weight in weights:
            if current + weight > mid:
                need += 1
                current = 0
            current += weight
        return need <= k
            
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        left = max(weights)  - 1
        right = sum(weights) + 1
        
        while right > left + 1:
            mid = left + (right - left) // 2
            if self.isPossible(weights,days,mid):
                right = mid 
            else:
                left = mid 
        return right 
        