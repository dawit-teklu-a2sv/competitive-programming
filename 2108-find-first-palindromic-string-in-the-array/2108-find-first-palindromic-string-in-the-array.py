class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def checkPalindrome(word):
            i = 0
            j = len(word)-1
            
            while i < j:
                if word[i] == word[j]:
                    i += 1
                    j -= 1
                else:
                    return False
            return True
        for word in words:
            if checkPalindrome(word):
                return word
        return ""
        