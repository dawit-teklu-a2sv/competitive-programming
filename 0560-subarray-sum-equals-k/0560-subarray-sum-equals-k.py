class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefSum = 0
        d = {0:1}
        
        for num in nums:
            prefSum += num
            
            if prefSum - k in d:
                count += d[prefSum-k]
            if prefSum in d:
                d[prefSum] += 1
            else:
                d[prefSum] = 1
        return count
        