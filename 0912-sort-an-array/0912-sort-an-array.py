class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def mergeSort(left,right,arr):
            if left == right:
                return [arr[left]]
            
            mid = (left + right) // 2
            left_half = mergeSort(left,mid,arr)
            right_half = mergeSort(mid + 1, right,arr)
            return merge(left_half,right_half)
        def merge(left_array, right_array):
            output = []
            left = 0
            right = 0
            n = len(left_array)
            m = len(right_array)
            while left < n and right < m:
                if left_array[left] < right_array[right]:
                    output.append(left_array[left])
                    left += 1
                else:
                    output.append(right_array[right])
                    right += 1
            while left < n:
                output.append(left_array[left])
                left += 1
            while right < m:
                output.append(right_array[right])
                right += 1
            return output
        return mergeSort(0,len(nums)-1,nums)