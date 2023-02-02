class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left,right = 0, len(nums)-1
        output = 0
        while left < right:
            temp_sum =  nums[left] + nums[right] 
            if temp_sum == k:
                output += 1
                right -= 1
                left += 1
            elif temp_sum > k:
                right -= 1
            else:
                left += 1
        return output
                
            
            
            
        
        
        
        