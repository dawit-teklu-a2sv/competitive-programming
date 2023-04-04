class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)
        for i in range(n):
            temp = nums[i]
            if temp == k:
                count += 1
            for j in range(i+1,n):
                temp = gcd(temp,nums[j])
                if temp == k:
                    count += 1
        return count
            