class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s = s + s
        alt1,alt2 = "",""
        diff1,diff2 = 0,0
        
        for i in range(len(s)):
            if i % 2 == 0:
                alt1 += "1"
                alt2 += "0"
                
            else:
                alt1 += "0"
                alt2 += "1"
                
        left = 0
        res = len(s)
        for right in range(len(s)):
            if alt1[right] != s[right]:
                diff1 += 1
            if alt2[right] != s[right]:
                diff2 += 1
                
            if (right-left + 1 > n):
                if alt1[left] != s[left]:
                    diff1 -= 1
                if alt2[left] != s[left]:
                    diff2 -= 1
                left += 1
            if (right-left + 1 == n):
                res = min(res,diff1,diff2)
        return res

        