class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        temp_max = 0
        count = 0
        curr = 0
        for i in range(len(nums)-1):
            temp_max = max(temp_max,i + nums[i])
            if curr == i:
                curr = temp_max
                count += 1
            if curr > len(nums) -1:
                return count
        return count
                
        