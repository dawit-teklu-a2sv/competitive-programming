class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)    
        ans = set()
        def backtrack(curr,start):
            if len(curr) > 1:
                ans.add(tuple(curr))
            last = curr[-1] if curr else -101
            for i in range(start,n):
                if nums[i] >= last:
                    curr.append(nums[i])
                    backtrack(curr,i+1)
                    curr.pop()
        backtrack([],0)
        return ans
    
