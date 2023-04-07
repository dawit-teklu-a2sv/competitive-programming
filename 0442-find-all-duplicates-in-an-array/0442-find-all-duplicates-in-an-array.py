class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        i = 0
        while i < n:
            pos = nums[i] - 1
            if nums[pos] != nums[i]:
                nums[pos],nums[i] = nums[i],nums[pos]
            else:
                i += 1
        result = []
        for index,item in enumerate(nums):
            if index + 1 != item:
                result.append(item)
        return result
       