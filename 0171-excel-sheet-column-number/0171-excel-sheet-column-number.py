class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        val = lambda ch: ord(ch)-ord('A') + 1
        hash = 0
        k = 0
        i = len(columnTitle) - 1
        while k < len(columnTitle):
            hash += pow(26,k) * val(columnTitle[i])
            i -= 1
            k += 1
        return hash