class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # good_pairs = 0
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] == nums[j] and i < j:
        #             good_pairs += 1
        # return good_pairs
        good_pairs = 0
        numbers_count = {}
        for item in nums:
            temp = numbers_count.get(item,0)
            good_pairs += temp
            numbers_count[item] = temp + 1
        return good_pairs

            
        