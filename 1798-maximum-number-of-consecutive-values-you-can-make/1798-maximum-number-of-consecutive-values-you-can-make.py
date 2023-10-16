class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        
        summ = 0 
        coins.sort()
        for coin in coins:
            if coin > summ + 1:
                break
            summ += coin
        return summ + 1
        