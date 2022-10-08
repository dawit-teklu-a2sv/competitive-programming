class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        output = [int(x) for x in nums]
        output = sorted(output,reverse=True)
        return  str(output[k-1])