class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        if len(arr) < 3:
            return -1
        low = 1
        high = len(arr)-2
        
        while low <= high:
            mid = low + (high-low)//2
            if arr[mid-1] < arr[mid] < arr[mid+1]:
                low = mid + 1            
            elif arr[mid-1] > arr[mid] > arr[mid+1]:
                high = mid - 1

            else:
                return mid
            
            
