class Solution:
    def calculateXor(self,n):
        if n % 4 == 0:
            return n
        if n % 4 == 1:
            return 1
        if n % 4 == 2:
            return n + 1
        else:
            return 0
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        temp = self.calculateXor(n)
        xor = 0
        for i in nums:
            xor ^= i
        return xor ^ temp
        