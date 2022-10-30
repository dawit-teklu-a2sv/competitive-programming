class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        duplicate = False
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                duplicate = True
        return duplicate