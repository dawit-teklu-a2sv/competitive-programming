class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        while i < n:
            temp = nums[i]
            if nums[i] == i or temp == n:
                i += 1
            else:
                nums[i],nums[temp] = nums[temp],nums[i]
        for i,item in enumerate(nums):
            if i != item:
               return i
        return n
        