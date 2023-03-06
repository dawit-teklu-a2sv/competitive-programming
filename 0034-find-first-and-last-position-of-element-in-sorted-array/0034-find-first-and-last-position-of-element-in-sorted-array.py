class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        

        output = [-1,-1]
        if not len(nums):
            return output 
        i = 0
        j = len(nums) - 1
        
        while i < j:
            mid = i + (j-i) // 2
            
            if nums[mid] < target:i = mid+1
            else:j = mid
        if nums[i] != target:
            return output
        else:
            output[0] = i 
        
        i = 0
        j = len(nums) -1
        while i < j:
            mid = (j+i) // 2 + 1
            if nums[mid] > target:j=mid-1
            else:
                i = mid
        output[1] = j
        return output
            
        