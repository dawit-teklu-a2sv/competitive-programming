class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        output = []
        nums.sort()
        for i,a in enumerate(nums):
            if a == target:
                output.append(i)
        return output
