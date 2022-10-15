class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l,r = 0, len(cardPoints) - k 
        
        total = sum(cardPoints[r:])
        result = total
        print(f"result {result}")
        while r < len(cardPoints):
            print(r)
            total  += (cardPoints[l] - cardPoints[r])
            print(f"temp {total}")
            result = max(result,total)
            r += 1
            l += 1
            
        return result
            
        