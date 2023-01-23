class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        increasing_index = 0
        decreasing_index = 0
        
        for i in range(1,len(arr)):
            if arr[i] > arr[i-1]:
                increasing_index += 1 
            else:
                break
        if increasing_index == 0  or increasing_index + 1 == len(arr) :
            return False
        valley = True
        for j in range(increasing_index,len(arr)-1):
            if arr[j] <= arr[j+1]:
                valley = False
        return valley
        