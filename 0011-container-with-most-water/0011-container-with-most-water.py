class Solution:
    def maxArea(self, height: List[int]) -> int:
        #brute force not working
        # result = 0
        # for l in range(len(height)):
        #     for r in range(l + 1, len(height)):
        #         width = r - l
        #         h = min(height[l],height[r])
        #         area = width * h
        #         if area > result:
        #             result = area
        # return result
        
        left = 0
        right = len(height) - 1
        area = 0
        while left < right:
            output = (right - left) * min(height[left],height[right])
            area = max(area,output)
            if height[left] > height[right]:
                right -= 1
            elif height[left] < height[right]:
                left += 1
            
            elif height[left] == height[right] and height[left + 1] > height[right-1]:
                left += 1
            else:
                right -= 1
        return area
                

        