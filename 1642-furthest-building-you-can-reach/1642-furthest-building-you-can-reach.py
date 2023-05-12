class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        n = len(heights)
        for i in range(n-1):
            diff = heights[i+1] - heights[i]
            
            if diff > 0:
                if ladders > 0:
                    heapq.heappush(heap,diff)
                    ladders -= 1
                elif heap and diff > heap[0]:
                    d = heapq.heappushpop(heap,diff)
                    bricks -= d
                else:
                    bricks -= diff
                if bricks < 0:
                    return i 
            print(i,bricks)
        return n - 1
    