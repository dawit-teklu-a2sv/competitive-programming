class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n 
        dp[n-1] = nums[n-1]
        queue = deque()
        queue.appendleft(n-1)
        for i in range(n-2,-1,-1):
            if queue[-1] - i > k:
                queue.pop()
            dp[i] = nums[i] + dp[queue[-1]]
            
            while queue and dp[queue[0]] < dp[i]:
                queue.popleft()
            queue.appendleft(i)
        return dp[0]
                    
                
        