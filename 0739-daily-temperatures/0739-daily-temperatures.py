class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        
        #monotonic stack
        output = [0] * len(t)
        stack = []
        
        for i,a in enumerate(t):
            while stack and stack[-1][0] < a:
                item = stack.pop()
                output[item[1]] = i - item[1]
            stack.append([a,i])
        return output
                
            
        