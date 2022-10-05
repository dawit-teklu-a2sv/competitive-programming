class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        output = []
        for i,a in enumerate(nums):
            count = 0
            for j,b in enumerate(nums):
                if a > b:
                    count += 1
            output.append(count)
        return output
      
