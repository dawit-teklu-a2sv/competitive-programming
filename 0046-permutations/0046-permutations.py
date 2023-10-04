class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def solve(res,subsets,visited):
            if len(subsets) == len(nums):
                res.append(subsets)
            
            for i in range(len(nums)):
                if i not in visited:
                    visited.add(i)
                    solve(res,subsets + [nums[i]],visited)
                    visited.remove(i)
        res = []
        visited = set()
        solve(res,[],visited)
        return res
       