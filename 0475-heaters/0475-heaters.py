class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        
        houses.sort()
        heaters.sort()
        
        
        radius = 0
        i = 0
        for house in houses:
            
            while i < len(heaters)-1  and heaters[i] <= house:
                i += 1
                
            left = abs(house-(heaters[i-1] if i > 0 else heaters[0]))
            right = abs(heaters[i]-house)
            radius = max(radius,min(left,right))
            
        return radius