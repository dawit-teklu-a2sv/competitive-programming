class Solution:
    def balancedString(self, s: str) -> int:
        counter = Counter(s)
        res = n = len(s)
        i = 0
        for j in range(n):
            counter[s[j]] -= 1
            while i < n and all(n/4 >= counter[c] for c in 'QWER'):
                res = min(res,j-i+1)
                counter[s[i]] += 1
                i += 1
        return res
    