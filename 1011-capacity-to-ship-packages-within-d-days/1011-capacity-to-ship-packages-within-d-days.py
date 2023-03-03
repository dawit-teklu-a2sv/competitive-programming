class Solution:
    def isPossible(self,weights,k,mid):
        current,need = 0,1
        for weight in weights:
            if current + weight > mid:
                need += 1
                current = 0
            current += weight
        print(need,mid)
        return need <= k
            
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        left = max(weights)
        right = sum(weights)
        
        while right > left:
            mid = left + (right - left) // 2
            if self.isPossible(weights,days,mid):
                print(mid)
                right = mid 
            else:
                left = mid + 1
        return left 
        