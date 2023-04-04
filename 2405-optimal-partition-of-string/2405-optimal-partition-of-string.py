class Solution:
    def partitionString(self, s: str) -> int:
        m = {}
        count = 1 # since we take the whole string
        
        for item in s:
            if item in m:
                count += 1
                m.clear()
            m[item] = 1
        return count
            