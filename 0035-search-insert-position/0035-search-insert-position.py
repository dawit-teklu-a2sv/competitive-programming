class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        low = -1
        high = len(nums)
        
        while high > low + 1:
            mid = low + (high - low) // 2
            
            if target > nums[mid]:
                low = mid 
            else:
                high = mid 
        return high
        