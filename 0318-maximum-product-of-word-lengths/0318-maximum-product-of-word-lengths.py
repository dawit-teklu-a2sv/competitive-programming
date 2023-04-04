class Solution:
    def maxProduct(self, words: List[str]) -> int:
        temp = [[set(word),len(word)] for word in words]
        n = len(words)
        ans = 0
        for i in range(n):
            word1,length1 = temp[i]
            for j in range(i+1,n):
                word2,length2 = temp[j]
                if not len(word1.intersection(word2)):
                    ans = max(length1 * length2,ans)
        return ans