class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        #add all items and their reverses to set
        # return length of set
        # time complexity O(n)
        # space complexity O(n)
    
        output = set([item for item in nums])
        for item in nums:
            output.add(int(str(item)[::-1]))
        return len(output)