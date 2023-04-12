class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        
        s = set()
        
        def processNum(n):
            for i in range(2,n+1):
                if n % i == 0:
                    while n % i == 0:
                        n //= i
                    s.add(i)
                if n == 1:
                    return 
        for num in nums:
            processNum(num)
        return len(s)