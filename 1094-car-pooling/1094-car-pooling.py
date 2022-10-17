class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        trips.sort(key = lambda t:t[1])
        
        minHeap = []#takes [end, and noOfPassangeer of last trip]
        currentPass = 0
        for t in trips:
            numPass,start,end = t
            
            while minHeap and minHeap[0][0] <= start:
                currentPass -= minHeap[0][1]
                heapq.heappop(minHeap)#trip was ended
            currentPass += numPass
            heapq.heappush(minHeap,[end,numPass])
            if currentPass > capacity:
                return False
        return True

        
        
        