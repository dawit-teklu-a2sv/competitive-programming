class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def larger(n1, n2):
            return 1 if n1+n2<n2+n1 else -1
        sorted_nums = sorted([str(n) for n in nums], key=cmp_to_key(larger))
        return "0" if sorted_nums[0] == "0" else "".join(sorted_nums)
            
    