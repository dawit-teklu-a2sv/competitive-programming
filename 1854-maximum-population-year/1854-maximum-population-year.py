class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        pref_sum = [0] * 101
        
        for birth,death in logs:
            pref_sum[birth-1950] += 1
            pref_sum[death-1950] -= 1
        for i in range(1,100):
            pref_sum[i] += pref_sum[i-1]
            
        ans = 0 
        
        for i in range(100):
            if pref_sum[i] > pref_sum[ans]:
                ans = i 
        return 1950 + ans 
        
        