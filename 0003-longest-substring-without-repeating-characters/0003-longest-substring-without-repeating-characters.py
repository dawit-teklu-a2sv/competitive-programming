class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #         charSet = set()
        # l = 0
        # r = 0
        # res = 0 
        # while r < len(s):
        #     if s[r] not in charSet:
        #         charSet.add(s[r])
        #         r += 1
        #         res = max(len(charSet),res)
        #     else:
        #         print(f"sets {charSet}, s[{l}]: {s[l]}")
        #         charSet.remove(s[l])
        #         l += 1
        # return res
        charSet = set()
        l = 0
        res = 0 
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res,r - l + 1)
        return res
