class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        freq = [0] * (n+1)
        
        for s,e in requests:
            freq[s] += 1
            freq[e+1] -= 1
            
        for i in range(1,n+1):
            freq[i] += freq[i-1]
        freq.pop()
        ans = 0
        freq = sorted(freq)
        nums = sorted(nums)
        for num,freq in zip(freq,nums):
            ans += (num * freq)
        return ans %(10**9 + 7)