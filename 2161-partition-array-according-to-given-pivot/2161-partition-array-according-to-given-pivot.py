class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        #put the elements less than or greater than the pivot element to separate lists as they occur and merge them 
        #time complexity O(n)
        #Space complexity O(n)
        smaller_than_pivot_items = []
        greater_than_pivot_items = []
        pivot_items = 0
        for item in nums:
            if item < pivot:
                smaller_than_pivot_items.append(item)
            elif item > pivot:
                greater_than_pivot_items.append(item)
            else:
                pivot_items += 1
        output =  smaller_than_pivot_items + [pivot] * pivot_items + greater_than_pivot_items
        return output
                
        