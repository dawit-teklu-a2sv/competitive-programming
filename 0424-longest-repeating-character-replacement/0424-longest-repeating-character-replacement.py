class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=right = 0
        res = 0
        counter = Counter()
        while right < len(s):
            counter[s[right]] = counter[s[right]] + 1
            currentMaximum = max(counter.values())
            if right - left + 1 - currentMaximum >k:
                counter[s[left]] -= 1
                left += 1
            res = max(res,right-left+1)
            right += 1
            
        return res
