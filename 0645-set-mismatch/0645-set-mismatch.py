class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        i = 0
        
        while i < n:
            num = nums[i]
            if num - 1 != i and nums[num-1] != num:
                nums[i],nums[num-1] = nums[num-1],nums[i]
            else:
                i += 1
        for index,item in enumerate(nums):
            if index + 1 != item:
                return [item,index+1]
        