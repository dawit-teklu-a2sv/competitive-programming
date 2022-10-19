class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        def larger(n1,n2):
            return 1 if n1 + n2 < n2 + n1 else -1 
        
        res = sorted([str(x) for x in nums],key = cmp_to_key(larger))
        return "0" if res[0] == '0' else "".join(res)
