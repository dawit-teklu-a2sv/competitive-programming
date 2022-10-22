class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right = 0,len(height)-1
        area = 0
        while left < right:
            output = min(height[left],height[right]) * (right - left)
            area = max(area,output)
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1 
        return area
            
    

                

        