#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here 
        x = i
        for j in range(i-1,-1,-1):
            if arr[j] > arr[x]:
                x = j
        return x
                

    def selectionSort(self, arr,n):
        #code here
        for i in range(n-1,-1,-1):
            j = self.select(arr,i)
            arr[i],arr[j]= arr[j],arr[i]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends
