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
        def decodeString(self, s: str) -> str:
 #recursion
        
#         def recur(s):
#             sb = ""
#             k = 0
            
#             while s:
#                 c = s.popleft()
#                 if c in string.ascii_letters:
#                     sb += c
#                 elif c in string.digits:
#                     k = k * 10 + int(c)
                    
#                 elif c == '[':
#                     temp_string = recur(s)
#                     sb += temp_string * k
#                     k = 0
#                 else:
#                     break 
#             return sb
            
#         return recur(deque(s))
            
        
