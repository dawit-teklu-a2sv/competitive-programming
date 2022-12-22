class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = {x:1 for x in nums}
        for i in range(len(nums) + 1):
            if i not in res:
                return i
        