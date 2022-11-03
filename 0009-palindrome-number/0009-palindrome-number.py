class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        output = 0
        y = x
        while y > 0:
            remainder = y % 10
            output = output * 10 + remainder
            y = y // 10
        return output == x
        