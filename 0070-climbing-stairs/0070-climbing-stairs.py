class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def cBSolve(start,memo):
            if start >= n:
                if start == n:
                    return 1
                else:
                    return 0
            if start not in memo:
                temp =  cBSolve(start + 1,memo) + cBSolve(start + 2,memo)
                memo[start] = temp
            return memo[start]

        cBSolve(0,memo)
        
        return memo[0]
       
            
        