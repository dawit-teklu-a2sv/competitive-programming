class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        count = [0 for i in range(len(nums))]
        for i in range(len(nums)):
            nums[i] = [nums[i], i]
        self.mergeSort(nums, 0, len(nums)-1, count)
        return count
    
    def mergeSort(self, nums, start, end, count):
        if start < end:
            mid = start + (end - start)//2
            self.mergeSort(nums, start, mid, count)
            self.mergeSort(nums, mid + 1, end, count)
            self.merge(nums, start, mid, end, count)
        return
    
    def merge(self, nums, start, mid, end, count):
        i = start
        j = mid+1
        k = 0
        temp = [[l, 0] for l in range(end - start+1)]
        
        while(i<=mid and j<=end):
            if nums[i][0] <= nums[j][0]:
                temp[k] = nums[j]
                j += 1
            else:
                temp[k] = nums[i]
                count[nums[i][1]] += (end - j + 1)
                i += 1
            k += 1
        
        while(i<=mid):
            temp[k] = nums[i]
            i+=1
            k+=1
        
        while(j<=end):
            temp[k] = nums[j]
            j+=1
            k+=1        
        for i in range(start, end + 1):
            nums[i] = temp[i-start]