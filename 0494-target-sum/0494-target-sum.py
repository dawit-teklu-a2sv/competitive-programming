class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # count = 0
        n = len(nums)
        total = sum(nums)
        memo = [[float('inf')] * (2 * total + 1) for _ in range(n)]
        def solve(i,summ):
            nonlocal count
            if i == len(nums):
                if summ == target:
                    return 1
                else:
                    return 0
            else:
                if memo[i][summ + total] == float('inf'):
                    add = solve(i+1,summ + nums[i])
                    subtract = solve(i+1,summ - nums[i])
                    memo[i][summ + total] = add + subtract
                return memo[i][summ+total]
        count = solve(0,0)      
        return count