class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        i = 0
        duplicates = 0
        while i < len(nums):
            while i < len(nums) - 1 and nums[i+1] == nums[i]:
                i += 1
                duplicates += 1
            nums[index] = nums[i]
            index += 1
            i += 1
        return len(nums) - duplicates



            
        