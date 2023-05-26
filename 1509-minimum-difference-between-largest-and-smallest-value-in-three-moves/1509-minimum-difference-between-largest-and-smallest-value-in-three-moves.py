class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n <= 4:
            return 0
        nums.sort()
        left3,right3 = nums[-1] - nums[3],nums[-4]  - nums[0]
        left2,right2 = nums[-2] - nums[2],nums[-3] - nums[1]
        return min(left3,right3,left2,right2)
        