class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}
        
        def triSolve(n):
            if n == 0:
                return 0
            if n <= 2:
                return 1
            if n not in memo:
                temp = triSolve(n-1) + triSolve(n-2) + triSolve(n-3)
                memo[n] = temp
            return memo[n]
        
        return triSolve(n)
        