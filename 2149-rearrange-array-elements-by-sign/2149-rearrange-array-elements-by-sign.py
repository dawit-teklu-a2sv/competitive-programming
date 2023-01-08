class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        #Splitting positive and negative items to two arrays
        #Merging the two arrays
        #Time complexity O(n)
        #Space complexity O(n)
        positive_arrays = []
        negative_arrays = []
        
        for item in nums:
            if item > 0:
                positive_arrays.append(item)
            else:
                negative_arrays.append(item)
        length = len(nums)
        positive_items = 0
        negative_items = 0
        result = []
        for i in range(length):
            if i %2 ==0:
                result.append(positive_arrays[positive_items])
                positive_items += 1
            else:
                result.append(negative_arrays[negative_items])
                negative_items += 1                
        return result
