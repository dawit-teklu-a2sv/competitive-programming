class Solution:
    def compress(self, chars: list[str]) -> int:
        n = len(chars)
        left = pos = 0
        for right in range(1,n+1):
            if right == n or chars[left] != chars[right]:
                chars[pos] = chars[left]
                pos += 1
                if right-left>1:
                    temp = str(right-left)
                    for c in temp:
                        chars[pos] = c 
                        pos += 1
                left = right 
        return pos