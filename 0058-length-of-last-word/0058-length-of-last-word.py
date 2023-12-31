class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        array = s.split(' ')
        processed_array = []
        
        for item in array:
            if len(item) >= 1:
                processed_array.append(item)
        return len(processed_array[-1])
        