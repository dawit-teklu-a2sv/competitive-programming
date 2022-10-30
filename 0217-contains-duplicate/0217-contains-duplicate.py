class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for item in nums:
            if item in d:
                return True
            else:
                d[item] = 1
        return False
                    
                    
        # nums.sort()
        # for i in range(1,len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return True
        # return False