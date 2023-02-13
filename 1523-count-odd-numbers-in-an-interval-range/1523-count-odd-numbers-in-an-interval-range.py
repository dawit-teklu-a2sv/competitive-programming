class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # if low % 2 == 0 and high % 2 == 0:
        #     return (high - low) // 2 
        # elif low % 2 == 1 and high % 2 == 1:
        #     return ((high + 1)  - ( low - 1)) // 2
        # elif low % 2 == 1:
        #     return (high - (low - 1)) // 2
        # else:
        #     return ((high + 1) - low ) // 2
        if low % 2 != 0:
            low -= 1
        if high % 2 != 0:
            high += 1
        return (high - low) // 2
