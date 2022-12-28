class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        incomment = False
        output = []
        temp = ""
        for item in source:
            index = 0
            while index < len(item):
                if index + 1 < len(item) and item[index:index+2] == "//" and not incomment:
                    break
                elif index + 1 < len(item) and item[index:index+2] == "/*" and not incomment:
                    incomment = True
                    index += 2
                    continue
                elif index + 1 < len(item) and item[index:index+2] == "*/" and  incomment:
                    incomment = False
                    index += 2
                    continue
                if  not incomment:
                    temp += item[index]
                index += 1
            if temp != "" and not incomment:
                output.append(temp)
                temp = ""
                
        return output
                    
                    
                