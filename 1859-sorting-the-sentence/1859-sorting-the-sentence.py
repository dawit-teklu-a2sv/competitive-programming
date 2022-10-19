class Solution:
    def sortSentence(self, s: str) -> str:
        res = s.split(" ")
        output = [''] * len(res)
        for item in res:
            output[int(item[-1]) - 1] = item[:-1]
        return " ".join(output)
        