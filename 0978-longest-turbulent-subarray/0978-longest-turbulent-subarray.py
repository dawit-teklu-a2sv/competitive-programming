class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        
        def compare(a,b):
            return (a>b)-(a<b)
        
        left = 0
        result = 1
        n = len(arr)
        for right in range(1,n):
            c = compare(arr[right-1],arr[right])
            if c == 0:
                left = right
            elif right == n-1 or c * compare(arr[right],arr[right+1]) != -1:
                result = max(result,right-left + 1)
                left = right
        return result
        
        
        
        