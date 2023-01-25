class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = [0] * 26
        for index,item in enumerate(s):
            last_index[ord(item)-ord('a')] = index

        output = []
        right = 0
        left = 0
        for i in range(len(s)):
            right = max(last_index[ord(s[i])-ord('a')],right)
            if right == i:
                output.append(right-left + 1)
                left = i + 1
        return output