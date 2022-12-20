class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_counter = Counter(s)
        t_counter = Counter(t)
        for char,item in t_counter.items():
            if char not in s_counter or s_counter[char] != item:
                return char