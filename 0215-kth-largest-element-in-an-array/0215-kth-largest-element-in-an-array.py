class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quicksort(arr,start,end):
            if end - start <= 1:
                return 
            pivot = arr[start]
            write = start + 1
            
            for read in range(start+1,end):
                
                if pivot >= arr[read]:
                    arr[write],arr[read] = arr[read],arr[write]
                    write += 1
            arr[start],arr[write-1] = arr[write-1],arr[start]
            
            quicksort(arr,start,write-1)
            quicksort(arr,write,end)
        quicksort(nums,0,len(nums))
        print(nums)
        return nums[-k]
        