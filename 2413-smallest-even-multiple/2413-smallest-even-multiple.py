class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        for i in range(2,2*n + 1):
            #iterating over 2x of n because the higer limit would be 2x of n
            if i % 2 == 0 and i %n == 0:#checking if a number is both multiple of 2 and n 
                return i
        