class Solution:
    def findComplement(self, num: int) -> int:
        count = 0
        output = 0
        while num > 0:
            output += (2 ** count) * (0 if num & 1 else 1)
            count += 1
            num >>= 1
        return output
            