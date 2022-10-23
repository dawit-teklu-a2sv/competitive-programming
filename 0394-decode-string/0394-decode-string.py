class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for item in s:
            if item != ']':
                stack.append(item)
            else:
                temp = ""
                
                while stack[-1] != "[":
                    temp = stack.pop() + temp
                stack.pop()
                
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k 
                    
                stack.append(int(k) * temp)
        return "".join(stack)
            
        