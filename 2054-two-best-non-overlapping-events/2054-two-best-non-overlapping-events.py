class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        def binarySearch(low, high, key):
            if low <= high:
                mid = (low+high)//2
                if events[mid][1] >= key:
                    return binarySearch(low, mid-1, key)
                else:
                    return binarySearch(mid+1, high, key)
            return high
        
        events.sort(key=lambda x: x[1])
        dp = [0 for _ in range(len(events))]
        dp[0] = events[0][2]
        for i in range(1, len(events)):
            dp[i] = max(dp[i-1], events[i][2]) # maximum values if only one selection was allowed         
        
        maxi = events[0][2]
        
        for i in range(1, len(events)):
            cur = events[i][2]
            prev =  binarySearch(0, len(events), events[i][0]) # previos non-overlapping index
            maxi = max(maxi, cur+dp[prev]) if prev != -1 else max(maxi, cur)
        return maxi