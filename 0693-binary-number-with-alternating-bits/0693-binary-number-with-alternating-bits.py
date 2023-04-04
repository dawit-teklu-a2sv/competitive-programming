class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        length = n.bit_length()
        mask = (1 << length) - 1
        if mask ^ n == n >> 1:
            return True
        return False
       