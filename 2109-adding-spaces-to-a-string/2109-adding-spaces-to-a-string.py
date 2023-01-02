class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        output = ''
        space = 0 # to track the current space number
        for i in range(len(s)):
            if space < len(spaces) and i == spaces[space]:
                output += ' ' # add space
                space += 1
            output += s[i]
        return output
            
        