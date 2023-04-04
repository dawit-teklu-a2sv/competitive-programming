class Solution:
    def maxProduct(self, words: List[str]) -> int:
        #brute force approach
        # temp = [[set(word),len(word)] for word in words]
        # n = len(words)
        # ans = 0
        # for i in range(n):
        #     word1,length1 = temp[i]
        #     for j in range(i+1,n):
        #         word2,length2 = temp[j]
        #         if not len(word1.intersection(word2)):
        #             ans = max(length1 * length2,ans)
        # return ans
        n = len(words)
        ans = 0
        mask = [0] * n
        for i in range(n):
            for char in words[i]:
                mask[i] |= 1 << (ord(char)-ord('a'))
            for j in range(i):
                if mask[i] & mask[j] == 0:
                    ans = max(ans,len(words[i]) * len(words[j]))
        return ans