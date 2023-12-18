class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        length = len(nums)
        return nums[length-1]*nums[length-2] - nums[1] * nums[0]