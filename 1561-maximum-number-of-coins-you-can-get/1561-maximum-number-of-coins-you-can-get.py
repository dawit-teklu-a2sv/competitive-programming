class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        i = len(piles) - 2
        j  = 0
        result = 0
        while j < len(piles) // 3:
            result += piles[i]
            j += 1
            i -= 2
        return result
        