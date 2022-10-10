class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        result = True
        for i in s:
            if i in '([{':
                stack.append(i)
            else:
                try:
                    output = stack.pop()
                    if i == ')' and output == '(':
                        pass 
                    elif i == '}' and output == '{':
                        pass
                    elif i == ']' and output == '[':
                        pass
                    else:
                        result = False
                except:
                    return False
        return result if not len(stack) else False
        
                
                
                    
                    


                       
                       
                       
                       
                       
                       
                       
                
                
        