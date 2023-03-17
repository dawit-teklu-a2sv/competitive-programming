class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_sum = [0]
        for x in nums: prefix_sum.append(prefix_sum[-1] + x)
        counter = Counter()
        ans = 0
        for x in prefix_sum:
            ans += counter[x]
            counter[x + goal] += 1
        return ans
                