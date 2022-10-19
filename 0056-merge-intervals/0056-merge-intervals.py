class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals,key = lambda interval: interval[0])    
        ans = []
        i = 0
        
        while i < len(intervals):
            start = intervals[i][0]            
            end = intervals[i][1]
            i+= 1
            
            while i < len(intervals) and intervals[i][0] <= end:
                end = max(end,intervals[i][1])
                i += 1
            ans.append([start,end])
        return ans