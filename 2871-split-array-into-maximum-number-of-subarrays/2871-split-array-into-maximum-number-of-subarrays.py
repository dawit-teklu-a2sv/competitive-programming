class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        
        bit_result = nums[0]
        
        for num in nums:
            bit_result &= num 
            
        if bit_result != 0:
            return 1
        
        count = 0
        bit_result = nums[0]
        for index,num in enumerate(nums):
            bit_result &= num
            
            if bit_result == 0:
                count += 1
                if index < len(nums)-1:
                    bit_result = nums[index+1]
        return count
        
        