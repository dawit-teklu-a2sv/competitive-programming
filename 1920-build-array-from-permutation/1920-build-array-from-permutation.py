class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        #since all items are less thatn the length of input arrays
        # we can take values as index and append array[item] to the output array
        # time complexity O(n)
        # space complexity O(1)
        output = []
        for item in nums:
            output.append(nums[item])
        return output