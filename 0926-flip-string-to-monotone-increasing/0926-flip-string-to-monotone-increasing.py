class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        count_one,count_flip = 0,0
        for char in s:
            if char == '1':
                count_one += 1
            else:
                count_flip += 1
                count_flip = min(count_flip,count_one)
        return count_flip
