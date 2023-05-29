class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n <= 1:
            return n
        temp_i = -float('inf')
        nums = [0] * (n + 1)
        nums[1] = 1
        for i in range(2,n+1):
            if not i % 2:
                nums[i] = nums[i//2]
            else:
                nums[i] = nums[i//2] + nums[i//2 + 1]
            temp_i = max(temp_i,nums[i])
        return temp_i