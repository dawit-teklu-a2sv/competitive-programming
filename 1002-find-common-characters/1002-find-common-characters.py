class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        character_map = [[0] * 26 for _ in range(len(words))]
        for  index,word in enumerate(words):
            for char in word:
                character_map[index][ord(char)-ord('a')] += 1
        output = []
        
        for i in range(26):
            temp = float('inf')
            for j in range(len(words)):
                temp = min(temp,character_map[j][i])
            if temp != float('inf') and temp > 0:
                character = chr(ord('a') + i)
                output.extend([character] * temp)
        return output

            
        