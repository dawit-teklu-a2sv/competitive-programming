class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-1 * item for item in piles]
        heapq.heapify(piles)
        for i in range(k):
            item = abs(heapq.heappop(piles))
            heapq.heappush(piles,item//2 - item)
        return sum([abs(item) for item in piles])
        