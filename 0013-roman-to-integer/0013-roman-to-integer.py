class Solution:
    def romanToInt(self, s: str) -> int:
        numbers = {'I':1,"V":5,'X':10,'L':50,"C":100,"D":500,"M":1000}
        output= 0
        right = 0
        
        while right <= len(s) - 1:

            if  right < len(s) - 1 and numbers[s[right]] < numbers[s[right + 1]]:
                output += (numbers[s[right + 1]] - numbers[s[right]])
                right += 2
            else:
                output += (numbers[s[right]])
                right += 1
        return output
                
            