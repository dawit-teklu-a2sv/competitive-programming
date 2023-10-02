class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        words_set = set(words)
        ans = ""
        
        for word in words:
            if len(word) > len(ans) or len(word) == len(ans) and word < ans:
                if(all(word[:i] in words_set for i in range(1,len(word)))):
                    ans = word
        return ans
    