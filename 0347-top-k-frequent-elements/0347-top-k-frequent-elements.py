class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        b = Counter(nums)
        for i in nums:
            if i in b:
                b[i] += 1
            else:
                b[i] = 1
        return list({k:v for k,v in sorted(b.items(), key = lambda item: -item[1])})[:k]
        