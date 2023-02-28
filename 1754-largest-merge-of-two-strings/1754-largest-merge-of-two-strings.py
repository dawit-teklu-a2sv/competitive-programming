class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        if len(word1) == 0 == len(word2):
            return ""
        if len(word1) == 0:return word2
        if len(word2) == 0:return word1
        
        if word1 > word2:
            return word1[0] + self.largestMerge(word1[1:],word2)
        else:
            return word2[0] + self.largestMerge(word1,word2[1:])
        
        