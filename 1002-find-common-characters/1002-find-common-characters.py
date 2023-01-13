class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        #count the occurence of every character using their ASCII value and put them on 2d array
        #check if a character found in all words and mark the minimum occurence 
        #append it to output array
        #time complexity O(n*longestword length)
        #space compleixty O(26 * n)
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

            
        