class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = -float('inf')        
        max_at_current_index = 0
        for item in nums:
            max_at_current_index += item
            if max_at_current_index < item:
                max_at_current_index = item
            if max_so_far < max_at_current_index:
                max_so_far = max_at_current_index
        return max_so_far
            
                
            