class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        
        arr.sort()
        arr[0] = 1
        n = len(arr)
        for i in range(n-1):
            if abs(arr[i] - arr[i+1]) > 1:
                arr[i+1] = arr[i] + 1
        return arr[-1]
        