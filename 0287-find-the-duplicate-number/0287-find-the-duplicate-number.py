class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        
        n = len(nums)
        
        while i < n:
            num = nums[i]
            if num - 1 != i and nums[num-1] != num:
                nums[num-1],nums[i] = nums[i],nums[num-1]
            else:
                i += 1
        
        for index,item in enumerate(nums):
            if index != item-1:
                return item
