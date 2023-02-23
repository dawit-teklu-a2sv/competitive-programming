class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix_sum = [0] * len(s)
        for shift in shifts:
            start,end,direction = shift
            if direction == 1:
                prefix_sum[start] += 1
                if end + 1 < len(s):
                    prefix_sum[end+1] -= 1
            else:
                prefix_sum[start] -= 1
                if end + 1 < len(s):
                    prefix_sum[end+1] += 1
        n = len(prefix_sum)
        for i in range(1,n):
            prefix_sum[i] += prefix_sum[i-1]
        output = ""
        for i in range(n):
            temp = ord(s[i]) - ord('a')
            temp_ord = (temp + prefix_sum[i]) % 26
            output += chr(temp_ord + ord('a'))

        return output