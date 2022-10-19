class Solution:
    def sortSentence(self, s: str) -> str:
        output = sorted(s.split(" "),key = lambda x:x[-1])
        
        return " ".join(x[:-1] for x in output)
        