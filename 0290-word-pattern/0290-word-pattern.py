class Solution:
    def returnPattern(self,s):
        temp_dict = {}#takes array item with their previous index
        output = []
        for i in range(len(s)):
            if s[i] in temp_dict:
                output.append(temp_dict[s[i]])
            else:
                temp_dict[s[i]] = i
                output.append(i)
        return output
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_output = self.returnPattern(pattern)       
        s_output = self.returnPattern(s.split())
        return pattern_output == s_output
        