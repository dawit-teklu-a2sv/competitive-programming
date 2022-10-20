class Solution:
    def isValid(self, s: str) -> bool:
        braces = {")":"(","]":"[","}":"{"}
        stack = []
        for i in s:
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
            else:
                if stack:
                    temp = stack.pop()
                    if braces[i] != temp:
                      return False
                else:
                    return False
        return True if not stack else False
                

        