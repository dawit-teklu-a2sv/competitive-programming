class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        n = len(digits)
        last_digit_sum = digits[-1] + 1
        offset = last_digit_sum // 10 
        digits[n-1] = last_digit_sum % 10
        m = n - 2
        while m >= 0:
            temp = (digits[m] + offset)
            digits[m] = temp % 10
            offset = temp // 10
            m -= 1
        if offset > 0:
            digits.insert(0,offset)
        return digits
            
            
        