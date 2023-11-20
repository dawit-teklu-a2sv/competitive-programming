class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
            
        for index,item in enumerate(nums):
            if target - item in d:
                if index != d[target -item]:
                    return [index,d[target-item]]
                        
            d[item] = index

        
        