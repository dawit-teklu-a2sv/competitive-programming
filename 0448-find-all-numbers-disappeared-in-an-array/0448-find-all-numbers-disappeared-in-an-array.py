class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        n = len(nums)
        
        while i < n:
            pos = nums[i] - 1
            if nums[i] != nums[pos]:
                nums[i],nums[pos] = nums[pos],nums[i]
            else:
                i += 1
        result = []
        for i,item in enumerate(nums):
            if i + 1 != item:
                result.append(i+1)
        return result
    