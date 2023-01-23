class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        #get the last increasing index and check wheter the items after last index are
        # decreasing or not 
        # Time complexity O(n)
        # Space Complexity O(1)
        increasing_index = 0        
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
        