class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        output = []
        for item in nums:
            output.append(nums[item])
        return output