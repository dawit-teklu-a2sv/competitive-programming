class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        max_perimeter = 0
        for i in range(len(nums)-2):
            if (nums[i] + nums[i+1]) > nums[i+2]:
                max_perimeter = max(max_perimeter,nums[i] + nums[i+1] + nums[i+2])
        return max_perimeter
        