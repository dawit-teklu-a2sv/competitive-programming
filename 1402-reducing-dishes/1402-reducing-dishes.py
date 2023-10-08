class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        
        satisfaction.sort(reverse=True)
        res = 0 
        pref = 0
        
        for num in satisfaction:
            pref += num 
            
            if pref > 0:
                res += pref 
        return res
            
        
        def solve(i,t):
            if (i,t) in dp:
                return dp[(i,t)]
            if i == len(satisfaction):
                return 0 
            
            dp[(i,t)] = max( (t * satisfaction[i] + solve(i+1,t+1)),solve(i+1,t))
            return dp[(i,t)]
        
        dp = {}
        satisfaction.sort()
        return solve(0,1)

        