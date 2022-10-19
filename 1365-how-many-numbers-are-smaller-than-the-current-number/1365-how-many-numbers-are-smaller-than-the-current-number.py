class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedNums = sorted(nums,reverse=True)
        count = [0] * ( len(nums) + sortedNums[0])
        res = [0] * len(nums)
        
        for i in range(len(nums)):
            count[nums[i]] += 1
        for j in range(1,len(count)):
            count[j] += count[j-1]
        for i in range(len(res)):
            if nums[i] == 0:
                res[i] = 0
            else:
                res[i] = count[nums[i]-1]
        return res
        