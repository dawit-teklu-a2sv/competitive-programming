class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        output = []
        last_indices = [0] * 26
        for i in range(len(s)):
            last_indices[ord(s[i])-ord('a')] = i 
        start = 0
        end = 0
        for i in range(len(s)):
            end = max(last_indices[ord(s[i])-ord('a')],end)
            if (i == end):
                output.append(end-start + 1)
                start = end + 1
        return output