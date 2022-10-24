class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n == 0:
            return 1
        if x == 0:
            return 0
        if n < 0:
            return 1/self.myPow(x,-n)
        p = self.myPow(x, n //2 )
        if n %2 == 0:
            return p * p
        else:
            return p * p * x
            

        