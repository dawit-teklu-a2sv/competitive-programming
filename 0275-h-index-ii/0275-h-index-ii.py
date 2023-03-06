class Solution:
    
    def isPossible(self,citations,item):
        count = 0
        for cit in citations:
            if cit >= item:
                count += 1
        return count >= item
        
    def hIndex(self, citations: List[int]) -> int:
        
        low = 0
        high = max(citations) + 1
        
        while low < high - 1:
            mid = low + (high-low) // 2
            
            if self.isPossible(citations,mid):
                low = mid 
            else:
                high = mid 
        return low
