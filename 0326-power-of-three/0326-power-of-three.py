class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        #iterative approach
        
#         if n < 1:
#             return False
#         while n % 3 == 0:
#             n = n//3
            
#         return n == 1
        if n <= 0:
            return False
        elif n%3 != 0 and n != 1:
            return False
        elif n == 3 or n == 1:
            return True
        return self.isPowerOfThree(n//3)
        
        