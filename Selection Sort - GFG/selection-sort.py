#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here 
        temp = i 
        for j in range(i,len(arr)):
            if arr[temp] > arr[j]:
                temp = j
        return temp
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(len(arr)):
            temp = self.select(arr,i)
            arr[i],arr[temp] = arr[temp],arr[i]
        
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