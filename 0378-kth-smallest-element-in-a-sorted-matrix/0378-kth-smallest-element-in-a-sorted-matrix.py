class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        
        for row in matrix:
            for item in row:
                heapq.heappush(heap,item)
        for i in range(k-1):
            heapq.heappop(heap)
        return heapq.heappop(heap)