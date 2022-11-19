class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        output = 0
        left = 0;right=1
        while right < len(prices):
            output = max(output,prices[right]-prices[left])
            if prices[right] < prices[left]:
                left = right
            right += 1
                
        return output
        