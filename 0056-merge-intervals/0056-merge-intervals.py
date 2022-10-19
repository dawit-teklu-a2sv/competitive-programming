class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         intervals = sorted(intervals,key = lambda interval: interval[0])    
#         ans = []
#         i = 0
        
#         while i < len(intervals):
#             start = intervals[i][0]            
#             end = intervals[i][1]
#             i+= 1
            
#             while i < len(intervals) and intervals[i][0] <= end:
#                 end = max(end,intervals[i][1])
#                 i += 1
#             ans.append([start,end])
#         return ans
        intervals.sort()
        stack = [intervals[0][0],intervals[0][1]]
        
        for i in range(len(intervals)):
            if intervals[i][0] <= stack[-1]:
                if intervals[i][1] <= stack[-1]:
                    continue
                else:
                    stack.pop()
            else:
                stack.append(intervals[i][0])
            stack.append(intervals[i][1])
        output = []
        for i in range(0,len(stack),2):
            output.append([stack[i],stack[i+1]])
        return output
        print("stack ",stack)
    
    
    