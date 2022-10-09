class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result = []
        for i in range(len(l)):
            result.append(self.checkSubArray(nums[l[i]:r[i]+1]))
        return result
        
    def checkSubArray(self,nums:List[int]) -> bool:
        nums.sort()
        print(nums)
        if len(nums) <2:
            return False
        else:
            temp = nums[1]  - nums[0]
            for i in range(1,len(nums)):
                if nums[i] - nums[i-1] != temp:
                    return False
            return True

        
        