class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for item in nums:
            xor ^= item
        return xor
        
        