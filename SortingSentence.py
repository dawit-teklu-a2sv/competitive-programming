class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(' ')
        n = len(words)
        output = [' '] * n 
        for i,a in enumerate(words):
            index = int(a[-1])
            word = a[:-1]
            output[index-1] = word
        return " ".join(output)
