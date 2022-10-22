class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        need = 0
        for num in nums:
            res += max(need - num,0)
            need = max(need,num) + 1
            
        return res
        