class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        maxSum = 0
        length = len(nums) - 1
        for i in range(length):
            maxSum = max(maxSum, (nums[i] + nums[length-i]))
        return maxSum
            
        