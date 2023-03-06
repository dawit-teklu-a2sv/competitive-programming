class Solution:
    def __init__(self):
        self.d = {}
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        words = sorted(words,key = lambda word: self.getValue(word))
        output = [0] * len(queries)
        for i,query in enumerate(queries):
            output[i] = len(words) - self.find(words,self.getValue(query))
        return output
    
    def find(self,words,limit):
        low = 0
        high = len(words) - 1
        
        while low < high:
            mid = low + (high - low) // 2
            
            if self.getValue(words[mid]) > limit:
                high = mid
            else:
                low = mid + 1
        if low == high and self.getValue(words[low]) <= limit:
            return len(words)
        return low
    def getValue(self,s):
        if s in self.d:return self.d[s]
        lowest = 123
        freq = 0
        for char in s:
            if ord(char) < lowest:
                lowest = ord(char)
                freq = 1
            if ord(char) == lowest:
                freq += 1
        self.d[s] = freq
        return freq
        
        
    
        