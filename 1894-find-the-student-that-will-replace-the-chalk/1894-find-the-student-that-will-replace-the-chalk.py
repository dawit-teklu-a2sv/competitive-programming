class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total = sum(chalk)
        
        k = k % total 
        for i  in range(len(chalk)):
            if k - chalk[i] < 0:
                return i 
            else:
                k -= chalk[i]
        return len(chalk) - 1
      
    
                
                
        